
def check(n):
    for b in str(n):
        if int(b) % 2 == 0:
            pass
        else:
            return False
    return True

    
a=int(input("enter the list elements "))
l=[]
if a<1000 :
    print(" range should be more than 1000")
else:
    for i in range(1000,a,2):
        r=check(i)
        if r==True:
            rs=i**0.5
            if rs==int(rs):
                l.append(i)
                
if len(l)==0:
    print("no elements ")
else:
    print(l)

