from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

"""
Alvin Yeonata

https://github.com/alvinyeonata/CP1404_assignment2
"""


class Assignment2(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super (Assignment2, self).__init__(**kwargs)

        self.Assignment2 = {"Rusty Bucket": "40L bucket - quite rusty", "Golf Cart": "Tesla powered 250 turbo,195.0", "Thermomix": "TM-31,25.5"}

    def build(self):

        self.title = "Equipment Hire"
        self.root = Builder.load_file('dummy.kv')
        self.create_entry_buttons()
        return self.root

    def create_entry_buttons(self):

        for name in self.Assignment2:

            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "{} {}".format(name, self.Assignment2[name])
        instance.state = 'down'

    def press_clear(self):
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = "Choose action from the left menu, then select items on the right"

    def press_add(self):
        self.status_text = "Enter details for new phonebook entry"
        self.root.ids.popup.open()

    def press_save(self, added_name, added_number):
        self.Assignment2[added_name] = added_number
        self.root.ids.entriesBox.cols = len(self.Assignment2) // 5 + 1
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        self.root.ids.addedName.text = ""
        self.root.ids.addedNumber.text = ""

    def press_cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = "Choose action from the left menu, then select items on the right"

Assignment2().run()