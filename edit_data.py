import pandas as pd
import datetime as dt
import xlwings as xw
import to_excel
import os
import PySimpleGUI as sg

class EditData:
    def __init__(self):
        pass
    def edit_data(self, download_path):
        """

        :param download_path: ダウンロードフォルダpath
        :return:
        """
        # ダウンロードフォルダのpathの/を\に変更
        path = download_path + "\\" + "export.csv"
        # csvファイルの読み込み
        data = pd.read_csv(path, skiprows=3)
        # 日付のデータのみリストに格納
        data_to_list = data.set_index('Date')
        # 日付リストを集合でユニークリストに変更
        date_list = list(data_to_list.index)
        set_list = list(set(date_list))
        set_list.sort()
        # csv全データのデータフレーム　日付と時間のカラムを結合
        data["Date"] = data["Date"].str.cat(data["Time"], sep="/")
        # 日付と時間を結合したので、時間のみのカラムを削除
        df = data.drop("Time", axis=1)
        # 日付をインデックスに登録
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")

        # 日付リストに入っている日付毎にデータフレームを分割
        # 時間を指定して必要なデータのみを抽出する
        for date in set_list:
            date_df = df[date + " 010:00":date + " 15:00"]
            print(date_df)
            # Excelへ入力
            te = to_excel.InputToExcel(date_df, excel_path=r"D:\ドキュメント\temperture_file\温度記録.xlsx")
            te.input_to_excel()




if __name__ == '__main__':
    edt = EditData()
    edt.edit_data("D:\\ドキュメント\\temperture_file")


