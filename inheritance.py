class Quadilateral:
    def __init__(self,a,b,c,d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d
    def perimeter(self):
        p=self.side1+self.side2+self.side3+self.side4
        print("Perimeter : ",p)
class Rectange(Quadilateral):
    def __init__(self,a,b):
        super().__init__(a,b,c=None,d=None)
        self.side3=a
        self.side4=b

