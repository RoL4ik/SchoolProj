import flet as ft
from certifi import contents


def main(page: ft.Page):
    page.title="Telegram pro"
    page.theme_mode=ft.ThemeMode.DARK
    page.window.width=1000
    page.window.height=700
    page.padding=0
    page.spacing=0


    chat_data={
        "Оля": [],
        "Рома": [],
        "Максим": []
    }

    current_chat="Оля"

    all_contacts= [
        ft.ListTile(leading=ft.CircleAvatar(content=ft.Text("O")), title=ft.Text("Оля", weight="bold"), subtitle=ft.Text("Привіт!"), data="Оля"),
        ft.ListTile(leading=ft.CircleAvatar(content=ft.Text("Р")), title=ft.Text("Рома", weight="bold"), subtitle=ft.Text("Як справи?"), data="Рома")
    ]

    chat_history = ft.ListView(expand=True, spacing=10, auto_scroll=True, padding=15, controls=chat_data[current_chat])
    message_input = ft.TextField(hint_text="Enter a message...", expand=True, border_color="transparent")
    contacts_view = ft.ListView(expand=True, controls=all_contacts.copy())

    top_name = ft.Text(current_chat, size=18, weight="bold")
    top_avatar = ft.CircleAvatar(content=ft.Text(current_chat[0]), radius=15)


    sidebar=ft.Container(
        width=300,
        bgcolor="#17212b",
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(ft.Icons.MENU,icon_color="white"),
                        ft.TextField(hint_text="Пошук...", bgcolor="#242f3d",
                            border_color="transparent", height=35,
                            border_radius=15,expand=True,
                        )
                    ]),
                    padding=ft.Padding(5,10,10,10)
                ),
                ft.ListTile(
                    leading=ft.CircleAvatar(content=ft.Text("0")),
                    title=ft.Text("Оля",color="white",weight="bold"),
                    subtitle=ft.Text("Привіт", color="grey")
                ),
                ft.ListTile(
                    leading=ft.CircleAvatar(content=ft.Text("P")),
                    title=ft.Text("Рома", color="white", weight="bold"),
                    subtitle=ft.Text("Привіт, як справи?", color="grey")
                )
            ]
        )
    )
    chat_area = ft.Container(
        expand=True, bgcolor="#0e1621",
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row([
                        ft.CircleAvatar(content=ft.Text("О"), radius=15),
                        ft.Text("Оля", size=18, weight="bold", color="white"),

                        ft.Container(expand=True),

                        ft.IconButton(ft.Icons.SEARCH, icon_color="white"),
                        ft.IconButton(ft.Icons.CALL, icon_color="white"),
                    ]),
                    bgcolor="#17212b", padding=ft.Padding(15, 10, 15, 10)
                ),

                ft.Container(expand=True),

                ft.Container(
                    content=ft.Row([
                        ft.IconButton(ft.Icons.ATTACH_FILE, icon_color="grey"),
                        ft.TextField(hint_text="Напишіть повідомлення...", expand=True, border_color="transparent"),
                        ft.IconButton(ft.Icons.SEND, icon_color="#2b5278")
                    ]),
                    padding=10
                )
            ]
        )
    )
    main_layout=ft.Row(
        controls=[sidebar,chat_area],
        expand=True,
        spacing=0,
    )
    page.add(main_layout)
if __name__=="__main__":
    ft.run(main)
