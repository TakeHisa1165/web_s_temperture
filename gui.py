import PySimpleGUI as sg
import w_csv


class Select_File:
    def __init__(self):
        self.path_dict = self.select_file()

    def select_file(self):

        sg.theme('SystemDefault')

        layout = [
            [sg.Text('データロガー内の Records.html を選択してください', size=(50, 1), font=('メイリオ', 14))],
            [sg.InputText(font=('メイリオ', 14)), sg.FilesBrowse('開く', key='File1', font=('メイリオ', 14))],
            [sg.Text('CSVファイルのダウンロード先フォルダを選んでください', size=(50, 1), font=('メイリオ', 14))],
            [sg.InputText(font=('メイリオ', 14)), sg.FolderBrowse('開く', font=('メイリオ', 14))],
            [sg.Text('chromedriverの場所を指定してください', size=(50, 1), font=('メイリオ', 14))],
            [sg.InputText(font=('メイリオ', 14)), sg.FilesBrowse('開く', key='File1', font=('メイリオ', 14))],
            [sg.Text('記録用Excelファイルを選択してください', size=(50, 1), font=('メイリオ', 14))],
            [sg.InputText(font=('メイリオ', 14)), sg.FolderBrowse('開く', key='File1', font=('メイリオ', 14))],
            [sg.Submit(button_text='設定', font=('メイリオ', 14)), sg.Submit(button_text="閉じる", font=('メイリオ', 14))],
        ]

        # セクション 2 - ウィンドウの生成z
        window = sg.Window('ファイル選択', layout)

        # セクション 3 - イベントループ
        while True:
            event, values = window.read()

            if event is None:
                print('exit')
                break

            if event == '設定':
                path_dict = {}
                logger_path = values[0]
                path_dict["logger_path"] = logger_path
                download_path = values[1]
                path_dict["download_path"] = download_path
                driver_path = values[2]
                path_dict["driver_path"] = driver_path
                excel_path = values[3]
                path_dict["excel_path"] = excel_path
                csv = w_csv.Write_csv()
                csv.write_csv(path_dict=path_dict)

                return path_dict

            if event == '閉じる':
                break

        #  セクション 4 - ウィンドウの破棄と終了
        window.close()


if __name__ == "__main__":
    Select_File()
