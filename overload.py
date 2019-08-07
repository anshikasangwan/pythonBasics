class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())
class gift:
    def __init__(self,nm,prc):
        super().__init__(nm,prc)    #this code have an error
    def get_price(self):
        return self.price+product.deliveryCharge+100
