from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import ItemList
from item import Item
from AlvinYeonataA1_v2 import loading_items

"""
Alvin Yeonata
Date: 31/5/2016
This is a code about an application in which is the items in taken froma csv file.
This codes will allow changes in the csv file allowing a change in availability status and adding items.
https://github.com/alvinyeonata/CP1404_assignment2
"""

class Assignment2(App):

    def __init__(self, **kwargs):
        super (Assignment2, self).__init__(**kwargs)
        self.item_list = ItemList()
        items_storage = open("items.csv", "r+")
        for line in items_storage:
            self.item_list.store(line)

    def build(self):

        self.title = "Items Hire"
        self.root = Builder.load_file('Assignment2.kv')
        self.itemlist()
        return self.root

    def itemlist(self):

        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color =  [0, 0.5, 0.5, 1]
        self.root.ids.hire_item.background_color = [1, 1, 1, 1]
        self.root.ids.return_item.background_color = [1, 1, 1, 1]
        self.root.ids.confirm.background_color = [1, 1, 1, 1]
        self.root.ids.add_item.background_color = [1, 1, 1, 1]
        item_count = 0
        for line in self.item_list:
            name, description, price_per_day, availability = line.split(",")
            if "in" in availability:
                temp_button = Button(text=name, background_color=[0, 1, 0, 1])
            else:
                temp_button = Button(text=name, background_color=[0.9, 0.3, 0.5, 1])
            temp_button.bind(on_press=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)
            item_count += 1

    def itemreturn(self):

        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.label.text = 'Choose action from the left menu, then select items on the right'
        self.root.ids.item_list.background_color = [1, 1, 1, 1]
        self.root.ids.hire_item.background_color = [1, 1, 1, 1]
        self.root.ids.return_item.background_color = [0, 0.5, 0.5, 1]
        self.root.ids.confirm.background_color = [1, 1, 1, 1]
        self.root.ids.add_item.background_color = [1, 1, 1, 1]
        for line in self.item_list:
            name, description, price_per_day, availability = line.split(",")
            if "in" in availability:
                temp_button = Button(text=name, background_color=[0, 1, 0, 1])
            else:
                temp_button = Button(text=name, background_color=[0.9, 0.3, 0.5, 1])
            temp_button.bind(on_press=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)

    def itemhire(self):
        self.root.ids.itemsBox.clear_widgets()
        self.root.ids.item_list.background_color = [1, 1, 1, 1]
        self.root.ids.hire_item.background_color = [0, 0.5, 0.5, 1]
        self.root.ids.return_item.background_color = [1, 1, 1, 1]
        self.root.ids.confirm.background_color = [1, 1, 1, 1]
        self.root.ids.add_item.background_color = [1, 1, 1, 1]
        for line in self.item_list:
            name, description, price_per_day, availability = line.split(",")
            if "in" in availability:
                temp_button = Button(text=name, background_color=[0, 1, 0, 1])
            else:
                temp_button = Button(text=name, background_color=[0.9, 0.3, 0.5, 1])
            temp_button.bind(on_press=self.press_item)
            self.root.ids.itemsBox.add_widget(temp_button)

    def press_item(self, instance):

        for line in self.item_list:
            name, description, price_per_day, availability = line.split(",")
            if instance.text == name:
                if self.root.ids.item_list.background_color == [0, 0.5, 0.5, 1]:
                    self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(name, description, float(price_per_day), availability)
                elif self.root.ids.hire_item.background_color == [0, 0.5, 0.5, 1]:
                    if "in" in availability:
                        self.root.ids.label.text = "Hiring: {} for ${:,.2f}".format(name, float(price_per_day))
                    else:
                        self.root.ids.label.text = "Hiring: no items for $0.00"
                elif self.root.ids.return_item.background_color == [0, 0.5, 0.5, 1]:
                    if "out" in availability:
                        self.root.ids.label.text = "Returning: {}".format(name)
                    else:
                        self.root.ids.label.text = "Returning: no items"

    def confirm(self): #this made a confirm change on the hire/return

        item_count = 0
        with open("items.csv") as file:
            read_items = file.readlines()
        for line in read_items:
            name, description, price_per_day, availibility = line.split(",")
            if name in self.root.ids.label.text:
                if self.root.ids.hire_item.background_color == [0, 0.5, 0.5, 1]:
                    self.item_list.clear()
                    read_items[item_count] = read_items[item_count].replace("in", "out")
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)
                    for line in read_items:
                        self.item_list.store(line)
                    file.close()
                    self.itemlist()
                elif self.root.ids.return_item.background_color == [0, 0.5, 0.5, 1]:
                    self.item_list.clear()
                    read_items[item_count] = read_items[item_count].replace("out", "in")
                    with open("items.csv", "w") as file:
                        file.writelines(read_items)  # commit changes to the csv file
                    for line in read_items:
                        self.item_list.store(line)
                    file.close()
                    self.itemlist()
            item_count += 1

    def save(self, name, description, price_per_day, availibility): #saves the details in the popup menu

        def price_check(cost):
            try:
                float(cost)
                return True
            except ValueError:
                return False

        if len(name.strip()) == 0 or len(description.strip()) == 0 or len(price_per_day.strip()) == 0:
            availibility.text = "All fields must be completed"
        elif price_check(price_per_day) == False:
            availibility.text = "Price must be valid number"
        elif price_check(price_per_day) == True and float(price_per_day) < 0:
            availibility.text = "Price cannot be negative"
        else:
            add_item = "\n{},{},{},in".format(name, description, float(price_per_day))
            with open("items.csv", "a") as file:
                file.writelines(add_item)
            self.item_list.store(add_item)
            self.cancel()
            self.itemlist()

    def additem(self): #opens up the popup menu

        self.root.ids.item_list.background_color = [1, 1, 1, 1]
        self.root.ids.hire_item.background_color = [1, 1, 1, 1]
        self.root.ids.return_item.background_color = [1, 1, 1, 1]
        self.root.ids.confirm.background_color = [1, 1, 1, 1]
        self.root.ids.add_item.background_color = [0, 0.5, 0.5, 1]
        self.root.ids.popup.open()
    def cancel(self): #turn back the popup as it's default
        self.root.ids.itemName.text = ""
        self.root.ids.description.text = ""
        self.root.ids.price_per_day.text = ""
        self.root.ids.popup.dismiss() #closes the popup


Assignment2().run()