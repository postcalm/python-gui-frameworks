from dataclasses import dataclass
import flet as ft


@dataclass
class User:
    login: str = None
    password: str = None


class App(ft.Container):
    user = User()

    def __init__(self):
        super().__init__()

        self.login = ft.TextField(label="Login", hint_text="Enter your login")
        self.password = ft.TextField(label="Password", hint_text="Enter your password")
        self.button = ft.TextButton(icon=ft.icons.LOGIN, on_click=self.button_clicked)
        self.dlg = ft.AlertDialog(title=ft.Text("Successful"))
        self.width = 750
        self.height = 490
        self.bgcolor = ft.colors.GREY_200
        self.border_radius = ft.border_radius.all(20)
        self.padding = 10
        self.content = ft.Column([
            ft.Row([self.login], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.password], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.button], alignment=ft.MainAxisAlignment.CENTER)
        ],
            alignment=ft.MainAxisAlignment.CENTER
        )

    def button_clicked(self, e: ft.ControlEvent):
        if self.login.value and self.password.value:
            e.control.page.overlay.append(self.dlg)
            self.dlg.open = True
            e.control.page.update()


def main(page: ft.Page):
    page.title = "App"
    page.window.width = 750
    page.window.height = 550
    app = App()
    page.add(app)


ft.app(main)
