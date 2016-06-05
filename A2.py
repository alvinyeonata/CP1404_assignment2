from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import ItemList
from AlvinYeonataA1_v2 import *

class Assignment(App):

    def __init__(self):
        item_list = []
        super (Assignment,self).__init__()
        self.item_list=item_list
        self.label_popup="Enter details for new item"

    def build(self):
        self.title = "Items Hire"
        self.root = Builder.load_file('A2.kv')
        self.items()
        self.root.ids.item_list.background_color= [0, 0, 1, 1]
        self.root.ids.hire_item.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[1,0,1,1]
        self.root.ids.confirm.background_color=[1,0,1,1]
        return self.root

    def items(self):

        self.item_list.clear()
        list(self.item_list)
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
                if self.root.ids.item_list.background_color == [0, 0, 1, 1]:
                    self.root.ids.label.text = "{} ({}), ${:,.2f} is {}".format(each[1], each[2], float(each[3]),each[4])
                elif "Hiring" in self.root.ids.label.text:
                    if each[4] == 'in':
                        self.root.ids.label.text = "Hiring: {} for ${:,.2f}".format(each[1], each[3])
                    else:
                        self.root.ids.label.text = "Hiring: no items for $0.00"
                elif "Returning" in self.root.ids.label.text:
                    if each[4] == 'out':
                        self.root.ids.label.text = "Returning: {} for ${:,.2f}".format(each[1], each[3])
                    else:
                        self.root.ids.label.text = "Returning: no items for $0.00"

    def listitem(self):
        self.root.ids.label.text="Choose action from the left menu, then select items on the right"
        self.root.ids.item_list.background_color= [0,0,1,1]
        self.root.ids.hire_item.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[1, 0, 1, 1]
        self.items()

    def save(self, itemName, description, price_per_day):
        """try:
            if itemName== "" or description== "" or price_per_day== "":
                self.label_popup="All field must be answered"
            elif price_per_day< 0 :
                self.label_popup="Value must not be negative"
            else:
        except ValueError:
        """
        add_item = "\n{},{},{},in".format(itemName, description, float(price_per_day))
        with open("items.csv", "a") as file:
            file.writelines(add_item)
            if itemName=="":
                print("Item must be filled")


        self.item_list.append(add_item)
        self.cancel()
        self.items()



    def cancel(self):

        self.root.ids.itemName.text = ""
        self.root.ids.description.text = ""
        self.root.ids.price_per_day.text = ""
        self.root.ids.popup.dismiss()

    def itemhire(self):

        self.root.ids.label.text="Hiring items"
        self.root.ids.item_list.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[1,0,1,1]
        self.root.ids.hire_item.background_color = [0, 0, 1, 1]
        self.items()

    def itemreturn(self):

        self.root.ids.label.text="Returning items"
        self.root.ids.item_list.background_color= [1,0,1,1]
        self.root.ids.hire_item.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[0, 0, 1, 1]
        self.items()

    def additem(self):

        self.root.ids.popup.open()

    def confirm(self):

        if "Hiring" in self.root.ids.label.text:
            for each in self.item_list:
                if each[4] == "in" and each[1] in self.root.ids.label.text:
                    each[4]="out"
                else:
                    pass
        elif "Returning" in self.root.ids.label.text:
            for each in self.item_list:
                if each[4] == "out" and each[1] in self.root.ids.label.text:
                    each[4]="in"
                else:
                    pass
        writing = open("items.csv","w")
        for each in self.item_list:
            print("{},{},{},{}".format(each[1], each[2], each[3], each[4]), file= writing)
        writing.close()
        self.items()

Assignment().run()