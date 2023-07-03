def mitmorning ():
    print("This is MIT morning class")
mitmorning()

def calculate():
    x=7
    y=10
    print(x*y)
    print(x+y)
    print(y/x)
calculate()

def majina(myfirstname,mylastname,age):
    print(myfirstname +" " + mylastname +" " , age)
majina("Faith","chemutai" , 23)
majina("Jael","chelangat",34)
majina("Yvonne","wangari", 96)


#[2.5,6,3,5]

def average(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average

data=[3,6,8,9,2,1,8]
result=average(data)
print("the average is",result)



