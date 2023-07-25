n=input(" enter the string ")
c=[(x,n.count(x)) for x in n]
c=set(c)
for x,y in enumerate(c):
    print(" count of %c is %d "%(y[0],y[1]))
