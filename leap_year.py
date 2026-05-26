y=int(input("enter a year "))
if (y%400==0) or (y%4==0 and y%100!=0):
    print("the year ",y,"is a leap year")
else:
    print("the year ",y,"is not a leap year")