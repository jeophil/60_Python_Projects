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
    def work(self):
        print("working....from SE desk")
    def softwareEnggWork(self):
        print("I'm a SDE and my level is ",self.level)    
    pass

class Designer(Employee):
    pass

# all the attributes and functions are inherited by child class

se = SoftwareEngg("jeo",26,1)
se.work()
se.softwareEnggWork()