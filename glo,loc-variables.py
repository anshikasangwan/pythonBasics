age=7
def a():
    print("global var 'age': ",globals()['age'])
    globals()['age']=27
    print("global var after modify: ",globals()['age'])
    age=11
    print("local var: ",age)
    return
a()
print("chechking global var OTSIDE function :",age)
