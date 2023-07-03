class animal:
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def speak(self):

        raise NotImplementedError("child classes must implement this method")
class Dog(animal):
    def speak(self):
        return "woof!"
class Cat(animal):
    def speak(self):
        return "meows"
class Cow(animal):
    def speak(self):
        return "moows"


#create an object
dog=Dog("Tom","black and white")
print(dog.name)
print(dog.speak())
print(dog.color)
cat=Cat("c`namon","brown")
print(cat.name)
print(cat.color)
print(cat.speak())
cow=Cow("jersey","grey")
print(cow.name)
print(cow.color)
print(cow.speak())




