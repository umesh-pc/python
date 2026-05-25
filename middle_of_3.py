a=int(input("enter a number "))
b=int(input("enter another number "))
c=int(input("enter another number "))
print("the middle number is :",a if (a>b and a<c) or (a<b and a>c) else b if (b>a and b<c) or (b<a and b>c) else c) 