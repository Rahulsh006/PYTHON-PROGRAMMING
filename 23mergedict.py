
dict1 = {3: "three", 2: "two", 4: "four", 1: "one"}

dict2= {'a': 'apple', 'b':'bat','c':'cat','d':'dog','e':'egg' }

print("dict1 : ",dict1)

print("dict2 : ",dict2)

dict2.update(dict1) #we can also use d3={**dict1,**dict2} or d3 = dict1 | dict2

print("after merging ",dict2)





