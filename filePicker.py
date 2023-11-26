import flet as ft

def main(page: ft.Page):
    page.title = "Big CSV Importer - By Freddy Alcarazo"
    page.window_width = 1280        # window's width is 200 px
    page.window_height = 720       # window's height is 200 px
    page.window_resizable = True  # window is not resizable
    page.scroll = "always" # TO DO SCROLL BECAUSE OF THE TABLE ITEMS

    def on_dialog_result(e: ft.FilePickerResultEvent):
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                print(f"File: {f.name}")
                print(f"Path: {f.path}")


    file_picker = ft.FilePicker( on_result = on_dialog_result)
    page.overlay.append(file_picker)
    page.update()



    fp = ft.ElevatedButton("Choose File...",
                           on_click = lambda _: file_picker.pick_files(allow_multiple=False),
                           icon=ft.icons.FOLDER)

    page.add(fp)

ft.app(target=main)

