class rectangle:

	def __init__(self,l,b):
		self.length=l
		self.breadth=b

	def area(self):
		return self.length*self.breadth

	def perimeter(self):
		return 2*(self.length+self.breadth)

n1,n2=list(map(int,input("enter the length and breadth of rectangle:").split()))

r1=rectangle(n1,n2)

n3,n4=list(map(int,input("enter the length and breadth of rectangle:").split()))

r2=rectangle(n3,n4)

a1=r1.area()
a2=r2.area()

if a1<a2:
	print("area of object 2 is greater than  object 1")
elif a1==a2:
	print("area of object 1 is equal to object 2")
else:
	print("area of object 1 is greater than object 2")



		
