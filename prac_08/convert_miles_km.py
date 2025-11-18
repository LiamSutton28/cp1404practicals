"""Convert miles to kilometres Program"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION = 1.609


class ConvertMilesToKmApp(App):
    """ConvertMilesToKmApp is a Kivy App for converting miles to km."""

    km_output = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.km_output = "Type in the field & press Enter"
        return self.root

    def handle_update(self):
        """Convert from miles to km and update output."""
        try:
            mile_number = float(self.root.ids.user_input.text)
            km_number = CONVERSION * mile_number
            self.km_output = str(km_number)
        except ValueError:
            self.km_output = "0.0"

    def handle_increment(self,user_input, increment):
        """Handle Up and Down increments."""
        try:
            mile_number = float(user_input) + increment
        except ValueError:
            mile_number = 0.0 + increment
        self.root.ids.user_input.text = str(mile_number)
        self.handle_update()

ConvertMilesToKmApp().run()
