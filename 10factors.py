n=int(input("enter the number "))
for i in range(1,n+1):
    if n%i==0:
        print("{f} is a factor".format(f=i))
