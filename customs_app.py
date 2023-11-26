import flet as ft
from flet import Row, DataColumn, DataTable, DataRow, DataCell, Column
import datetime
from datetime import date

fechaNacimiento = ""
def main(page: ft.Page):
    page.title = "🔥 Customs Form - By Freddy Alcarazo"
    page.window_width = 1280        # window's width is 200 px
    page.window_height = 720       # window's height is 200 px
    page.window_resizable = True  # window is not resizable
    page.scroll = "always" # TO DO SCROLL BECAUSE OF THE TABLE ITEMS

    # Welcome message - Showing SnackBar
    page.snack_bar = ft.SnackBar(
        ft.Text("Welcome Freddy! - creatorpart@gmail.com", color="white"),
        bgcolor="green",
    )

    page.snack_bar.open = True
    page.update()

    def change_date(e):
        global fechaNacimiento
        print(f"Date picker changed, value is {date_picker.value}")
        fechaNacimiento = date_picker.value

    def date_picker_dismissed(e):
        global fechaNacimiento
        print(f"Date picker dismissed, value is {date_picker.value}")
        fechaNacimiento = date_picker.value

    def saveFormBtn(e):

        print("===================== Guardando datos.. ========================")
        print("Name: "+txtNombres.value)
        print("Last Name: " + txtApellidos.value)
        print("Birth Date: " + str(fechaNacimiento))
        print("Nationality: " + str(nacionalidad_dropdown.value))
        print("Gender: " + str(genero_radiobutton.value))
        print("Address: " + txtDireccion.value)
        print("#Passport: " + txtNumPasaporte.value)

        names = txtNombres.value
        lastNames = txtApellidos.value
        birthDate = str(fechaNacimiento)
        nationality = str(nacionalidad_dropdown.value)
        gender = str(genero_radiobutton.value)
        address = txtDireccion.value
        passportNumber = txtNumPasaporte.value

        # Add Data to the table

        mytable.rows.append(
            DataRow(
                cells=[
                    # THIS FOR ID THE YOU TABLE
                    DataCell(ft.Text(len(mytable.rows))),
                    DataCell(ft.Text(names)),
                    DataCell(ft.Text(lastNames)),
                    DataCell(ft.Text(birthDate)),
                    DataCell(ft.Text(nationality)),
                    DataCell(ft.Text(gender)),
                    DataCell(ft.Text(address)),
                    DataCell(ft.Text(passportNumber)),
                ],
                # IF YOU CLIK THIS ROW THEN RUN YOU FUNCTION
                # THIS SCRIPT IS IF CLICK THEN GET THE ID AND NAME OF ROW
                on_select_changed=lambda e: editIndex(e.control.cells[0].content.value,
                                                      e.control.cells[1].content.value, #names
                                                      e.control.cells[2].content.value, #lastNames
                                                      e.control.cells[3].content.value, #bithDate
                                                      e.control.cells[4].content.value, #nationality
                                                      e.control.cells[5].content.value, #gender
                                                      e.control.cells[6].content.value, #address
                                                      e.control.cells[7].content.value) #passportNum
            )
        )
        # CLEAN FORM INPUTS
        txtNombres.value = ""
        txtApellidos.value = ""
        nacionalidad_dropdown.value = "Seleccionar"
        genero_radiobutton.value = ""
        txtDireccion.value = ""
        txtNumPasaporte.value = ""

        page.update()

    def button_cancel_clicked(e) :
        print("cancelando.")

        txtNombres.value = ""
        txtApellidos.value = ""
        nacionalidad_dropdown.value = "Seleccionar"
        genero_radiobutton.value = " "
        txtDireccion.value = ""
        txtNumPasaporte.value = ""

        page.update()

    """
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    """
    # =============================================== Row 1 elements ================================================

    row_0 = Row(
        controls=[
            ft.Text(value="Customs Form.", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
        ]
    )
    row_1 = Row(
        controls=[
            ft.Text(value="🔴 Fill the form to enter the Peru country:", size=15, color=ft.colors.BLACK)
        ]
    )
    # =============================================== Row 2 elements ================================================

    txtNombres = ft.TextField(label="Names", hint_text="Write you name")
    txtApellidos = ft.TextField(label="Last Name", hint_text="Write your last name")

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
        "Birth Date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

    nacionalidad_dropdown = ft.Dropdown(width=200, label="Nationality",
        options=[
            ft.dropdown.Option("Venezuelan"),
            ft.dropdown.Option("Peruvian"),
            ft.dropdown.Option("Colombian"),
            ft.dropdown.Option("Argentinian"),
            ft.dropdown.Option("Chilean"),
            ft.dropdown.Option("Mexican"),
        ])

    lblGeneros = ft.Text(value="Gender:", color=ft.colors.BLACK)

    # Radio button sexos
    genero_radiobutton = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="female", label="Female"),
        ft.Radio(value="male", label="Male"),
        ft.Radio(value="other", label="Other")]))


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
    txtDireccion = ft.TextField(label="Residence address", hint_text="Residence address", width=610)
    txtNumPasaporte = ft.TextField(label="Passport number", hint_text="Passport Number")

    row_3 = Row(
        controls=[
            txtDireccion,
            txtNumPasaporte
        ]
    )
    # =============================================== Row 4 elements ================================================

    submit_btn = ft.ElevatedButton(text="Register",
                                   on_click=saveFormBtn,
                                   bgcolor=ft.colors.BLUE,
                                   color=ft.colors.WHITE,
                                   icon=ft.icons.SAVE)

    cancelar_btn = ft.ElevatedButton(text="Cancel/Clean",
                                   on_click=button_cancel_clicked,
                                   bgcolor=ft.colors.GREY,
                                   color=ft.colors.WHITE,
                                    icon=ft.icons.CLEAR)

    def removeIndex(e):
        #print("you id is = ", youid.value)
        del mytable.rows[youid.value]

        # THEN SHOW SNACK BAR . THIS OPTIONAL
        page.snack_bar = ft.SnackBar(
            ft.Text(f"Success deleted. Your id  = {youid.value}", color="white"),
            bgcolor="red",
        )
        page.snack_bar.open = True
        page.update()

        # EDIT THEN SAVE YOU DATA

    def editTableAndSave(e):
        # THIS SCRIPT IS SELECT YOU DATA BEFORE AND
        # CHANGE TO NEW DATA FOR UPDATE IN TEXTFIELD

        mytable.rows[youid.value].cells[1].content = ft.Text(txtNombres.value)
        mytable.rows[youid.value].cells[2].content = ft.Text(txtApellidos.value)
        mytable.rows[youid.value].cells[3].content = ft.Text(date_picker.value)
        mytable.rows[youid.value].cells[4].content = ft.Text(nacionalidad_dropdown.value)
        mytable.rows[youid.value].cells[5].content = ft.Text(genero_radiobutton.value)
        mytable.rows[youid.value].cells[6].content = ft.Text(txtDireccion.value)
        mytable.rows[youid.value].cells[7].content = ft.Text(txtNumPasaporte.value)
        page.update()

    # DELETEBUTTON
    deleteButton = ft.ElevatedButton("Delete this",
                                  bgcolor="red",
                                  color="white",
                                  on_click=removeIndex,
                                  icon=ft.icons.DELETE

                                  )

    # EDIT BUTTON
    editbutton = ft.ElevatedButton("Update data",
                                bgcolor="orange",
                                color="white",
                                on_click=editTableAndSave,
                                icon=ft.icons.UPDATE)

    row_4 = Row(
        controls=[
            submit_btn,
            editbutton,
            deleteButton,
            cancelar_btn
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )


    # =============================================== Row 5 DataTable ================================================
    youid = ft.Text("")

    # Create aa empty table
    mytable = DataTable(
        columns=[
            DataColumn(ft.Text("# id")),
            DataColumn(ft.Text("Names")),
            DataColumn(ft.Text("Last Name")),
            DataColumn(ft.Text("Birth Date")),
            DataColumn(ft.Text("Nationality")),
            DataColumn(ft.Text("Gender")),
            DataColumn(ft.Text("Address")),
            DataColumn(ft.Text("# Passport")),
        ],
        # THIS IS YOU ROW OF YOU TABLE
        rows=[]
    )

    # GET ID THE ROW

    def editIndex(e, names, lastNames, bithDate, nationality, gender, address, passport):
        print("you id is = ", e)
        print("you seledted name is = ", names)

        # SET FORM INPUTS OF THE SELECTED ROW
        txtNombres.value = names
        txtApellidos.value = lastNames
        date_picker.value = bithDate
        nacionalidad_dropdown.value = nationality
        genero_radiobutton.value = gender
        txtDireccion.value = address
        txtNumPasaporte.value = passport

        youid.value = int(e)

        #Update the page
        page.update()
        # HIDE THE ADD NEW BUTTON . AND TRUE OF EDIT AND DELETE BUTTON

    row_5 = Row(
        controls=[
            mytable
        ]
    )


    # Add rows the the page
    page.add(row_0, row_1, row_2, row_3, row_4, row_5)
    page.update()


ft.app(target=main)