# Task 1 - Create a list of name and output the length of each name.
# Task 2 - Add an if check and output just name that are longer than 5 characters.
# Task 3 - Add another if check that see if the name include "n" or "N" character.
# Task 4 - Use a while loop that empty the list of names.

#######################
# Task 1
#######################
names = ['Maria', "Eduardo", "Alfredo", "Ana", "Carlos", "Natalia"]

def add_name():
    names.append(input("Write the next name in the list: "))


def print_length_names(names):
    print("*" * 30)
    print("The lenght of ALL NAMES are: ")
    for name in names:
        print(name + ": " + str(len(name)))
    print("*" * 30)

#######################
# Task 2
#######################
def print_names_longer_five_characters(names):
    print("*" * 30)
    print("The lenght of each name (>5 characters) are: ")
    for name in names:
        if len(name) > 5:
            print(name + ": " + str(len(name)))
    print("*" * 30)

#######################
# Task 3 - Include "n" or "N"
#######################
def print_names_include_n_N(names):
    print("*" * 30)
    print("Names that inclunde 'n' or 'N' are: ")
    for name in names:
        if "n" in name or "N" in name:
            print(name + ": " + str(len(name)))
    print("*" * 30)


#######################
# Task 4 - Delete ALL Elements
#######################
def erase_names(names):
    while len(names) >= 1:
        names.pop()
    print("*" * 30)
    print("Names DELETED...!")
    print("*" * 30)



def delete_element(names):
    elements_str = "["
    for i in range(len(names)):
        elements_str += names[i] + " (" + str(i) + ")"
        if len(names)-1 != i:
            elements_str += ", "
    elements_str += "]"
    print(elements_str)
    index_selected = int(input("Select one element (number) to delete: "))
    name_deleted = names.pop(index_selected)
    print("Name deleted: ", name_deleted)


main_loop = True

while main_loop:
    print("""Chose one option:
    1 - Add name to the list.
    2 - Print the length of each name.
    3 - Print names that have more than 5 characters.
    4 - Print names that include "n" or "N".
    5 - Delete an element.
    6 - ERASE ALL names.
    e - Exit""")
    option_selected = input()

    if option_selected == "1":
        add_name()

    elif option_selected == "2":
        print_length_names(names)
        
    elif option_selected == "3":
        print_names_longer_five_characters(names)
        
    elif option_selected == "4":
        print_names_include_n_N(names)
        
    elif option_selected == "5":
        delete_element(names)
        
    elif option_selected == "6":
        erase_names(names)

    elif option_selected == "e":
        main_loop = False
        
    else:
        print ("Invlaid option...")

print("Closed...")
print("Names in the list: ", names)
