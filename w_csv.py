import csv
import os
import PySimpleGUI as sg

class Write_csv:
    def __init__(self):
        pass

    def write_csv(self, path_dict):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        with open('path.csv', 'w', newline='') as csvfile:
            fieldnames = ["logger_path", "download_path", "driver_path", "excel_path"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(path_dict)
            sg.popup_ok('初期設定が完了しました。\nもう一度ソフトを立ち上げてください')
