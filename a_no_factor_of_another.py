a=int(input("enter a number"))
b=int(input("enter another number"))
if (a%b==0) or (b%a==0):
    print("one number is a factor of the other")
else:   
     print("neither number is a factor of the other")