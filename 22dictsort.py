dict1 = {3: "Jim", 2: "kack", 4: "mane", 1: "zill"}
print("dict before sotring ",dict1 )

d1=dict(sorted(dict1.items()))
print("ascendingly sorted dict using keys : ",d1 )

d2=dict(reversed(sorted(dict1.items())))
print("descendingly sorted dict using keys : ",d2)
