#################################
### DICTIONARY
#################################

# Definition
dic_1 = {
    "name": "Eduardo",
    "age": "39"
    }

# Print Dictionary
print("Printing dictionary --->", dic_1)

# Accesing Data Element
print('Access to element "age" ---> ', dic_1["age"])

# Changing value
dic_1['age'] = 56
print('Changing value "age = 56" ---> ', dic_1)


# For
print("For by key --->")
for key in dic_1:
    print(key)

print("For by values --->")
for value in dic_1.values():
    print(value)

print('For by pair (key, value) --->')
for (key, value) in dic_1.items():
    print(key, value)


dic_2 = [{"id": name, "value": val } for name, val in dic_1.items() if len(name) > 2]
print(dic_2)


# Nested Dioctionary
dic_3 = {
    "obj_1": {"name": "Alfredo", "age": 34},
    "obj_2": {"name": "Eduardo", "age": 38},
    "obj_3": {"name": "Tico", "age": 70}
}

print("Accesing to nested dic ---> ")
for key, value in dic_3.items():
    print("Key L1:", key)
    print("Value L1:", value)
    for item in value.items():
        print(type(item))
        print("Key L2:", item[0])
        # print("Value L2:", item["age"])

