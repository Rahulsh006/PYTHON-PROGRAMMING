l=list(input(" enter the list of first name : ").split())
res =[i for x in l for i in x if i=='a']
print(res,"count = ",len(res))
