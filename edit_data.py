import pandas as pd
import datetime as dt
import xlwings as xw
import to_excel

class EditData:
    def __init__(self):
        pass
    def edit_data(self, download_path):
        path = download_path + "\\" + "export.csv"

        data = pd.read_csv(path, skiprows=3)
        data_to_list = data.set_index('Date')
        data_to_list
        date_list = list(data_to_list.index)
        set_list = list(set(date_list))
        set_list.sort()

        data["Date"] = data["Date"].str.cat(data["Time"], sep="/")

        df = data.drop("Time", axis=1)
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.set_index("Date")

        for date in set_list:
            date_df = df[date + " 08:30":date + " 08:40"]
            print(date_df)
            te = to_excel.InputToExcel()
            te.input_to_excel(date_df)


        return date_df



if __name__ == '__main__':
    edt = EditData()
    edt.edit_data("D:\\ドキュメント\\temperture_file")


