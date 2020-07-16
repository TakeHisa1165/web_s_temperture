import xlwings as xw


class InputToExcel:
    def __init__(self, dataframe, excel_path):
        path = excel_path
        wb = xw.Book(path)
        self.ws = wb.sheets(1)
        self.dataframe = dataframe
    def input_to_excel(self):
        max_row = self.ws.range(1048576, 1).end("up").row
        self.ws.range(max_row + 1, 1).value = self.dataframe
        delete_row1 = max_row + 1
        delete_row1 = str(delete_row1)
        self.ws.range((delete_row1, 1), (delete_row1, 3)).delete()


