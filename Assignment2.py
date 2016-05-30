from kivy.app import App
from kivy.lang import Builder

"""
Alvin Yeonata


"""

class Assignment2(App):
    def build(self):
        self.title = "Assignment2"
        self.root = Builder.load_file('Assignment2_txt.kv')
        return self.root

    def addItem(self):
        self.title= "Equipment Hire"
        self.root = Builder.load_file('test.kv')
        return self.root

    def itemList(self):
        self.root.ids.itemBox.clear_widgets()
        se

Assignment2().run()