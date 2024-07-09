class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming fast!"

class Duck(Flyer, Swimmer):
    pass

# Instantiate the Duck class
duck = Duck()

# Calling methods
print(duck.fly())  
print(duck.swim())  