class person:
    counter=0   #class attribute
    def __init__(self,a='ravi',b='male'):
        self.name=a
        self.gender=b  #attributes or instance variables
        person.counter=person.counter + 1
    def showInfo(self):     #instance methods or methods
        print("Name: ",self.name)
        print("Gender: ",self.gender)
    @classmethod
    def showCount(cls):
        print("Number of objects created so far ",cls.counter)
