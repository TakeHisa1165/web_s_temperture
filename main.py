"""
A&D AD-5326T を使用した気温記録アプリケーション
"""
import csv
import os
import xlwings as xw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import tkinter.messagebox as tmsg
import sys


file = os.path.isfile("path.csv")
if file:
    with open("path.csv", mode="r", newline="", encoding="UTF-8") as file:
        reader = csv.reader(file)
        for row in reader:
            html = row[0]
            download_dir = row[1]
            excel = row[2]
            driver = row[3]
else:
    import gui
html_file = os.path.isfile(html)
# if html_file:
#     pass
# else:
#     tmsg.showinfo("接続確認", "温度計が接続されていません。\n温度計を接続してください。")
#     sys.exit()

driver = webdriver.Chrome()
driver.get(html)
driver.find_element(By.ID, "ex").click()
time.sleep(2)
driver.quit()

with open(download_dir + "/export.csv", mode="r", newline="", encoding="UTF-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])
        if row[1] == "ID:0001":
            sheet_name = "検査場"
        if row[1] == "ID:0002":
            sheet_name = 2
        break
wb = xw.Book(excel)
ws = wb.sheets[sheet_name]

max_row = ws.range(1000000, 1).end('up').row
start_row = max_row + 1
with open(download_dir + "/export.csv", mode="r", newline="", encoding="UTF-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    header = next(reader)
    header = next(reader)
    header = next(reader)
    # print(reader)
    for row in reader:
        date = row[0]
        time = row[1]
        temp = row[2]
        print(date, time, temp)
        ws.range(start_row, 1).value = date
        ws.range(start_row, 2).value = time

        if 12 <= float(temp) <= 35:
            ws.range(start_row, 3).value = temp
        else:
            ws.range(start_row, 3).value = temp
            ws.range(start_row, 3).color = "e49edd"
        start_row += 1

os.remove(download_dir + "/export.csv")
tmsg.showinfo("完了", "処理が終わりました。\nExcelファイルを確認してください。")
