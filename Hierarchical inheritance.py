##Hierarchical inheritance :- inherting properties from single class to multiple class


class Parent:
    def __init__(self):
        print("This is a Parent class.")

class ChildOne(Parent):
    def m1(self):
        print("This is a ChildOne class.")

class ChildTwo(Parent):
    def m2(self):
        print("This is a ChildTwo class.")

child_one_instance = ChildOne()
child_one_instance.m1()

child_two_instance = ChildTwo()
child_two_instance.m2()
