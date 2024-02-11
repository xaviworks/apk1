from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class xavi(App):

    def calculate_wpa(self, instance):
        total_score = 0
        total_units = 0
        for subject in self.subjects:
            try:
                score = float(self.text_inputs[subject].text)
                if 0 <= score <= 100:
                    total_score += score * self.units[subject]
                    total_units += self.units[subject]
                else:
                    raise ValueError("Grade must be between 0 and 100")
            except ValueError as e:
                self.total_label.text = str(e)
                return
                
        if total_units != 0:
            wpa = total_score / total_units
            self.total_label.text = f'Weighted GPA: {wpa:.2f}'
        else:
            self.total_label.text = 'Please input grades for all subjects'

    def build(self):
        self.subjects = [
            "GE 12",
            "GE 3",
            "IT 2",
            "IT 204",
            "IT 205",
            "IT 206",
            "PD 4",
            "PE 4"
        ]
        self.units = {
            "GE 12": 3,
            "GE 3": 2,
            "IT 2": 4,
            "IT 204": 3,
            "IT 205": 3,
            "IT 206": 2,
            "PD 4": 3,
            "PE 4": 4
        }
        self.text_inputs = {}

        background = Image(source='ayti.png', allow_stretch=True, keep_ratio=False)

        layout = GridLayout(cols=3, spacing=dp(10), padding=dp(20), size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        for subject in self.subjects:
            layout.add_widget(Label(text=subject, color=get_color_from_hex('#FFFFFF'), font_size=dp(14), size_hint_y=None, height=dp(40)))
            self.text_inputs[subject] = TextInput(multiline=False, size_hint=(None, None), size=(dp(120), dp(40)), input_type='number')
            layout.add_widget(self.text_inputs[subject])

            spinner = Spinner(text='1', values=('1', '2', '3', '4', '5'), size_hint=(None, None), size=(dp(120), dp(40)))
            layout.add_widget(spinner)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        calculate_button = Button(text="Compute WPA", background_color=get_color_from_hex('#00BFFF'), size_hint=(None, None), size=(dp(200), dp(50)), font_size=dp(16))
        calculate_button.bind(on_press=self.calculate_wpa)
        calculate_button.pos_hint = {'center_x': 0.5}

        total_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))
        total_layout.add_widget(background)  # Add background image first
        total_layout.add_widget(scroll_view)
        total_layout.add_widget(calculate_button)
        total_layout.add_widget(Label(text='', bold=True, font_size=dp(20), size_hint_y=None, height=dp(40), color=get_color_from_hex('#00BFFF')))

        return total_layout

if __name__ == '__main__':
    xavi().run()
