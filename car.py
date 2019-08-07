class car:
    def __init__(self,a=40):
        self.speed=a
    def get_speed(self):
        return self.speed
    def set_speed(self,a):
        if a<=0 or a>=160:
            print("speed needs to be between 0 and 160")
        else:
            self.speed=a
    speed = property(get_speed,set_speed)
    
