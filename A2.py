from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import ItemList
from AlvinYeonataA1_v2 import *

class Assignment(App):

    def __init__(self):
        item_list = []
        super (Assignment,self).__init__()
        list(item_list)
        self.item_list=item_list

    def build(self):
        self.title = "Items Hire"
        self.root = Builder.load_file('A2.kv')
        self.items()
        return self.root

    def items(self):
        self.root.background_color= [1, 1, 1, 1]
        self.root.ids.itemsBox.clear_widgets()
        for each in self.item_list:
            button1 = Button(text=each[1])
            button1.bind(on_release=self.press_key)
            if each[4] == 'out':
                button1.background_color = [1, 0, 0, 1]
            else:
                button1.background_color = [0, 1, 0, 1]
            self.root.ids.itemsBox.add_widget(button1)

    def press_key(self,instance):

        for each in self.item_list:
            if instance.text == each[1]:
                print(each)
                if self.root.background_color == [1, 0, 0, 1] or self.root.background_color == [0, 1, 0, 1]:
                    self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(each[1], each[2], float(each[3]),each[4])
                elif self.root.ids.hire_item.background_color == [0, 1, 0, 1]:
                    if each[4] == 'in':
                        self.root.ids.label.text = "Hiring: {} for ${:,.2f}".format(each[1], each[2], float(each[3]))
                    else:
                        self.root.ids.label.text = "Hiring: no items for $0.00"
                elif self.root.ids.return_item.background_color == [1, 0, 0, 1]:
                    if each[4] == 'out':
                        self.root.ids.label.text = "Returning: {}".format(each[1])
                    else:
                        self.root.ids.label.text = "Returning: no items"

    def additem(self):
        self.root.ids.popup.open()

    def cancel(self):
        self.root.ids.itemName.text = ""
        self.root.ids.description.text = ""
        self.root.ids.price_per_day.text = ""
        self.root.ids.popup.dismiss()

Assignment().run()