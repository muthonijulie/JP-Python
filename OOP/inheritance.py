class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This will be overridden in subclasses

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods
print(dog.speak()) 
print(cat.speak())