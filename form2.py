import flet as ft
from flet import Row
import datetime
from datetime import date

fechaNacimiento = ""
def main(page: ft.Page):
    page.title = "🔥 Formulario 2"
    page.window_width = 1280        # window's width is 200 px
    page.window_height = 720       # window's height is 200 px
    page.window_resizable = True  # window is not resizable



    def change_date(e):
        global fechaNacimiento
        print(f"Date picker changed, value is {date_picker.value}")
        fechaNacimiento = date_picker.value

    def date_picker_dismissed(e):
        global fechaNacimiento
        print(f"Date picker dismissed, value is {date_picker.value}")
        fechaNacimiento = date_picker.value

    def button_clicked(e):

        print("===================== Guardando datos.. ========================")
        print("Nombres: "+txtNombres.value)
        print("Apellidos: " + txtApellidos.value)
        print("Fecha. Nacimiento: " + str(fechaNacimiento))
        print("Nacionalidad: " + str(nacionalidad_dropdown.value))
        print("Género: " + str(genero_radiobutton.value))
        print("Dirección: " + txtDireccion.value)
        print("#Pasaporte: " + txtNumPasaporte.value)

        page.update()

    def button_cancel_clicked(e) :
        print("cancelando.")
        page.update()

    """
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    """
    # =============================================== Row 1 elements ================================================

    row_0 = Row(
        controls=[
            ft.Text(value="Formulario de Inscripción - Aduanas", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
        ]
    )
    row_1 = Row(
        controls=[
            ft.Text(value="🔴 Rellene los siguiente campos para registrar ingreso al pais:", size=15, color=ft.colors.BLACK)
        ]
    )
    # =============================================== Row 2 elements ================================================

    txtNombres = ft.TextField(label="Nombres", hint_text="Ingresa tu nombre")
    txtApellidos = ft.TextField(label="Apellidos", hint_text="Ingresa tus Apellidos")

    fecha = date.today()
    year = fecha.year
    month = fecha.month
    day = fecha.day

    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(1950, 1, 1),
        last_date=datetime.datetime(year, month, day),
    )
    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        "Fecha de Nacimiento",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

    nacionalidad_dropdown = ft.Dropdown(width=200, label="Nacionalidad",
        options=[
            ft.dropdown.Option("Venezolano"),
            ft.dropdown.Option("Colombiano"),
            ft.dropdown.Option("Argentino"),
            ft.dropdown.Option("Chileno"),
            ft.dropdown.Option("Mexicano"),
        ])

    lblGeneros = ft.Text(value="Género:", color=ft.colors.BLACK)

    # Radio button sexos
    genero_radiobutton = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="femenino", label="Femenino"),
        ft.Radio(value="masculino", label="Masculino"),
        ft.Radio(value="otro", label="Otro")]))


    row_2 = Row(
        controls=[
            txtNombres,
            txtApellidos,
            date_button,
            nacionalidad_dropdown,
            lblGeneros,
            genero_radiobutton

        ]
    )

    # =============================================== Row 3 elements ================================================
    txtDireccion = ft.TextField(label="Dirección de permanencia", hint_text="Dirección donde va a permanecer", width=610)
    txtNumPasaporte = ft.TextField(label="Número de pasaporte", hint_text="Número de pasaporte")

    row_3 = Row(
        controls=[
            txtDireccion,
            txtNumPasaporte
        ]
    )
    # =============================================== Row 4 elements ================================================

    submit_btn = ft.ElevatedButton(text="Registrar",
                                   on_click=button_clicked,
                                   bgcolor=ft.colors.BLUE,
                                   color=ft.colors.WHITE)

    cancelar_btn = ft.ElevatedButton(text="Cancelar",
                                   on_click=button_cancel_clicked,
                                   bgcolor=ft.colors.GREY,
                                   color=ft.colors.WHITE)

    row_4 = Row(
        controls=[
           submit_btn,
            cancelar_btn
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    """
    t = ft.Text()
    tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
    tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, b, t)
    """
    page.add(row_0, row_1, row_2, row_3, row_4)
    page.update()
ft.app(target=main)