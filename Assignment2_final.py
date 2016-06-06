from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import ItemList
from AlvinYeonataA1_v2 import *
"""
Alvin Yeonata
Date: 6/6/2016 11:55
This is a code about an application in which is the items in taken froma csv file.
This codes will allow changes in the csv file allowing a change in availability status and adding items.
https://github.com/alvinyeonata/CP1404_assignment2
"""
class Assignment(App):

    def __init__(self):

        item_list = []
        super (Assignment,self).__init__()
        self.item_list=item_list

    def build(self):

        self.title = "Items Hire"
        self.root = Builder.load_file('Assignment2_final.kv')
        self.items()
        self.root.ids.item_list.background_color= [0, 0, 1, 1]
        self.root.ids.hire_item.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[1,0,1,1]
        self.root.ids.confirm.background_color=[1,0,1,1]
        return self.root

    def items(self): #this activates the

        self.item_list.clear()
        list(self.item_list) #this opens the csv from Assignment1
        self.root.ids.itemsBox.clear_widgets()
        for each in self.item_list:
            button1 = Button(text=each[1])
            button1.bind(on_release=self.press_key)
            if each[4] == 'out': #makes sure of the color changes to differentiate out and in
                button1.background_color = [1, 0, 0, 1]
            else:
                button1.background_color = [0, 1, 0, 1]
            self.root.ids.itemsBox.add_widget(button1)

    def listitem(self): #this makes the icon when pressed to change color to see which is being clicked

        self.root.ids.label.text="Choose action from the left menu, then select items on the right"
        self.root.ids.item_list.background_color= [0,0,1,1]
        self.root.ids.hire_item.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[1, 0, 1, 1]
        self.items() #this always go back to the item so that any changes to the csv will be loaded in immediately


    def itemhire(self):#this makes the icon when pressed to change color to see which is being clicked
        self.root.ids.label.text="Hiring items"
        self.root.ids.item_list.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[1,0,1,1]
        self.root.ids.hire_item.background_color = [0, 0, 1, 1]
        self.items()

    def itemreturn(self):#this makes the icon when pressed to change color to see which is being clicked
        self.root.ids.label.text="Returning items"
        self.root.ids.item_list.background_color= [1,0,1,1]
        self.root.ids.hire_item.background_color=[1,0,1,1]
        self.root.ids.return_item.background_color=[0, 0, 1, 1]
        self.items()

    def additem(self): #this simply activates the popup menu
        self.root.ids.popup.open()

    def press_key(self,instance): #this is what happen when the button is pressed

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


    def confirm(self): #this saves the changes

        if "Hiring" in self.root.ids.label.text: #the condition when the hire is clicked, then the following can work
            for each in self.item_list:
                if each[4] == "in" and each[1] in self.root.ids.label.text: #changes in to out
                    each[4]="out"
                else:
                    pass
        elif "Returning" in self.root.ids.label.text: #the condition when the return is clicked, then the following can work
            for each in self.item_list:
                if each[4] == "out" and each[1] in self.root.ids.label.text: #changes out to in
                    each[4]="in"
                else:
                    pass

        writing = open("items.csv","w") #this opens the csv file and update the changes
        for each in self.item_list:
            print("{},{},{},{}".format(each[1], each[2], each[3], each[4]), file= writing)
        writing.close()
        self.items()

    def save(self, itemName, description, price_per_day):

        try:
            float(price_per_day)
            if itemName == "" or description == "" or price_per_day== "":
                self.root.ids.label_popup.text="All field must be answered"
            elif float(price_per_day) < 0 :
                self.root.ids.label_popup.text="Value must not be negative"
            else:
                add_item = "\n{},{},{},in".format(itemName, description, float(price_per_day))
                with open("items.csv", "a") as file:
                    file.writelines(add_item)
                    if itemName=="":
                        print("Item must be filled")
                self.item_list.append(add_item)
                self.cancel()
                self.items()

        except ValueError:
            if itemName == "" or description == "" or price_per_day== "":
                self.root.ids.label_popup.text="All field must be answered"
            else:
                self.root.ids.label_popup.text="Value must be in number"

    def cancel(self): # this makes the reset on the add item
        self.root.ids.itemName.text = ""
        self.root.ids.description.text = ""
        self.root.ids.price_per_day.text = ""
        self.root.ids.popup.dismiss()


Assignment().run()