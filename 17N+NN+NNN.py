n=int(input(" enter the no  : "))
s=str(n)
s1=(s,s+s,s+s+s)
v=0
for x in s1:
    v=int(x)+v
print(v)
