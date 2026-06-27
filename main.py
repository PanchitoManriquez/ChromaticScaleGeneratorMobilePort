from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
import parselmouth
import os
from os.path import exists

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10
    Label:
        text: 'Chromatic Scale Generator'
        font_size: 25
    BoxLayout:
        Label: text: 'Sample path:'
        TextInput:
            id: dir_path
            text: '/content/samples'
            multiline: False
    BoxLayout:
        Label: text: 'Starting note:'
        Spinner:
            id: note_choice
            values: ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
            text: 'C'
    BoxLayout:
        Label: text: 'Range:'
        TextInput:
            id: range_input
            text: '24'
    CheckBox:
        id: pitched_check
        active: True
    Button:
        text: 'Generate Chromatic'
        on_press: app.generate_chromatic()
'''

class ChromaticApp(App):
    def build(self):
        return Builder.load_string(KV)

    def generate_chromatic(self):
        sample_path = self.root.ids.dir_path.text
        # La lógica de parselmouth sigue siendo igual
        # Asegúrate de que las rutas sean correctas en Android/Colab
        print("Generando...")

if __name__ == '__main__':
    ChromaticApp().run()
