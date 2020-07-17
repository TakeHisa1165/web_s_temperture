"""
温度データ記録用、メイン制御プログラム
"""

import r_csv
import w_csv
import gui
import download_file
import edit_data
import to_excel

# path.csvを読み込んで、必要な絶対pathを取得
# r_csvのインスタンス
rcsv = r_csv.Read_csv()
logger_path, download_path, driver_path, excel_path = rcsv.read_csv()

# seleniumを使用してブラウザで表示されるデータのCSVを保存
dlf = download_file.DownLoad()
dlf.down_load(logger_paht=logger_path, download_path=download_path, driver_path=driver_path)

# ダウンロードしたcsvファイルを編集
edt = edit_data.EditData()
data_frame = edt.edit_data(download_path=download_path)



