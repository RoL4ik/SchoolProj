import flet as ft
from flet.controls import border_radius
from flet.controls.material import button


def main(page: ft.Page):
    def button_clicked():
        print("clicked")
        page.add(ft.Text(value="Button clicked"))
    title = ft.Text(value="Моя перша программа", size=30)
    btn = ft.Button(content=ft.Text(value="start"), on_click=button_clicked)
    row1=ft.Row(
        controls=[
            ft.Card(
                shape=ft.ContinuousRectangleBorder(radius=10),
                content=ft.Container(
                    padding=5,
                    border_radius=ft.border_radius.all(5),
                    bgcolor=ft.Colors.AMBER_100,
                    content=ft.Text(f"Control {i}"),
                ),
            )
            for i in range(1,6)
        ],
    )
    radio = ft.RadioGroup(
        content=ft.Row(
            controls=[ft.Radio(label=f"{i}") for i in range(1, 4)],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(title, btn)
    page.add(row1)
    page.add(radio)


    pass
ft.run(main)
