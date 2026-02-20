import json

FILE = "data.json"

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        try:
            with open(FILE) as f:
                data = json.load(f)
        except:
            data = []

        data.append({"name": self.name, "age": self.age})

        with open(FILE, "w") as f:
            json.dump(data, f, indent=2)


name = input("Name: ")
age = input("Age: ")

u = User(name, age)
u.save()

print("Saved!")
