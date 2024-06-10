from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from datetime import datetime
import calendar

class DayOfWeekApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical')

        day = datetime.today().strftime('%A')
        year = datetime.today().year
        calendar_month = datetime.today().strftime('%B %Y')

        day_label = Label(text=f"Today is {day}", font_size=30)
        year_label = Label(text=f"Current Year: {year}", font_size=22)
        calendar_label = Label(text=f"Calendar: {calendar_month}", font_size=22)

        root_layout.add_widget(day_label)
        root_layout.add_widget(year_label)
        root_layout.add_widget(calendar_label)

        calendar_table = self.create_calendar_table()
        root_layout.add_widget(calendar_table)

        return root_layout

    def create_calendar_table(self):
        calendar_table = GridLayout(cols=7, spacing=5, padding=10, size_hint_y=None, height=400)
        calendar_table.bind(minimum_height=calendar_table.setter('height'))

        day_names = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for day in day_names:
            day_label = Label(text=day, size_hint_y=None, height=40)
            calendar_table.add_widget(day_label)

        today = datetime.today()
        calendar_matrix = calendar.monthcalendar(today.year, today.month)

        for week in calendar_matrix:
            for day in week:
                if day == 0:
                    day_label = Label(text='', size_hint_y=None, height=40)
                else:
                    day_label = Label(text=str(day), size_hint_y=None, height=40)
                calendar_table.add_widget(day_label)

        return calendar_table

if __name__ == '__main__':
    DayOfWeekApp().run()