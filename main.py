# Jordan Kooyman
# 1/26/21 -
# To-Do List Program - Integration Project for COP 1500 Spring 2021
# Specifications:
# A sortable list of items that can be added, removed, edited, hidden, and marked complete that is stored in a .txt file
# Read data upon program launch - do not crash if file is not present, generate new file
# Data stored in a list, modified from there, and saved to the file when printed to the screen
# Includes a priority system as well as categories and estimated completion time, sortable by all three
# Items can be color coded by category or estimated time
# Menu navigation done with the usage of numeric inputs rather than spelled out commands (if invalid command given, loop
# Configurable settings saved to a separate file (?)
# Ability to load a different data or config file (?)
# TODO: Update Specifications when implementation is complete

# TODO: Add a basic calculator to meet math command requirements (?)

# TODO: Implement a group system that shows all groups combined, just one group, or all categorized by group, and group
#  names - be able to change group names (new function) - all functions support groups (individual or combined)
import random


class ListItem:  # Create a class object that will store the data for each entry in the list (custom variable)
    def __init__(self, text, priority, group, visible):  # From w3schools.com
        self.text = text
        self.priority = priority
        self.group = group
        self.visible = visible


def concept_demonstration():
    number = clean_input("Please enter a positive number")
    number2 = clean_input("Please enter a number")
    while number2 == 0:  # Rejects a 0 if it is input as the second number
        print("Error: Cannot Divide by 0")
        number2 = clean_input("Please enter a different number")
    color = input("Please enter a color\n")
    thing = input("Please enter a thing\n")
    thing2 = thing + ' '  # Adding space so that when thing is repeated, it has a space in between
    location = input("Please enter a location\n")
    print(f"{number} raised to the power of {number2} is {number ** number2}")  # Raise the first number to the
    # second number
    print(f"{number} multiplied by {number2} is {number * number2}")  # Multiply the two numbers
    print(f"{number} divided by {number2} is {number / number2}")  # Divide the first number by the second number
    print(f"The remainder from  dividing {number} by {number2} is {number % number2}")  # Find the modulus of the
    # two numbers
    print(f"{number} divided by {number2} rounded down is {number // number2}")  # Divide the first number by the
    # second and round it down (floor it)
    print(f"{number} plus {number2} is {number + number2}")  # Add the two numbers
    print(f"{number} minus {number2} is {number - number2}")  # Subtract the second number from the first number
    if number > 1:  # if the first number entered is greater than 1
        print(f"The {color + ' ' + thing} at {location} yelled '{thing2 * int(number - 1) + thing}'")  # Combine two
        # strings with + (no added space), repeat a string x number of times with * (must use an integer) (I have
        # the minus 1 and + thing to get the spacing to look proper and still  repeat number amount of times) -
        # if a negative number is used when multiplying a string, it does nothing (but does not crash) - but it
        # is still handled in the other statement with some added user shaming
    elif number < 0:  # if the first number entered is negative
        print(f"The {color + ' ' + thing} at {location} yelled '{thing2 * int(number)}'\nYou entered a negative "
              f"number when a positive number was requested, so you made the {thing} mute. Good Job.")  # Same as
        # above, expect that it will print nothing in the yelled section if the first number entered is negative
    else:  # if the first number entered is 0 or 1 (because of the int() function removing a decimal)
        print(f"The {color + ' ' + thing} at {location} yelled '{thing * int(number)}'")  # this is to prevent
        # errant spaces or showing the phrase too many times
    return


def cascade_list(priority_to_cascade_from, todo_list):
    for item in todo_list:
        if item.priority >= priority_to_cascade_from:
            item.priority += 1
    return


def check_priority_overlap(priority_to_check, todo_list):
    overlap = False
    for item in todo_list:
        if item.priority == priority_to_check:
            overlap = True
    if overlap:
        answer = 0
        while answer > 3 or answer < 1:
            answer = clean_input("The priority number you entered overlaps with another entry's priority. Enter:\n1 to "
                                 "change priority number\n2 to leave as is with overlap\n3 to push all priority numbers"
                                 " below this entry down by 1")
            if answer > 3 or answer < 1:
                print("Invalid Option Selected\nPlease Try Again")
        if answer == 1:
            priority_to_check = check_priority_overlap(int(clean_input("New Priority:")), todo_list)
            # change the priority value input
        elif answer == 3:
            cascade_list(priority_to_check, todo_list)
    return priority_to_check


