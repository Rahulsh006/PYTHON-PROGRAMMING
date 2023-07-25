def check(n):
    if n > 100:
        l.append("over")
        print(l)
    else:
        l.append(n)
        print(l)
        
l=[]
no=int(input(" enter the length of list "))
while(no>0):
    ele=int(input("enter the element "))
    check(ele)
    no-=1
    
