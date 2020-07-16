import subprocess
from selenium import webdriver
import time


class DownLoad:
    def __init__(self):
        pass
    def down_load(self, logger_paht, download_path, driver_path):
        download_path = download_path
        rpc_path = download_path.replace("/", "\\")
        download_path = rpc_path
        # download_dir = r"D:\ドキュメント\temperture_file"
        download_dir = download_path

        print(download_path)
        print(download_dir)
        chop = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : download_dir}
        chop.add_experimental_option("prefs", prefs)
        chop.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(driver_path, chrome_options=chop)
        # driver = webdriver.Chrome(driver_path)
        time.sleep(1)
        driver.get(logger_paht)
        time.sleep(1)
        driver.find_element_by_id("ex").click()
        time.sleep(1)