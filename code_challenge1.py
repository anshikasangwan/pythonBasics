def func(rg):
    if rg<7000:
        print("Aheem,can you rethink this number please?")
    elif rg>10000:
        print("Wow sis!You are a queen")
    else:
        print("Cool,thanks sis! {} rupees will certainly help".format(rg))
    return

rupee=int(input("sis gave the rupee :Rs "))
func(rupee)
