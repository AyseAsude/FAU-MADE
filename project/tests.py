import pandas as pd
import unittest
import io
import os
import numpy as np
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
        print("Expecting to receive 404...")
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

    def test_load(self):

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

        

        mock_df = pd.DataFrame([
            [np.nan, np.nan, np.nan, 1995, 1996, 1997,1998,1999,2000],
            ["Kohlendioxid (CO2)", "CPA08-01", "Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL", 16801097, 17666353, 14959294, 15249144, 15020915, 9751762],
            ["Kohlendioxid (CO2)", "CPA08-02", "Forstwirtschaftl. Erzeugnisse und Dienstleistungen", 492779, 462774, 1246367, 473786, 458240, 411683],
            ["Kohlendioxid (CO2)", "CPA08-03", "Fische und Fischereierz., Aquakulturerz., DL", 54261, 53700, 51894, 51826, 52134, 53113],
            ["Kohlendioxid (CO2)", "CPA08-05", "Kohle", 1752124, 1874657, 1515425, 1191846, 1059279, 1036480],
        ])
        
        encoding = 'utf-8'
        data_source = io.StringIO(mock_csv_content)

        result = load(data_source, encoding)

        pd.testing.assert_frame_equal(result, mock_df)

    @patch('extract_transform.save_as_csv')
    def test_transform_2019_data(self, mock_save_as_csv):

        data = [
                [np.nan, np.nan, np.nan, 1995, 1996],
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
            pd.testing.assert_frame_equal(temp_df, args[0])

    @patch('requests.get')
    def test_integration(self, mock_get):

        mock_response = Response()
        mock_response.status_code = 200
        content_mock = PropertyMock(return_value=b'some content')
        type(mock_response).content = content_mock
        mock_get.return_value = mock_response

        # dummy url, just for the signature
        url = "https://google.com"

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

        mock_df = pd.DataFrame([[None, None, None, 1995, 1996, 1997, 1998, 1999, 2000],
            ["Kohlendioxid (CO2)", "CPA08-01", "Erz.d. Landwirtschaft u. Jagd sowie damit verb. DL", 16801097, 17666353, 14959294, 15249144, 15020915, 9751762],
            ["Kohlendioxid (CO2)", "CPA08-02", "Forstwirtschaftl. Erzeugnisse und Dienstleistungen", 492779, 462774, 1246367, 473786, 458240, 411683],
            ["Kohlendioxid (CO2)", "CPA08-03", "Fische und Fischereierz., Aquakulturerz., DL", 54261, 53700, 51894, 51826, 52134, 53113],
            ["Kohlendioxid (CO2)", "CPA08-05", "Kohle", 1752124, 1874657, 1515425, 1191846, 1059279, 1036480],
        ])

        data_source = io.StringIO(mock_csv_content)

        # step 1: check encoding
        encoding = check_and_get_encoding(url)
        self.assertIsInstance(encoding, str)

        # step 2: load data
        result = load(data_source, encoding)
        pd.testing.assert_frame_equal(result, mock_df)
      
        # step 3: apply transform
        save_locations = transform_2019_data(result)
        mock_save_locations = ['../data/Luftemissionen_1995.csv', '../data/Luftemissionen_1996.csv', \
                               '../data/Luftemissionen_1997.csv', '../data/Luftemissionen_1998.csv', \
                                '../data/Luftemissionen_1999.csv', '../data/Luftemissionen_2000.csv']
        
        self.assertEqual(save_locations, mock_save_locations)
        
        for file_path in mock_save_locations:
            assert os.path.isfile(file_path)

if __name__ == '__main__':
    unittest.main()