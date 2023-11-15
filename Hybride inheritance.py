##Hydride inheritance :- combination of more than one type of inheitance

class Person:
    def m1(self):
        self.name = "Pavana"

class Address(Person):
    def m2(self):
        super().m1()
        self.address = "Hyderabad"

class Job(Address):
    def m3(self):
        super().m2()
        self.job = "Software Engineer"
        print("Name:", self.name)
        print("Address:", self.address)
        print("Job:", self.job)

job_instance = Job()
job_instance.m3()
