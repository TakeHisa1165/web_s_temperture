from selenium import webdriver
import time
import sys
import os
import PySimpleGUI as sg


class DownLoad:
    def __init__(self):
        pass
    def down_load(self, logger_paht, download_path, driver_path):
        """

        :param logger_paht: 温度データのhtmlファイルpath
        :param download_path: ダウンロードしたCSVの保存先path
        :param driver_path: chromedriverのpath
        :return: なし
        """
        download_path = download_path
        rpc_path = download_path.replace("/", "\\")
        download_path = rpc_path
        download_dir = download_path
        chop = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : download_dir}
        chop.add_experimental_option("prefs", prefs)
        chop.add_argument('--ignore-certificate-errors')
        # htmlファイルの有無を確認
        if os.path.isfile(logger_paht):
            pass
        else:
            sg.popup_error('データロガーを認識していません。\n接続状態を再確認してください')
            sys.exit()
        driver = webdriver.Chrome(driver_path, chrome_options=chop)
        time.sleep(1)
        driver.get(logger_paht)
        time.sleep(1)
        driver.find_element_by_id("ex").click()
        time.sleep(1)