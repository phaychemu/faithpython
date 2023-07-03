class vehicles:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def color(self):
        NotImplementedError("child classes must implement this method")
class Toyota(vehicles):
    def color(self):
        return "white"
class landcruiser(vehicles):
    def color(self):
        return "black"
class volvo(vehicles):
    def color(self):
        return "grey"
#create an object
toyota=Toyota("Danish","arrow")
print(toyota.brand)
print(toyota.model)
print(toyota.color())
landcruiser=landcruiser("cruiser","round")
print(landcruiser.model)
print(landcruiser.brand)
print(landcruiser.color())
volvo=volvo("new orleans","arrow")
print(volvo.brand)
print(volvo.model)
print(volvo.color())

