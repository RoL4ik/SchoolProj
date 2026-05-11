import flet as ft
from certifi import contents


def main(page: ft.Page):
    page.title="Telegram pro"
    page.theme_mode=ft.ThemeMode.DARK
    page.window.width=1000
    page.window.height=700
    page.padding=0
    page.spacing=0
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
    # Оновлюємо chat_area:
    chat_area = ft.Container(
        expand=True, bgcolor="#0e1621",
        content=ft.Column(
            controls=[
                # 1. ВЕРХНЯ ПАНЕЛЬ + Пружина
                ft.Container(
                    content=ft.Row([
                        ft.CircleAvatar(content=ft.Text("О"), radius=15),
                        ft.Text("Оля", size=18, weight="bold", color="white"),

                        ft.Container(expand=True),  # <-- ПРУЖИНА в рядку! Відштовхує іконки

                        ft.IconButton(ft.Icons.SEARCH, icon_color="white"),
                        ft.IconButton(ft.Icons.CALL, icon_color="white"),
                    ]),
                    bgcolor="#17212b", padding=ft.Padding(15, 10, 15, 10)
                ),

                # 2. ПОРОЖНЕЧА ДЛЯ ПОВІДОМЛЕНЬ
                ft.Container(expand=True),  # <-- ПРУЖИНА в колонці!

                # 3. ПОЛЕ ВВОДУ
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
