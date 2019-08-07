#using same name for global and local variable using build in function globals()

alpha=1
beta=2
gamma=3
print(globals())    #returns dictionary object of all global variables
#as it returns a dictionary we can change value eg- globals()['gamma']=5
