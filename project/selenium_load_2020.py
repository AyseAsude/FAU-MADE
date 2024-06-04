from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


# returns the latest created file in the given directory
def get_latest_file(directory):
    files = os.listdir(directory)
    paths = [os.path.join(directory, basename) for basename in files]
    return max(paths, key=os.path.getctime)

# options for the driver
options = Options()
# headless arg make it run without a GUI
options.add_argument('--headless')
# window size is set because some buttons do not appear in certain sizes
options.add_argument("--window-size=2560,1440")

# constructing the absolute path for download directory, relative paths didn't work
script_directory = os.path.dirname(os.path.abspath(__file__))
download_directory = os.path.join(script_directory, '..', 'data')
download_directory = os.path.normpath(download_directory)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# specifying the download directory
prefs = {"download.default_directory": download_directory}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

URL = "https://www-genesis.destatis.de/datenbank/beta/statistic/85111/table/85111-0002/table-toolbar#filter=eyJoaWRlRW1wdHlDb2xzIjpmYWxzZSwiaGlkZUVtcHR5Um93cyI6ZmFsc2UsImNhcHRpb24iOlt7ImlkIjoiczEuODUxMTEiLCJ2YWx1ZXNJZHMiOlsiODUxMTEiXSwiY2hpbGRyZW4iOlt7ImlkIjoidjEuRElOU0ciLCJ2YWx1ZXNJZHMiOlsiREciXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJzaG93VmFyaWFibGUiOmZhbHNlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJzb3J0IjoiQ29kZUFzYyIsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoidjEiLCJibG9ja0lkIjoiMC4wIn1dLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6InMxIiwiYmxvY2tJZCI6IjAifSx7ImlkIjoidjEuRElOU0ciLCJ2YWx1ZXNJZHMiOlsiREciXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJzaG93VmFyaWFibGUiOmZhbHNlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJzb3J0IjoiQ29kZUFzYyIsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoidjEiLCJibG9ja0lkIjoiMC4wIn1dLCJyb3dIZWFkZXIiOlt7ImlkIjoidjIuSkFIUiIsInZhbHVlc0lkcyI6WyIyMDIwIl0sImNoaWxkcmVuIjpbeyJpZCI6ImMxLkVNUzAwMSIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOlt7ImlkIjoidjQuV1owOFUxIiwidmFsdWVzSWRzIjpbIldaMDgtQSIsIldaMDgtMDEiLCJXWjA4LTAyIiwiV1owOC0wMyIsIldaMDgtQiIsIldaMDgtMDUiLCJXWjA4LTA2IiwiV1owOC0wNy0wMSIsIldaMDgtQyIsIldaMDgtMTAtMDMiLCJXWjA4LTEzLTA0IiwiV1owOC0xNiIsIldaMDgtMTciLCJXWjA4LTE4IiwiV1owOC0xOSIsIldaMDgtMTkxIiwiV1owOC0xOTIiLCJXWjA4LTIwIiwiV1owOC0yMSIsIldaMDgtMjIiLCJXWjA4LTIzIiwiV1owOC0yMzEiLCJXWjA4LTIzMi0wMiIsIldaMDgtMjQiLCJXWjA4LTI0MS0wMiIsIldaMDgtMjQ0IiwiV1owOC0yNDUiLCJXWjA4LTI1IiwiV1owOC0yNiIsIldaMDgtMjciLCJXWjA4LTI4IiwiV1owOC0yOSIsIldaMDgtMzAiLCJXWjA4LTMxLTAyIiwiV1owOC0zMyIsIldaMDgtRCIsIldaMDgtMzUxLTAxIiwiV1owOC0zNTIiLCJXWjA4LUUiLCJXWjA4LTM2IiwiV1owOC0zNy0wMSIsIldaMDgtMzciLCJXWjA4LTM4LTAyIiwiV1owOC1GIiwiV1owOC00MS0wMSIsIldaMDgtNDMiLCJXWjA4LUciLCJXWjA4LTQ1IiwiV1owOC00NiIsIldaMDgtNDciLCJXWjA4LUgiLCJXWjA4LTQ5MS0wMSIsIldaMDgtNDkzLTAxIiwiV1owOC01MCIsIldaMDgtNTEiLCJXWjA4LTUyIiwiV1owOC01MyIsIldaMDgtSSIsIldaMDgtSiIsIldaMDgtSyIsIldaMDgtTCIsIldaMDgtTSIsIldaMDgtTiIsIldaMDgtTyIsIldaMDgtUCIsIldaMDgtUSIsIldaMDgtUi1UIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwic2hvd1ZhcmlhYmxlIjp0cnVlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJJRCIsIkxBQkVMIl0sImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoidjQiLCJibG9ja0lkIjoiMC4wLjAifV0sInNob3dBc0ludGVybGluZSI6ZmFsc2UsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoiYzEiLCJibG9ja0lkIjoiMC4wIn0seyJpZCI6ImMyLkVNUzAxMCIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImMyIiwiYmxvY2tJZCI6IjAuMSJ9LHsiaWQiOiJjMy5FTVMwMTEiLCJ2YWx1ZXNJZHMiOlsiUU1VIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwiaXNIaWRkZW4iOmZhbHNlLCJibG9ja0NvZGUiOiJjMyIsImJsb2NrSWQiOiIwLjIifSx7ImlkIjoiYzQuRU1TMDEyIiwidmFsdWVzSWRzIjpbIlFNVSJdLCJjaGlsZHJlbiI6W10sInNob3dBc0ludGVybGluZSI6ZmFsc2UsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoiYzQiLCJibG9ja0lkIjoiMC4zIn0seyJpZCI6ImM1LkVNUzAxMyIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImM1IiwiYmxvY2tJZCI6IjAuNCJ9LHsiaWQiOiJjNi5FTVMwMTQiLCJ2YWx1ZXNJZHMiOlsiUU1VIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwiaXNIaWRkZW4iOmZhbHNlLCJibG9ja0NvZGUiOiJjNiIsImJsb2NrSWQiOiIwLjUifSx7ImlkIjoiYzcuRU1TMDE1IiwidmFsdWVzSWRzIjpbIlFNVSJdLCJjaGlsZHJlbiI6W10sInNob3dBc0ludGVybGluZSI6ZmFsc2UsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoiYzciLCJibG9ja0lkIjoiMC42In0seyJpZCI6ImM4LkVNUzAxNiIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImM4IiwiYmxvY2tJZCI6IjAuNyJ9LHsiaWQiOiJjOS5FTVMwMTciLCJ2YWx1ZXNJZHMiOlsiUU1VIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwiaXNIaWRkZW4iOmZhbHNlLCJibG9ja0NvZGUiOiJjOSIsImJsb2NrSWQiOiIwLjgifSx7ImlkIjoiYzEwLkVNUzAxOCIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImMxMCIsImJsb2NrSWQiOiIwLjkifV0sInNob3dBc0ludGVybGluZSI6dHJ1ZSwic2hvd1ZhcmlhYmxlIjp0cnVlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6InYyIiwiYmxvY2tJZCI6IjAifV0sImNvbHVtbkhlYWRlciI6W3siaWQiOiJ2My5VTVdFTTIiLCJ2YWx1ZXNJZHMiOlsiRU1JUy1DTzIiLCJFTUlTLUNINCIsIkVNSVMtTjJPIiwiRU1JUy1OSDMiLCJFTUlTLVNPWCIsIkVNSVMtTk9YIiwiRU1JUy1OTVZPQyIsIkVNSVMtRlMxMCIsIkVNSVMtRlMyLTUiLCJFTUlTLUNPIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwic2hvd1ZhcmlhYmxlIjp0cnVlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6InYzIiwiYmxvY2tJZCI6IjAifV0sImlzVHJhbnNwb3NlZCI6ZmFsc2V9"

try:
    driver.get(URL)
    print(driver.title)

    close_modal = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "maintenance-modal-button-cancel"))
    )

    close_modal.click()
    print("closed modal")

except Exception as e:
    print("Exception occured while closing the pop up:", e)

try:
    print("opening download modal...")
    open_download_modal = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "statistic-table-toolbar-button-download"))
    )
    open_download_modal.click()
    print("opened download modal")

    print("trying to download...")
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='CSV Format']"))
    )

    download_button.click()
    print("Download initiated. Please wait for the file to download.")

    # giving some time for downloading and creating the file
    time.sleep(4)

    print("File should be downloaded now.")

    # rename the downloaded file so that it is consistent with other files
    latest_file = get_latest_file(download_directory)
    new_file_name = os.path.join(download_directory, "Luftemissionen_2020_not_transformed.csv")
    # remove if the file already exists because we want to store the newest
    if os.path.isfile(new_file_name):
        os.remove(new_file_name)
    os.rename(latest_file, new_file_name)

except Exception as e:
    print("Exception occured:", e)

# close the browser
driver.quit()


