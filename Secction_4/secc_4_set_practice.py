###########################
### SET
###########################

# Definition
set_1 = {"Maria", 2, "Carlos", 2}


# Printing
print('Printing {"Maria", 2, "Carlos", 2} ---> ', set_1)
print("The elements is not duplicated...")


# Indexing
#print("Indexing ---> ", set_1[1])
print("Indexing is not allowed...")


# Unpacking
print ("unpacking ---> ")
a, b , c = set_1
print(a)
print(b)
print(c)


# For
print("For loop ---> ")
for element in set_1:
    print(element)


# List Comprehension
print("List Comprehension ---> ")
set_comprehension = [element*2 for element in set_1]
print(set_comprehension)


# BAD COPY
print("BAD COPY ---> ")
set_2 = set_1

print("Set_1 (ORIGINAL) ---> ", set_1)
print("Set_2 (ORIGINAL) ---> ", set_2)

print("Adding alberto...")
set_2.add("Alberto")

print("Set_1 (BAD) ---> ", set_1)
print("Set_2 (BAD) ---> ", set_2)


# GOOD COPY
print("GOOD COPY ---> ")
set_2 = set_1.copy()

print("Set_1 (ORIGINAL) ---> ", set_1)
print("Set_2 (ORIGINAL) ---> ", set_2)

print("Adding JUAN...")
set_2.add("JUAN")

print("Set_1 (GOOD) ---> ", set_1)
print("Set_2 (GOOD) ---> ", set_2)
