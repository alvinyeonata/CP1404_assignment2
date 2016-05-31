"""
Alvin Yeonata 13255785
this program allows the user to view all the list from another file,
adding of items from the list and editing the data.
https://github.com/alvinyeonata/CP1404_assingment1.git
"""
def loading_items(item_list):
    """vertical
    pseudo code

    read file from the item_list
    for hire in item_list
        if hire="out"
            change hire to "*" #showing that the item is out
        elif hire="in"
            change hire to " " #blank to show that it is in


    """
    for item in item_list:
        if "out" in item[4]:
            print("{} - {:<40s} = ${:>7.2f}*".format(item[0],item[1]+" ("+item[2]+")",item[3]))
        elif "in" in item[4]:
            print("{} - {:<40s} = ${:>7.2f}".format(item[0],item[1]+" ("+item[2]+")",item[3]))
        #print(hire)

    return


def hiring_an_item(item_list):
    """
    pseudo code

    Get item from item_list
        For items in item_list
            if hire is "in"
                display the line
            else
                do nothing
        If item number is < 0
            print error
        elif answer is the same as the item number then
            change "in" for item number as "out"
        else
            print "That item is not available for hire"


    """
    list_Num = []
    for item in item_list:
        if item[4] == "in":
            print("{} - {:<40s} = ${:>7.2f}".format(item[0],item[1]+" ("+item[2]+")",item[3]))
            list_Num.append(item[0])
    if len(list_Num) == 0:
        print("Currently no item is available to hire")#if there is no items to hire
    else:
        try:
            change = int(input("Enter the number of an item to hire:"))
            if change in list_Num:
                for item in item_list:
                    if item[0] == change: #changing the state of item to hire
                        item[4] = "out"
            elif change > len(item_list)-1 or change < 0:
                print("Invalid input")
            else:
                print("That item is not available for hire")
        except ValueError:
            print("Invalid input")
    return

def main():

    items=open("items.csv","r")#opening the file and reading it
    item_list=[]
    item_Count=0

    for each_line in items: #getting the whole line to be categorized into fields to make it easy to change
        name, description, price_per_day, hire = each_line.strip().split(',')
        item = [item_Count, name, description, float(price_per_day), hire]
        item_list.append(item)
        item_Count+=1

    #Counting the items in the csv file
    item_line = 0
    for line_str in item_list: #looping so there is a number increase for every line in the csv
        item_line += 1

    print(item_line, " Items for Hire - by Alvin Yeonata")
    MENU = " Menu:\n (L)ist all items \n (H)ire an item \n (R)eturn an item \n (A)dd new item to stock \n (Q)uit \n >>>"

    USER_INPUT =""

    while USER_INPUT != "Q": #Making the loop so that only if the user press Q, it'll end the loop
        USER_INPUT = input(MENU)



        if USER_INPUT =="Q" or USER_INPUT =="q": #making an exit path to end the program
            print(item_Count, "items saved to item.csv")
            print("Have a nice day :)")
            break



        elif USER_INPUT =="L" or USER_INPUT =="l": #list all the items in the csv file
            print("All items on file (* indicates item is currently out):")
            loading_items(item_list)#calls function



        elif USER_INPUT =="H" or USER_INPUT =="h": #hiring items
            hiring_an_item(item_list)#calling function



        elif USER_INPUT =="R" or USER_INPUT =="r": # Returns the hired items
            list_Num = []#list
            for item in item_list:
                if item[4] == "out":
                    print("{} - {:<40s} = ${:>7.2f}".format(item[0],item[1]+" ("+item[2]+")",item[3]))
                    list_Num.append(item[0])

            if len(list_Num) == 0:# checking if is any item to hire
                print("Currently no item is available to hire")
            else:
                try:
                    change = int(input("Enter the number of an item to hire:"))
                    if change in list_Num:
                        for item in item_list:
                            if item[0] == change:
                                item[4] = "in"
                                print(item[1],"is returned")
                    elif change > len(item_list)-1 or change < 0:
                        print("Invalid input")
                    else:
                        print("That item is not available for hire")
                except ValueError:
                    print("Invalid input")


        elif USER_INPUT =="A" or USER_INPUT =="a": # Adding new items into the list

            item_name = input("Item name: ")

            while len(item_name) < 0:
                print("Input can not be blank")
                item_name = input("Item name: ")
            description = input("Description: ")

            while len(description) < 0:
                print("Input cannot be blank")
                description = input(" Description: ")

            try:
                price_per_day = float(input("Item price: $"))

                while price_per_day < 0:
                    print("Price must be >= 0 \n Invalid input, enter a valid number")
                    price_per_day = float(input("Item price: $"))

            except ValueError:
                print("Invalid input, enter a valid number")
                item_price = float(input("Item price: $"))

            items=open("items.csv", "a")
            print("{},{},{},{}".format(item_name, description, price_per_day, "in"), file=items)
            items.close()
            item_Count += 1
            print("{} ({}), ${:,.2f} now available for hire".format(item_name, description, price_per_day))

        else:
            print("Invalid response")

main()
