a=int(input("enter the lengthe of 1st side of the triangle"))
b=int(input("enter the lengthe of 2nd side of the triangle"))
c=int(input("enter the lengthe of 3rd side of the triangle"))
if (a+b>c) and (b+c>a) and (c+a>b):
    print("the side can form a triangle")
else:
    print("the sides cannot form a triangle")
    