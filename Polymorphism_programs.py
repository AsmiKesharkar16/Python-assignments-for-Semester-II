#Method Overloading
class calc:
    def add(self,a=0,b=0,c=0):
        return a+b+c
    
c=calc()
print("-------------------------------------------")
print(c.add(10))
print(c.add(10,30))
print(c.add(10,20,30))
print("-------------------------------------------")

#Method Overriding
class vehicle:
    def move(self):
        print("Vehicle is moving")

class car(vehicle):
    def move(self):
        print("Driving on the road")

class cycle(vehicle):
    def move(self):
        print("Pedalling on the road")
        print("-------------------------------------------")

c=car()
c1=cycle()
c.move()
c1.move()

#Operator overloading

class Box:
    def __init__(self,weight):
        self.weight=weight

    def __add__(self,other):
        return self.weight+other.weight
    
b1=Box(500)
b2=Box(200)
print(b1+b2)
print("-------------------------------------------")
