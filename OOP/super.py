class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the superclass's __init__ method
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"

# Instantiate the Dog class
dog = Dog("Buddy", "Golden Retriever")

# Calling methods
print(dog.speak())  