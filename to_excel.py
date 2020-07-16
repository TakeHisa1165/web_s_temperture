import xlwings as xw


class InputToExcel:
    def __init__(self):
        pass
    def input_to_excel(self, datafarame):
        path = r"D:\ドキュメント\temperture_file\温度記録.xlsx"
        wb = xw.Book(path)
        ws = wb.sheets(1)
        max_row = ws.range(1048576, 1).end("up").row
        print(max_row)
        print(len(datafarame))
        ws.range(max_row + 1, 1).value = datafarame
        delete_row1 = max_row + 1
        delete_row1 = str(delete_row1)
        ws.range((delete_row1, 1), (delete_row1, 3)).delete()


