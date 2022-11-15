"""
CP1404 - Dynamic Labels
Estimated time: 60 minutes
Actual time: 45 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each data entries and add them to the GUI."""
        for name in self.name_to_phone:
            # create a label for each data entry, specifying the text and id
            temp_label = Label(text=name)
            temp_label.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # get the name (dictionary key) from the text of Button we clicked on
        name = instance.text
        # update status text
        self.status_text = "{}'s number is {}".format(name, self.name_to_phone[name])

    def clear_all(self):
        """Clear all labels that are children of the 'entries_box' layout widget."""
        self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
