#lisst datastructure
 #a list enables you to change data
myclassmate=["Nelly","Joy","Shackro","Austine","susan"]
mynos=[4,9,20,3,1,50,-9]
myclassmate[0]="Danny"
mynos.sort()
myclassmate.append("Lindah")
myclassmate.insert(2,"Jael")
myclassmate.pop(0)
print(mynos)
print(myclassmate)
#for loop
for members in myclassmate:
    print(members)


    #this is a tuple


    countries=("Kenya","Uganda","Tanzania","Burundi")
    print(countries )
    for east in countries:
        print(east)


    #sets datastructures
    cars={"Toyota","Nissan","Mercedes","Subaru"}
    print(cars)
    for types in cars:
        print(types)
       # dictionaries data structure
    matunda={
        "price":50,
        "color":"yellow",
        "name":"banana"
    }
    matunda["shape"]="oval"

    print(matunda)
    utensils={
        "name":"sufuria",
        "price":500,
        "type":"aluminium"
    }
    utensils.pop("price")
    print(utensils)
    x=matunda["price"]
    print(x)
    x=matunda["color"]
    print(x)
    x=matunda["name"]
    print(x)
