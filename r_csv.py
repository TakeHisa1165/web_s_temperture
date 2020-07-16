import csv
import os
import gui
import PySimpleGUI as sg


class Read_csv:
    def __init__(self):
        pass

    def read_csv(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        try:
            with open('path.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    logger_path = row["logger_path"]
                    download_path = row["download_path"]
                    driver_path = row["driver_path"]
                    return logger_path, download_path, driver_path
        except FileNotFoundError:
            sg.popup_ok('初期設定が必要です。\nラベルチェックファイルと入出庫ファイルを選んでください')
            gui.Select_File()


if __name__ == "__main__":
    a = Read_csv()
    a.read_csv()