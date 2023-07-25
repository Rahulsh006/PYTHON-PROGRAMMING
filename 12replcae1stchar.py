l=input(" enter the string : ")
a=l[0]
b=l[1:]
for x in l:
    if l.count(a)>0:
        l1=a+b.replace(a,"$")
print(l1)
