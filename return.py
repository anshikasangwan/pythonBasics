def food(f):
    tip=0.1*f
    f=f+tip
    fperson=f/num
    #return fperson
def movie(m):
    #return m/num
    
num=int(input("no. of friend: "))
ftotal=int(input("spend on food "))
mtotal=int(input("spend on movie "))
f=food(ftotal)
m=movie(mtotal)
print("total per person :",f+m)
