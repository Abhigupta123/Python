def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greater")
    elif(b>a and b>c):
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

greatest(a,b,c)