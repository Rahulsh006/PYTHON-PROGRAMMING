yr=int(input("enter the year "))
cy=2022
for i in range(cy,yr+1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) :
        print(i," is a leap year ")
