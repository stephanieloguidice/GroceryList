# Make a program that asks for a grocery list
# asks for the department
# would like it to list and save all of those items in a list
# print out that list
# Have a menu to organize it!
grocery_list = []

##functions


def add_grocery():
    grocery_item = input(f"Please input your Grocery Item:")
    department = input(f"Please input the Department:")
    grocery_list.append(grocery_item)
    grocery_list.append(department)
    print("Item: " + grocery_item + " Department: " + department)
    return grocery_list


def return_menu():
    print("Welcome to your Virtual Grocery List!")
    answer = input("Please type Add, List, or End:")

    while True:
        if answer == "Add" or "add":
            add_grocery()
            return_menu()

        elif answer == "List" or "list":
            list_items()

        elif answer == "End" or "end":
            print("Thank you for using the Grocery List App!")
            exit()
        else:
            print("You seem to have headbutted your keyboard"
                  ", please try again.")



print("Welcome to your Virtual Grocery List!")
answer = input("Please type Add, List, or End:")

while True:
    if answer == "Add" or "add":
        add_grocery()
        return_menu()

    elif answer == "List" or "list":
        print(grocery_list)

    elif answer == "End" or "end":
        print("Thank you for using the Grocery List App!")
        exit()
    else:
        print("You seem to have headbutted your keyboard"
              ", please try again.")


# # Adding items and departments to the program
#
#
#
#
# # def grocery():
# #     grocery_item = input("Please input your grocery item:")
# #     department = input("Please input the department:")
# #     grocery_item.append(grocery_list)
# #     department.append(grocery_list)
# #
# #
# # print("Item: " + grocery_item + "Department: "
# #       + department)
#
# # listing the items
#
# # quitting
