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

    def build(self):
        self.title = "Items Hire"
        self.root = Builder.load_file('dummy.kv')
        self.itemlist()
        return self.root

    def itemlist(self):
        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color = (1, 1, 0.5, 1)
        read_items = open('items.csv', 'r')
        list_items = read_items.readlines()
        self.item_list = list_items
        print(self.item_list)
        print(self.item_list.__len__())
        self.number_of_items = self.item_list.__len__()
        self.create_item_buttons()
        read_items.close()

    def itemhire(self):
        self.root.ids.itemsBox.clear_widgets()

        self.root.ids.hire_item.background_color = (1, 1, 0.5, 1)

        read_items = open('items.csv', 'r')
        list_items = read_items.readlines()
        self.item_list = list_items
        print(self.item_list)
        print(self.item_list.__len__())
        self.number_of_items = self.item_list.__len__()
        self.create_item_buttons()
        read_items.close()

    def itemreturn(self):
        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'

        self.root.ids.return_item.background_color = (1, 1, 0.5, 1)

        read_items = open('items.csv', 'r')
        list_items = read_items.readlines()
        self.item_list = list_items
        print(self.item_list)
        print(self.item_list.__len__())
        self.number_of_items = self.item_list.__len__()
        self.create_item_buttons()
        read_items.close()

    def create_item_buttons(self):
        print("*****", self.item_list)
        for item in self.item_list:
            name, item_desc, cost, status = item.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0, 0, 1, 1))
            temp_button.bind(on_release=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)

    def press_item(self, instance):
        for item in self.item_list:
            name, item_desc, cost, status = item.split(",")
            if instance.text == name:
                self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(name, item_desc, float(cost),
                                                                            status)
    def additem(self):

        self.root.ids.add_item.background_color = (1, 1, 0.5, 1)
        self.root.ids.popup.open()

    def clear_fields(self):
        self.root.ids.itemName.text = ""
        self.root.ids.description.text = ""
        self.root.ids.price_per_day.text = ""

    def press_save(self, added_name, added_number):
        self.Assignment2[added_name] = added_number
        self.root.ids.entriesBox.cols = len(self.Assignment2) // 5 + 1
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = "Choose action from the left menu, then select items on the right"

Assignment2().run()