class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"
    
class Cow:
    def speak(self):
        return "mooo!" 

class Bird:
    def speak(self):
        return "chirp!"

class Horse:
    def speak(self):
        return "neigh!"    
# Polymorphism in action
for animal in [Dog(), Cat(), Cow(), Bird(), Horse()]:
    print(animal.speak())