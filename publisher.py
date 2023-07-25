class publisher:
	def __init__(self,name):
		self.name=name

class book(publisher):

	def __init__(self,title,author,name):
		super().__init__(name)
		self.title=title
		self.author=author

	def printf(self):
		print("book details => ",self.title,self.author)

class python(book):

	def __init__(self,name,title,author,price,pages):
		super().__init__(title,author,name)
		self.price=price
		self.pages=pages
		
	def printf(self):
		print("book details => ",self.name,self.title,self.author,self.price,self.pages)
		
pub=python("python3 publisher ","Introduction to python","james","2000","5000")	
pub.printf()
