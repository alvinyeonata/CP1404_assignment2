from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
"""
Alvin Yeonata

https://github.com/alvinyeonata/CP1404_assignment2
"""


class Assignment2(App):
    def build(self):
        self.title = "Equipment Hire"
        self.root = Builder.load_file('Assignment2_txt.kv')
        return self.root

    def addItem(self):
        self.title= "Equipment Hire"
        self.root.ids = Builder.load_file('test.kv')
        return self.root

    def pressed(self):
        self.root.ids=Builder.load_file('test.kv')
        return self.root

    def clearing(self):
        print("Clearing")
        self.root.ids.input_name1.text = ""
        self.root.ids.input_name2.text = ""
        self.root.ids.input_name3.text = ""
        self.root.ids.output_label.text = "Save item"

Assignment2().run()