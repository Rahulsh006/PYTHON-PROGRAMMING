s=input("enter the sentence  : ")
l=list(s.split())
l1=set(["count of "+x+" : "+str(l.count(x)) for x in l ])
for x in l1:
    print(x)
