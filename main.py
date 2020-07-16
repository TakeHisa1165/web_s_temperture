import r_csv
import w_csv
import gui
import download_file
import edit_data
import to_excel


rcsv = r_csv.Read_csv()
logger_path, download_path, driver_path = rcsv.read_csv()

dlf = download_file.DownLoad()
dlf.down_load(logger_paht=logger_path, download_path=download_path, driver_path=driver_path)

edt = edit_data.EditData()
data_frame = edt.edit_data(download_path=download_path)

te = to_excel.InputToExcel()
te.input_to_excel(data_frame)


