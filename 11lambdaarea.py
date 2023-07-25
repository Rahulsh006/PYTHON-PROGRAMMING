l=int(input(" enter the side of a square "))
ar=lambda n:n*n
print(" area of square = ",ar(l))

l,b=map(int,input(" enter the sides of a rectangle ").split())
ar=lambda l,b:l*b
print(" area of square = ",ar(l,b))

a,b,c=map(int,input(" enter 3 sides of triangle ").split())
s=(a+b+c)/2
ar=lambda s:(s*(s-a)*(s-b)*(s-c))**0.5
print(" area of square = ",ar(s))
