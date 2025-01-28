
# Taks 1 - Create a list of persons dictionary with a list of hobbies. (name, age, [hobbies])
# Task 2 - Convert the list into a list of persons.
# Task 3 - Create a list of persons where the age are older than 30.
# Task 4 - Copy the person list safely to edit.


# Task 1 
persons = [
    {"name": "Alfredo", "age": 36, "hobbies": ["Baseball", "Nintendo", "Ejercicios"]},
    {"name": "Eduardo", "age": 38, "hobbies": ["PinPon", "Psicologia", "Aprender"]},
    {"name": "Tico", "age": 70, "hobbies": ["Deportes", "Peliculas", "Caminar"]},
    {"name": "Eugenio", "age": 2, "hobbies": ["No", "OtaPaVe", "Juguetes", "Rabia"]},
    {"name": "Amanda", "age": 1, "hobbies": ["Lamer", "Llorar", "Babear"]},
    ]

# Task 2
list_persons = [el["name"] for el in persons]
print("List of name of persons ---> ", list_persons)

# Task 3
persons_30 = [el["name"] for el in persons if el["age"] > 30]
print("List of persons more than 30 ---> ", persons_30)

# Task 4
persons_copy = persons[:]
print("persons is persons_copy? ---> ", persons_copy is persons)

persons_copy[0]["name"] = "JULIO"

print("Persons ---> ", persons)
print("Persons_copy ---> ", persons_copy)
