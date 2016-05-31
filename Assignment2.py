from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from Item import *
from itemlist import ItemList
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.togglebutton import ToggleButtonBehavior
"""
Alvin Yeonata

https://github.com/alvinyeonata/CP1404_assignment2
"""

class Assignment2(App):
    def __init__(self, **kwargs):
        super (Assignment2, self).__init__(**kwargs)
        self.item_list = ItemList()
        storage_items = open("items.csv", "r+")
        for line in storage_items:
            self.item_list.store(line)

    def build(self):
        self.title = "Items Hire"
        self.root = Builder.load_file('dummy.kv')
        self.itemlist()
        return self.root

    def itemlist(self):
        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color = (1, 1, 0.5, 1)
        item_count = 0
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            temp_button.bind(on_press=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)
            item_count += 1

    def itemhire(self):
        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.hire_item.background_color = (1, 1, 0.5, 1)
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            temp_button.bind(on_press=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)


    def itemreturn(self):

        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.return_item.background_color = (1, 1, 0.5, 1)
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if "in" in status:
                temp_button = Button(text=name, background_color=(0, 1, 0, 1))
            else:
                temp_button = Button(text=name, background_color=(0.9, 0.3, 0.5, 1))
            temp_button.bind(on_press=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)

    def press_item(self, instance):
        for line in self.item_list:
            name, item_desc, cost, status = line.split(",")
            if instance.text == name:
                if self.root.ids.item_list.background_color == [0, 0.5, 0.5, 1]:  # when item_list is being selected
                    self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(name, item_desc, float(cost), status)
                elif self.root.ids.hire_item.background_color == [0, 0.5, 0.5, 1]:  # when hire_item is being selected
                    if "in" in status:
                        self.root.ids.label.text = "Hiring: {} for ${:,.2f}".format(name, float(cost))
                    else:
                        self.root.ids.label.text = "Hiring: no items for $0.00"
                elif self.root.ids.return_item.background_color == [0, 0.5, 0.5, 1]:  # when return_item is being selected
                    if "out" in status:
                        self.root.ids.label.text = "Returning: {}".format(name)
                    else:
                        self.root.ids.label.text = "Returning: no items"

    def additem(self):

        self.root.ids.add_item.background_color = (1, 1, 0.5, 1)
        self.root.ids.popup.open()

    def save(self, name, item_desc, cost, label):

        def price_check(cost):
            try:
                float(cost)
                return True
            except ValueError:
                return False

        if len(name.strip()) == 0 or len(item_desc.strip()) == 0 or len(cost.strip()) == 0:
            label.text = "All fields must be completed"
        elif price_check(cost) == False:
            label.text = "Price must be valid number"
        elif price_check(cost) == True and float(cost) < 0:
            label.text = "Price cannot be negative"
        else:
            add_item = "\n{},{},{},in".format(name, item_desc, float(cost))
            with open("items.csv", "a") as file:
                file.writelines(add_item)
            self.item_list.store(add_item)
            self.cancel()
            self.itemlist()

    def confirm(self):
        """
        this function will commit changes by modifying the csv file
        :return:
        """
        item_count = 0
        with open("items.csv") as file:
            read_items = file.readlines()
        for line in read_items:
            name, item_desc, cost, status = line.split(",")
            if name in self.root.ids.label.text:
                if self.root.ids.hire_item.background_color == [0, 0.5, 0.5, 1]:  # will only be executed if hire_item is active and an item is being selected
                    self.item_list.clear()
                    read_items[item_count] = read_items[item_count].replace("in", "out")  # will change the status of an item from in to out
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)  # commit changes to the csv file
                    for line in read_items:
                        self.item_list.store(line)
                    file.close()
                    self.itemlist()
                elif self.root.ids.return_item.background_color == [0, 0.5, 0.5, 1]:  # will only be executed if return_item is active and an item is being selected
                    self.item_list.clear()
                    read_items[item_count] = read_items[item_count].replace("out", "in")  # will change the status of an item from in to out
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)  # commit changes to the csv file
                    for line in read_items:
                        self.item_list.store(line)
                    file.close()
                    self.itemlist()
            item_count += 1  # adds each time a unit is written


    def clear_fields(self):
        self.root.ids.itemName.text = ""
        self.root.ids.description.text = ""
        self.root.ids.price_per_day.text = ""


    def cancel(self):
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = "Choose action from the left menu, then select items on the right"

    def terminate(self):
        print("{} items have been saved to items.csv".format(len(self.item_list)))
Assignment2().run()