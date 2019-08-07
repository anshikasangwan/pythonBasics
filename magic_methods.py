class Employee:
    def __new__(cls):
        print("__new__ magic method is executed")
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__ magic method is executed")
        self.name="Anshu"
        self.salary=10000
        
e1=Employee()
print(e1.name)
        
