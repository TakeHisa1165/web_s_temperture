import csv
import flet as ft


def main(page: ft.Page):
    # 温度計ファイル選択のコールバック関数
    def pick_temperature_file_result(e: ft.FilePickerResultEvent):
        print(e.path)
        if e.files:
            temperature_file_path.value = e.files[0].path
            temperature_file_path.update()

    # CSVファイル選択のコールバック関数
    def pick_csv_file_result(e: ft.FilePickerResultEvent):
        if e:
            csv_file_paths.value = e.path
            csv_file_paths.update()

    # Excelファイル選択のコールバック関数
    def pick_excel_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            excel_file_path.value = e.files[0].path
            excel_file_path.update()

    # Chrome Driverファイル選択のコールバック関数
    def pick_driver_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            driver_path.value = e.files[0].path
            driver_path.update()

    # CSVに登録する処理
    def regist_to_csv(self):
        temperature = temperature_file_path.value
        csv_path = csv_file_paths.value
        excel_path = excel_file_path.value
        driver_path_val = driver_path.value
        with open("path.csv", mode="w", newline="", encoding="UTF-8") as f:
            writer = csv.writer(f)
            writer.writerow([temperature, csv_path, excel_path, driver_path_val])

    # ファイルピッカーのインスタンスを作成
    pick_temperature_file_dialog = ft.FilePicker(on_result=pick_temperature_file_result)
    pick_csv_file_dialog = ft.FilePicker(on_result=pick_csv_file_result)
    pick_excel_file_dialog = ft.FilePicker(on_result=pick_excel_file_result)
    pick_driver_file_dialog = ft.FilePicker(on_result=pick_driver_file_result)

    # ファイルパス表示用のテキストコンポーネントを作成
    temperature_file_path = ft.TextField(read_only=True, key="temperature_file_path")
    csv_file_paths = ft.TextField(read_only=True, key="csv_file_paths")
    excel_file_path = ft.TextField(read_only=True, key="excel_file_path")
    driver_path = ft.TextField(read_only=True, key="driver_path")

    # ページにファイルピッカーを追加
    page.overlay.extend([pick_temperature_file_dialog, pick_csv_file_dialog, pick_excel_file_dialog, pick_driver_file_dialog])

    # ページにUIコンポーネントを追加
    page.add(
        ft.Row(
            [
                ft.Text("Htmlを選択してください"),
                ft.ElevatedButton(
                    "Html",
                    icon=ft.icons.FILE_OPEN,
                    on_click=lambda _: pick_temperature_file_dialog.pick_files(),
                ),
                temperature_file_path,
            ]
        ),
        ft.Row(
            [
                ft.Text("ダウンロードフォルダを選択してください"),
                ft.ElevatedButton(
                    "フォルダ",
                    icon=ft.icons.FILE_OPEN,
                    on_click=lambda _: pick_csv_file_dialog.get_directory_path(),
                ),
                csv_file_paths,
            ]
        ),
        ft.Row(
            [
                ft.Text("書き出すExcelファイルを選択してください。"),
                ft.ElevatedButton(
                    "Excel",
                    icon=ft.icons.FILE_OPEN,
                    on_click=lambda _: pick_excel_file_dialog.pick_files(allow_multiple=True),
                ),
                excel_file_path,
            ]
        ),
        ft.Row(
            [
                ft.Text("Chrome Driverのファイルを選択してください"),
                ft.ElevatedButton(
                    "Chrome Driver",
                    icon=ft.icons.FILE_OPEN,
                    on_click=lambda _: pick_driver_file_dialog.pick_files(allow_multiple=True),
                ),
                driver_path,
            ]
        ),
    )

    # 登録ボタンを追加
    page.add(ft.ElevatedButton(text="登録", on_click=regist_to_csv))


ft.app(target=main)
