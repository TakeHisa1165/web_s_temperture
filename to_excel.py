import xlwings as xw


class InputToExcel:
    def __init__(self, dataframe, excel_path):
        path = excel_path
        wb = xw.Book(path)
        self.ws = wb.sheets(1)
        self.dataframe = dataframe

        col = 1
        for i in range(1, 9, 2):
            data_list = self.ws.range((2, i), (13, i)).value
            for data in data_list:
                if data is None:
                    select_col = i
                    break
                else:
                    pass
            else:
                col += 1
                continue
            break
        self.input_to_excel(select_col=select_col)

    def input_to_excel(self, select_col):
        max_row = self.ws.range(1048576, select_col).end("up").row
        self.ws.range(max_row + 1, select_col).value = self.dataframe
        delete_row1 = max_row + 1
        delete_row1 = str(delete_row1)
        self.ws.range((delete_row1, select_col), (delete_row1, select_col + 2)).clear_contents()
        len_df = len(self.dataframe)
        self.ws.range(max_row + 1, select_col).value = self.ws.range((max_row + 2, select_col), (max_row + len(self.dataframe) + 2, select_col+1)).value
        data_max_row = self.ws.range(1048576, select_col).end('up').row
        # self.ws.range((data_max_row, select_col), (data_max_row, select_col + 1)).clear_contents()



