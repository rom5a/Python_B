person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

person["job"] = "Engineer"

print(person)

person1 = {}

person1["name"] = "Bob"
person1["age"] = 31
person1["city"] = "New York"

print(person1)


for item in person.items():
    print(item)
    print(type)