from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime

class MyClock(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.time_label = Label(font_size = '48sp')
        self.add_widget(self.time_label)

        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        now = datetime.now().strftime('%H:%M:%S')
        self.time_label.text = f'⏰ {now}'

class MainApp(App):
    def build(self):
        return MyClock()

if __name__ == '__main__':
    MainApp().run()