def sorting(list_object):  # Takes in a ListItem object and returns the priority value - from w3schools.com
    return list_object.priority


def print_list(save_file_location, my_list, to_save=False, show_hidden=False):  # Prints out the To-Do list from the
    # global list variable and saves list to the .txt file
    my_list.sort(key=sorting)  # Uses a custom function to be able to get the right value to sort by
    print("To-Do:")
    for item_index in my_list:  # The range needs to be the length of the list being printed
        if item_index.visible and not show_hidden:  # Only print visible items if show hidden is false
            print(item_index.priority, item_index.text, sep='.\t')
        elif show_hidden:  # Print everything is show hidden is trues
            if item_index.visible:
                print(item_index.priority, item_index.text, sep='.\t')
            else:
                print(f"{item_index.priority}.~\t{item_index.text}")  # Indicate hidden items
        # Printing the item priority with a dot, then the item, with a tab separating them
    if to_save:
        save_list(my_list, save_file_location)
    return


def divider(size=100):  # Draws a dividing line to go between sections (default 100 characters long)
    for i in range(size):
        print('-', end='')  # Prints out a single dash, no newline afterwards (the end= sets the last character to blank
    print('')  # Print out a newline (using the default ending of a print statement being a newline
    return


def clean_input(prompt='Error'):  # A special input function that will reject a user's input of text when a number is
    # requested  --   if no prompt is specified in the program, it will display "Error"
    text = True
    phrase = '0'
    while text:
        phrase = input(prompt + '\n')
        try:  # Adapted from an example in the ThinkPython textbook (15.7) - Checks whether the input is a number,
            # positive or negative. If not, rejects the input and user gets to try again
            float(phrase)
            text = False
        except ValueError:
            print("Error: Non-Numeric Entry Detected")
        # if phrase.isnumeric():  # Checks for a positive number (negative rejected as well as text) - replaced with
        # superior form from textbook example
        #     return float(phrase)  # Return the number the user entered
        # else:
        #     print("Error: Non-Numeric Entry Detected")
    return float(phrase)  # Return the number the user entered


def load_from_file(save_location):  # This is a function for readability - opens txt file in read mode and loads it
    # into an array (list) of ListItem variables
    data_file_r = open(save_location, "r")  # Open txt file in read mode
    list_item = ["Text", -1, 2, True]  # Item, Item Priority, group, is visible
    todo = []  # make a list of lists
    temp = 1  # Temporary counter variable to reconstruct lists from .txt file
    line_counter = 1
    try:
        for item in data_file_r:  # loop through each line in the file, one at a time - from w3schools.com
            if (line_counter - 1) % 5 != 0 and line_counter > 0:
                cleaned_item = ""
                for character_index in range(len(item)):  # Loop through each character in the extracted string
                    if character_index != len(
                            item) - 1:  # if it is not the last character, add it to the cleaned string
                        cleaned_item = cleaned_item + item[character_index]  # Add every character to a string but \n
                if temp == 1:  # Item Text
                    list_item[0] = cleaned_item
                    temp = 2
                elif temp == 2:  # Item Priority
                    list_item[1] = int(cleaned_item)
                    temp = 3
                elif temp == 3:  # Item Group
                    list_item[2] = int(cleaned_item)
                    temp = 4
                elif temp == 4:  # Is Visible
                    if cleaned_item == "False":
                        list_item[3] = False
                    else:  # Assume the item is visible if the text is not False
                        list_item[3] = True
                    todo.insert(0, ListItem(list_item[0], list_item[1], list_item[2], list_item[3]))
                    temp = 1
                else:  # If some error occurred and a condition outside of the possible four is met, restart
                    temp = 1
            line_counter += 1
    except ValueError:
        print("An error has occurred trying to load the file")
        result = int(clean_input("Please enter a 2 to overwrite the current save file and start over or any other "
                                 "number to exit the program"))
        if result == 2:
            key = random.randint(1, 9)  # Generate a random integer between 1 and 9 to be used as a second dynamic check
            result2 = int(clean_input(f"Are you sure you want to delete all of your saved data\nEnter {key} to proceed,"
                                      f" or anything else to cancel"))
            if result2 == key:
                data_file_w = open("C:Item_List.txt", "w")
                data_file_w.close()
                todo = []
                print("Save Data Erased")
                return todo  # Return an empty list if file load failed
            else:
                print("Program Exiting")
                quit(1)
        else:
            print("Program Exiting")
            quit(1)  # Exit the program with the exit code of 1
    data_file_r.close()
    # All the list functions above referenced from w3schools.com What is happening above: Opening the file,
    # initializing a list to hold all four pieces of data, then after pulling the data from the file and storing in
    # the list, it is copied (not referenced) into my main list of ListItem objects
    return todo


