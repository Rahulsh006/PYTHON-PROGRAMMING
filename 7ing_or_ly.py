s=input(" enter the string ")
e=s[-3:]
if e!="ing":
    s=s+"ing"
else:
    s=s+"ly"
print(s)
