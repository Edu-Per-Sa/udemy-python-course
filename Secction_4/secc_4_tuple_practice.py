##########################
### TUPLE
##########################

# Definition
tuple_1 = (2, "Carlos", "Antonio", 3.5)


# Printing
print("ORIGINAL Tuple ---> ", tuple_1)


# Indexing
print("Indexing[0] ---> ", tuple_1[0] )


# For Loop
print("For Loop ---> ")
for element in tuple_1:
    print(element)


# List Comprehension
tuple_3 = ((5.4, "Alberto"), (3, "Carlos"), (35, "Eduardo"))

print("List comprehension ---> ")
tuple_4 = ["Hola -> "+str(element) for element in tuple_3 if len(str(element)) > 3 ]
print(tuple_4)


# Unpacking
print("Unpacking by parts ---> ")
for value, name in tuple_3:
    print("Value:", value, ", Name:", name)

print("Unpacking by element ---> ")
for el in tuple_3:
    print(el)


# For with enumerate
print("Printing for with enumerate by element---> ")
for element in enumerate(tuple_1):
    print(element)


# For with enumerate and unpacking
print("Printing for with enumerate and unpacking ---> ")
for index, value in enumerate(tuple_1):
    print(index, value)

