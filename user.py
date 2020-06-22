class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"Hey I'm {self.name}"

user1 = User("david",32)

print(user1.speak())