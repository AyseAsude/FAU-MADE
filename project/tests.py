import pandas as pd
import unittest
import io
from extract_transform import check_and_get_encoding, save_as_csv, load, transform_2019_data
from unittest.mock import patch, PropertyMock
from requests import Response


class TestPipeline(unittest.TestCase):

    @patch('requests.get')
    def test_check_returns_str_for_ok_status(self, mock_get):

        mock_response = Response()
        mock_response.status_code = 200
        content_mock = PropertyMock(return_value=b'some content')
        type(mock_response).content = content_mock
        mock_get.return_value = mock_response

        url = "https://google.com"
        result = check_and_get_encoding(url)
        self.assertIsInstance(result, str)
        
    @patch('requests.get')
    def test_check_returns_none_for_non_ok_status(self, mock_get):
       
        mock_response = Response()
        mock_response.status_code = 404
        content_mock = PropertyMock(return_value=b'some content')
        type(mock_response).content = content_mock
        mock_get.return_value = mock_response

        url = "http://example.com"
        result = check_and_get_encoding(url)
        self.assertIsNone(result)

    @patch('pandas.DataFrame.to_csv')
    def test_save_as_csv(self, mock_to_csv):

        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c']
        })

        year = 2024
        expected_filename = f"../data/Luftemissionen_{year}.csv"

        save_as_csv(df, year)
        
        mock_to_csv.assert_called_once_with(path_or_buf=expected_filename, sep=";", index=False)

    @patch('pandas.read_csv')
    def test_load(self, mock_read_csv):

        mock_csv_content = """GENESIS-Tabelle: 85111-0001
        Luftemissionen: Deutschland, Jahre (bis 2019),;;;;;;;;
        Luftemissionsart, Produktionsbereiche;;;;;;;;
        Luftemissionsrechnung;;;;;;;;
        Deutschland;;;;;;;;
        Luftemissionen (t);;;;;;;;
        ;;;1995;1996;1997;1998;1999;2000
        Kohlendioxid (CO2);CPA08-01;Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL;16801097;17666353;14959294;15249144;15020915;9751762
        Kohlendioxid (CO2);CPA08-02;Forstwirtschaftl. Erzeugnisse und Dienstleistungen;492779;462774;1246367;473786;458240;411683
        Kohlendioxid (CO2);CPA08-03;Fische und Fischereierz., Aquakulturerz., DL;54261;53700;51894;51826;52134;53113
        Kohlendioxid (CO2);CPA08-05;Kohle;1752124;1874657;1515425;1191846;1059279;1036480
        __________
        � Statistisches Bundesamt (Destatis), 2023
        Stand: 11.08.2023 / 20:48:54"""

        

        mock_df = pd.DataFrame({
            'Luftemissionsart': ['Kohlendioxid (CO2)', 'Kohlendioxid (CO2)', 'Kohlendioxid (CO2)', 'Kohlendioxid (CO2)'],
            'Produktionsbereiche': ['CPA08-01', 'CPA08-02', 'CPA08-03', 'CPA08-05'],
            'Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL': ['16801097', '492779', '54261', '1752124'],
            '1995': ['17666353', '462774', '53700', '1874657'],
            '1996': ['14959294', '1246367', '51894', '1515425'],
            '1997': ['15249144', '473786', '51826', '1191846'],
            '1998': ['15020915', '458240', '52134', '1059279'],
            '1999': ['9751762', '411683', '53113', '1036480'],
            '2000': ['10013800', '321768', '52701', '956993'],
        })

        
        encoding = 'ISO-8859-1'
        data_source = io.StringIO(mock_csv_content)

        mock_read_csv.return_value = mock_df

        result = load(data_source, encoding)
        
        mock_read_csv.assert_called_once_with(
            data_source,
            delimiter=";",
            header=None,
            encoding=encoding,
            skiprows=6,
            skipfooter=3,
            engine='python'
        )
        
        pd.testing.assert_frame_equal(result, mock_df)

    @patch('extract_transform.save_as_csv')
    def test_transform_2019_data(self, mock_save_as_csv):

        data = [
                [None, None, None, 1995, 1996],
                ["Kohlendioxid (CO2)", "CPA08-01", "Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL", 16801097, 17666353],
                ["Kohlendioxid (CO2)", "CPA08-02", "Forstwirtschaftl. Erzeugnisse und Dienstleistungen", 492779, 462774],
                ["Methan (CH4)", "CPA08-01", "Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL", 12548621, 482403],
                ["Methan (CH4)", "CPA08-02", "Forstwirtschaftl. Erzeugnisse und Dienstleistungen", 13214587, 502932]
            ]

        mock_df = pd.DataFrame(data)

        transform_2019_data(mock_df)

        expected_call_1 = (
                pd.DataFrame({
                    'year': [1995, 1995],
                    'economic_sector': ['Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL', 'Forstwirtschaftl. Erzeugnisse und Dienstleistungen'],
                    'Kohlendioxid (CO2)': [16801097, 492779],
                    'Methan (CH4)': [12548621, 13214587]
                }), 1995
            )
        expected_call_2 = (
            pd.DataFrame({
                'year': [1996, 1996],
                'economic_sector': ['Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL', 'Forstwirtschaftl. Erzeugnisse und Dienstleistungen'],
                'Kohlendioxid (CO2)': [17666353, 462774],
                'Methan (CH4)': [482403, 502932]
            }), 1996
        )

        expected_calls = [expected_call_1, expected_call_2]


        for expected_call, actual_call in zip(expected_calls,mock_save_as_csv.call_args_list) :
            temp_df, year = expected_call
            args, kwargs = actual_call

            temp_df = temp_df[['year', 'economic_sector', 'Kohlendioxid (CO2)', 'Methan (CH4)']]
            args[0].columns.name = None
            print(temp_df.columns)
            pd.testing.assert_frame_equal(temp_df, args[0])


if __name__ == '__main__':
    unittest.main()