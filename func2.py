def verdict(m1,m2,m3):
    total=m1+m2+m3
    if total>15000:
        print("yes")
    else:
        print("no")
    return
gift=int(input("gift money :Rs."))
saving=int(input("saving :Rs."))
internship=int(input("internship :Rs."))
verdict(gift,saving,internship)
