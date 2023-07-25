a=int(input("enter the number "))
if a<0:
    print("factorial not defined ")
elif a==0:
    print("factorial  = 1")
else:
    f=1
    for i in range(1,a+1):
        f=f*i
    print("factorial = ",f)
