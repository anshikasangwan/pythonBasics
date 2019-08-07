class Employee:
    def __init__(self):
        self.name="kiran"
        self.salary=10000
    def __str__(self):
        return "Name "+self.name+" Salary "+str(self.salary)
e=Employee()
print(e)
