from django.shortcuts import render, redirect
from webpage.forms import rform
from webpage.forms import lform
from django.http import HttpResponse
from webpage.models import Person, Products
from django.contrib.auth import authenticate, login, logout
# Create your views here.
authen = 0
mydata = 0
pdata = Products.objects.all()
def homepage(request):
    return render(request,"index.html",{'authen':authen,'data':mydata})
def test(request):
    regform = rform()
    return render(request,"registerform.html",{'form':rform})

def register(request):
    print(request.POST['upassword'])
    print(request.POST['urepassword'])
    if request.POST['upassword']==request.POST['urepassword']:
        form = rform(request.POST)
        if form.is_valid():
            Usern = Person(fname=request.POST['fname'],lname=request.POST['lname'],username=request.POST['uname'],password=request.POST['upassword'],email=request.POST['email'])
            Usern.save()
            return HttpResponse("User created.")
        else:
            return HttpResponse("ERROR")
    else:
        return HttpResponse("Password Not match...")

def loggin(request):
    loginform = lform()
    return render(request,"loginform.html")
def lpage(request):
    flag = 0
    getdata = 0
    data = Person.objects.all()
    for i in data:
        if i.username == request.POST['uname'] and i.password == request.POST['upassword']:
            getdata = i
            flag = 1
            break
        else:
            flag = 0
    if flag==0:
        return HttpResponse("User doesn't exist")
    else:
        global authen
        authen = 1
        global mydata
        mydata = getdata
        return redirect("/home/")
def loggout(request):
    global authen
    authen = 0
    global data
    data = 0
    return redirect("/")
finalitems = '0'
def buy(request, productid):
    global authen
    global mydata
    global finalitems
    selecteditem = 0
    count = 0
    global pdata
    for i in pdata:
        if i.id == productid:
            selecteditem = i.id
            count = 1
            break
        else:
            count = 0
    if count == 1:
        if authen == 1:
            mydata.orders = str(mydata.orders) + ' ' + str(selecteditem) + ' '
            mydata.save()
            finalitems = mydata.orders.split()
            return render(request,"buy.html",{'items':finalitems,'authen':authen,'productdata':pdata})
        else:
            return HttpResponse("<h1>Please login first.</h1>")
    else:
        return HttpResponse("Product not found")
def cart(request):
    global authen
    global mydata
    global finalitems
    count = 1
    if count == 1:
        if authen == 1:
            finalitems = mydata.orders.split() 
            return render(request,"buy.html",{'items':finalitems,'authen':authen,'productdata':pdata})
        else:
            return HttpResponse("<h1>Please login first.</h1>")
    else:
        return HttpResponse("Product not found")

def cancel(request):
    global finalitems
    global mydata
    global pdata
    savestr = ''
    finalitems = finalitems[0:len(finalitems)-1]
    for i in finalitems:
        savestr += str(i)+' '
    if len(finalitems) == 0:
        mydata.orders = ''
        finalitems = ''
    mydata.orders = str(savestr)
    mydata.save()
    return render(request,"buy.html",{'items':finalitems,'authen':authen,'productdata':pdata})