def save_list(todo_list, save_location):
    data_file_w = open(save_location, "w")  # open the save file and clear the data from it
    data_file_w.write(f"Warning: The Todo-List Program will not be able to load this save file if it is incorrectly "
                      f"modified. Modify at your own risk. The structure is Entry Text, Entry Priority as a number, "
                      f"Entry Group as a number, and Entry Visibility as a boolean, each on a separate line, "
                      f"a single line gap in between, and the very first line is skipped\n")
    for item in todo_list:
        data_file_w.write(f"{item.text}\n{item.priority}\n{item.group}\n{item.visible}\n\n")
    data_file_w.close()
    return


def add_item(todo_list):
    text = input("Please enter the name of the new item\n")
    priority = check_priority_overlap(int(clean_input("Please enter the priority of this item")), todo_list)
    group = int(clean_input("Please enter the group number of this item"))
    visible = True
    todo_list.insert(0, ListItem(text, priority, group, visible))  # Join the inputs to be added to the overall list
    return


def select_item(todo_list, show_hidden, prompt='Error'):  # Ask the user which item from the list is to be modified
    valid = False
    index = 0
    while not valid:
        x = 1  # counter for index printing
        for item in todo_list:  # The range needs to be the length of the list being printed
            if item.visible and not show_hidden:  # Only print visible items if show hidden is false
                print(x, item.text, sep='\t')
            elif show_hidden:  # Print everything is show hidden is true
                if item.visible:
                    print(x, item.text, sep='\t')
                else:
                    print(x, f"~ {item.text} ~", sep='\t')
            x += 1
            # Printing the item number, then the item, with a tab separating them
        index = int(clean_input(prompt))
        if index < x:
            valid = True
        else:
            print("Invalid Input: Number is too big")
    return index - 1


def remove_item(todo_list, show_hidden):
    item = select_item(todo_list, show_hidden, "Please enter the item number you wish to remove\nEnter a negative "
                                               "number or zero to cancel")
    if item >= 0:  # 0, not 1 because the index returned is shifted to be computer friendly
        todo_list.pop(item)
    return


def mark_complete(todo_list, show_hidden):
    item = select_item(todo_list, show_hidden, "Please enter the item number you wish to Mark Completed and hide from "
                                               "the list\nEnter a negative number or zero to cancel")
    if item >= 0:
        todo_list[item].visible = False
    return


def edit_item(todo_list, show_hidden):
    item = select_item(todo_list, show_hidden, "Please enter the item number you wish to edit\nEnter a negative "
                                               "number or zero to cancel")
    if item >= 0:
        while True:
            value = clean_input(f"Which value would you like to edit? Enter:\n1 for the Item Text (Currently: "
                                f"{todo_list[item].text})\n2 for the Item Priority (Currently: "
                                f"{todo_list[item].priority})\n3 for the Group (Currently: {todo_list[item].group})"
                                f"\n4 to Cancel and Exit")
            if value == 1:  # Item Text Change
                print(f"The Current Text is: {todo_list[item].text}")
                todo_list[item].text = input("New Text:\n")
            elif value == 2:  # Item Priority Change
                print(f"The Current Priority is: {todo_list[item].priority}")
                todo_list[item].priority = check_priority_overlap(int(clean_input("New Priority:")), todo_list)
            elif value == 3:  # Item Group Change
                print(f"The Current Group is: {todo_list[item].group}")
                todo_list[item].group = int(clean_input("New Group Number:"))
            elif value == 4:  # Exit Changing Menu
                break
            else:
                print("Invalid Input - Please Try Again")
    return


