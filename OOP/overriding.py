class Animal:
    def speak(self):
        return "Some generic sound"
#method overrriding
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Instantiate the classes
generic_animal = Animal()
dog = Dog()

# Calling methods
print(generic_animal.speak()) 
print(dog.speak()) 