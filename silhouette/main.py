from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    pass


class GameApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    GameApp().run()