############################
##### LIST 
############################

# Definition
list_1 = [1, 2, 3]


# Printing
print("Printing ---> ", list_1)


# Indexing
print("indexing ---> ", list_1[0])


# Unpacking
a, b , c = list_1
print("Unpacking ---> ")
print(a)
print(b)
print(c)


# For
print("For element ---> ")
for element in list_1:
    print(element)


# List comprehension
print("list Comprehension ---> ")
list_comp = [el*2 for el in list_1] 
print(list_comp)


# Copy (BAD)
print("Doing a copy with list_2 = list_1 ---> ")
list_2 = list_1

print("list_1 Before: ", list_1)
print("list_2 Before: ", list_2)

list_2[0] = 20

print("list_1 After (BAD): ", list_1)
print("list_2 After (BAD): ", list_2)


# Copy (GOOD)
print("Doing a copy with list_2 = list_1[:] ---> ")
list_2 = list_1[:]

print("list_1 Before: ", list_1)
print("list_2 Before: ", list_2)

list_2[0] = 56

print("list_1 After (GOOD): ", list_1)
print("list_2 After (GOOD): ", list_2)
