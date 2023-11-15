##Multiple inheritance :- inheriting from multiple class to single class at a Time.

class Grandparent:
    def m1(self):
        self.grandfather = "Rukhmanbhai"
        print("Grandparent class")

class Parent:
    def m2(self):
        self.father = "Umesh"
        print("Parent class")

class Child(Grandparent, Parent):
    def m3(self):
        self.child = "Pavana"

    def display(self):
        print("My grandfather's name:", self.grandfather)
        print("My father's name:", self.father)
        print("My name:", self.child)

c = Child()
c.m1()
c.m2()
c.m3()
c.display()
