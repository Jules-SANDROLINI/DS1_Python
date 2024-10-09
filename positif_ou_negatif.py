def addition_et_statut(a,b) :
    c=a+b
    if c<=0:
        print("la somme est négative ou nulle")
    else :
        print("la somme est positive")
    return
a=float(input("donner moi un nombre"))
b=float(input("donner moi un second nombre"))
addition_et_statut(a,b)