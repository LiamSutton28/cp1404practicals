"""Dynamic Labels App"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """DynamicLabelApp is a Kivy App for adding dynamic labels from a list."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.strings = ["Liam", "word", "anotherword", "lastword"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for string in self.strings:
            temp_button = Label(text=string)
            self.root.ids.main.add_widget(temp_button)
        return self.root

DynamicLabelApp().run()

