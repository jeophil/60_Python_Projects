# polymorphism allows to use parent class functions as if its own

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age  
    pass
    def work(self):
        print("working....")

class SoftwareEngg(Employee):
    def __init__(self, name, age,level):
        #super takes attributes from parent class
        super().__init__(name, age) 
        self.level = level

    # Overides parent class work function
    # def work(self):
    #     print("working....from SE desk")
    def work(self):
        print("I'm a SDE and my level is ",self.level)    
    pass

class Designer(Employee):
    pass

# all the attributes and functions are inherited by child class

Employees = [SoftwareEngg("philip",56,1),SoftwareEngg("peter",55,2)]


def HR_motivate(Employees):
    for employee in Employees:
        employee.work()

HR_motivate(Employees)