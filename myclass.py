class people:
    def __init__(self,name,age,gender):
        self.personname=name
        self.personage=age
        self.persongender=gender
    def display(self):
        print(self.personname,self.personage,self.persongender)
myobj=people("Jael",43,"Female")
myobja=people("Danny",73,"male")
myobjb=people("Cynthia",65,"Female")
myobjc=people("Erick",36,"male")
myobj.display()
myobja.display()
myobjb.display()
myobjc.display()