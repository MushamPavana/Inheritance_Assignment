##Single inheritance 

##whatever we declare inside the parent class variables,methods, constructer will be by default available to the child class

class Vehicle:
    def __init__(self):
        self.brand = "Toyota"

    def m1(self):
        print("This is Toyota")

class Car(Vehicle):
    def m2(self):
        self.car_type = "four-wheeler"
        print("This is a Toyota and it is a four-wheeler")
              
c = Car()
c.m1()  
c.m2()  
 
   

