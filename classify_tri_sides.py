a=int(input("enter the lengthe of 1st side of the triangle"))
b=int(input("enter the lengthe of 2nd side of the triangle"))
c=int(input("enter the lengthe of 3rd side of the triangle"))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("the side can form a triangle")
    if a==b==c:
        print("the triangle is equilateral")
    elif (a==b) or (b==c) or (c==a):
        print("the triangle is isosceles")  
    elif (a!=b) and (b!=c) and (c!=a):
        print("the triangle is scalene")    
else:
    print("the sides cannot form a triangle")
    