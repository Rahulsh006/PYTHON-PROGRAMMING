class rectangle:

	def __init__(self,l,b):
		self.length=l
		self.breadth=b

	def area(self):
		return self.length*self.breadth

	def __lt__(self,oth):
		ar1=self.area()
		ar2=oth.area()
		if ar1 < ar2 :
			print("area of object 2 is greater than  object 1")
		else:
			print("area of object 1 is greater than object 2")


n1,n2=list(map(int,input("enter the length and breadth of rectangle:").split()))

r1=rectangle(n1,n2)

n3,n4=list(map(int,input("enter the length and breadth of rectangle:").split()))

r2=rectangle(n3,n4)

r1 < r2

		