def check_list_status(todo_list):  # Checks if the list is completely hidden (2), completely empty (1), or neither (0)
    if len(todo_list) == 0:
        state = 1  # Empty List
    else:
        state = 2  # Entirely Hidden List
        for item_index in range(len(todo_list)):
            if todo_list[item_index].visible:  # If an item is visible, then they are not all hidden
                state = 0  # Neither
    return state


def menu_loop(todo_list, save_file_location):
    show_hidden = False
    selection = 0
    invalid_input = False
    while selection != 6:
        if invalid_input:
            invalid_input = False
        else:
            print_list(save_file_location, todo_list, True, show_hidden)
        divider(137 + 17)  # Length of prompt statement below
        list_status = check_list_status(todo_list)
        if list_status == 0:  # No Issues
            selection = int(clean_input("Please enter: 1 for Add Item, 2 for Remove Item, 3 for Edit Item, 4 for Mark "
                                        "Item Complete, 5 for Toggle Hidden, and 6 for Exit, 7 for Concept "
                                        "Demonstration\n"))
        elif list_status == 1:  # Empty List - No Remove, Edit, Mark, or Toggle
            selection = int(clean_input("Please enter: 1 for Add Item, and 6 for Exit, 7 for Concept Demonstration\n"))
        else:  # Entirely Hidden List
            selection = int(clean_input("Please enter: 1 for Add Item, 5 for Toggle Hidden, and 6 for Exit, "
                                        "7 for Concept Demonstration\n"))
            # Uses the clean_input function above to get a number from the user, converting it to an int so a decimal
            # won't return an invalid input in the following steps
        print("")  # Blank Print statement to add an extra blank line after user input before displaying response
        if selection == 1:  # Add Item - modify the list variable, then save to file
            add_item(todo_list)
        elif selection == 2:  # Remove Item - modify the list variable, then save to file
            if list_status == 0:
                remove_item(todo_list, show_hidden)
            elif list_status == 2:
                print("Invalid Command: The Todo List has no visible items to remove")
            else:
                print("Invalid Command: The Todo List has no items to remove")
        elif selection == 3:  # Edit Item - modify the list variable, then save to file
            if list_status == 0:
                edit_item(todo_list, show_hidden)
            elif list_status == 2:
                print("Invalid Command: The Todo List has no visible items to edit")
            else:
                print("Invalid Command: The Todo List has no items to edit")
        elif selection == 4:  # Mark Item Complete - modify the list variable, then save to file
            if list_status == 0:
                mark_complete(todo_list, show_hidden)
            elif list_status == 2:
                print("Invalid Command: The Todo List has no visible items to mark complete")
            else:
                print("Invalid Command: The Todo List has no items to mark complete")
        elif selection == 5:  # Show Hidden - modify the list variable, then save to file
            if list_status == 0 or list_status == 2:
                if show_hidden:
                    print("No longer showing hidden items")
                    show_hidden = False
                else:
                    print("Now showing hidden items")
                    show_hidden = True
            else:
                print("Invalid Command: The Todo List has no items to show or hide")
        elif selection == 6:  # Exit Program
            print("Now Closing")
        elif selection == 7:  # Temporary (?) section to demonstrate proficiency with topics covered in class - Sprint 1
            concept_demonstration()  # If I have extra time/motivation, this will become a simple calculator
        else:
            invalid_input = True
            print("Invalid Input\nPlease Try Again")


def main():
    save_file_location = "C:Item_List.txt"
    data_file_a = open(save_file_location, "a")  # Opens ItemList.txt which is accessible in the file variable,
    # in append mode (using this so that if the file exists, nothing happens, but if it does not exist,
    # it gets created from w3schools.com
    data_file_a.close()  # Close the file, I now know it exists
    loaded_list = load_from_file(save_file_location)
    print(f"Welcome to the To-Do List - Version: 0.1.2")
    divider(42)  # Length of welcome statement above
    menu_loop(loaded_list, save_file_location)


main()
