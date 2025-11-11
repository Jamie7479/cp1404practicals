"""
Convert miles to km GUI
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


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
        self.output_string = str(float(self.root.ids.user_input.text) * 1.60934)

    def handle_increment(self, increment):
        """Increment text input"""
        self.root.ids.user_input.text = str(float(self.root.ids.user_input.text) + increment)


ConvertMilesKm().run()
