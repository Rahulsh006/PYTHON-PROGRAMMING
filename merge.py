d1={"a":1,"b":2,3:12}
print("dict 1 ",d1)

d2={"a":4,"b":5}
print("dict 2",d2)

d3 = {**d1, **d2}

for key in d3.keys():
    d3[key] = []
    
for key in d1.keys():
    d3[key].append(d1[key])
    
for key in d2.keys():
    d3[key].append(d2[key])

print(d3)
