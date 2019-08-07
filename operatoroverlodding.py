class Distance:
    def __init__(self,x,y):
        self.feet=x
        self.inches=y
    def __add__(self,other):
        final_feet=self.feet+other.feet
        final_inches=self.inches+other.inches
        if final_inches>=12:
            final_feet=final_feet+1
            final_inches=final_inches-12
        return Distance(final_feet,final_inches)
    def __str__(self):
        return "Distance: "+str(self.feet)+" feet and "+str(self.inches)+"inches"
