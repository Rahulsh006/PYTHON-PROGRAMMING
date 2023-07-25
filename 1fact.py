n=int(input(" enter the no to find the factorial "))
if n==0 or n==1:
    print("fact = 1")
elif n<0:
    print(" fact not defined ")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    print("fact = ",f)
