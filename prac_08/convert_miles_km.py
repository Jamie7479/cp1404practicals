"""
Convert miles to km GUI
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.60934


class ConvertMilesKm(App):
    output_string = StringProperty()

    def build(self):
        """Build app"""
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_string = '54.71756'
        return self.root

    def handle_convert(self):
        """Convert miles to km and change output based on text input"""
        try:
            self.output_string = str(float(self.root.ids.user_input.text) * CONVERSION_FACTOR)
        except ValueError:
            self.output_string = '0.0'

    def handle_increment(self, increment):
        """Increment text input"""
        try:
            self.root.ids.user_input.text = str(int(self.root.ids.user_input.text) + increment)
        except ValueError:
            self.root.ids.user_input.text = '0'
        self.handle_convert()


ConvertMilesKm().run()
