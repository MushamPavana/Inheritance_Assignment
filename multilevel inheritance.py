##Multilevel inheritance :- inheriting properties from multiple class to single class

class Grandma:
    def __init__(self):
        self.a = 20
        print("This is grandma constructor")

    def m1(self):
        self.b = 20

class Mother(Grandma):
    def m2(self):
        self.c = 80

class child(Mother):
    def sum(self):
        print(self.a + self.b + self.c)

c = child()
c.m1()
c.m2()
c.sum()
