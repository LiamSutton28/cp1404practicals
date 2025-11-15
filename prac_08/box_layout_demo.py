from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayout is a Kivy App for getting use to kivy apps."""
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root


    def handle_greet(self):
        """Handle the greeting text in the output label."""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


    def handle_clear(self):
        """Handles the reset of the App by clearing input and outputs."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
