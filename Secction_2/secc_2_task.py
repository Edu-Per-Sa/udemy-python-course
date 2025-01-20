# Task 1 - Create two variables
name = 'Luis Peraza'
age = 38


# Task 2 - Function to print the age and name
def print_personal_data(name, age):
    print("My name is " + name + ", and I'm "+ str(age) + " old.")

print_personal_data(name, age)


# Task 3 - Function that print ANY data
def print_any_data(arg1, arg2):
    print("Printing ANY data1:", str(arg1), "and data2:", str(arg2) )

print_any_data("Hola como estas?", 36)


# Task 4 - Decades of age
def calculate_decades(age):
    return age//10

cal_dec = int(input("Inserte su edad: "))
print("Tienes", calculate_decades(cal_dec), "decadas.")