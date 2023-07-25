l1=[1,5,-9,6,99-32,-56,34,-2,9]
l2=[x for x in l1 if(x>0)]
print(l2)

n=int(input(" enter the number \n "))
l3=[x*x for x in range(1,n+1)]
print(l3)

s=input(" enter the string to find the vowels ")
v=['a','e','i','o','u']
[print(x) for x in s if x in v]

s1=input("enter the string to find ordinal value of each character ")
[print("ordinal value of ",x," : ",ord(x)) for x in s1]
