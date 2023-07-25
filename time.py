class time:

	def __init__(self,h,m,s):
		self.__s = s
		self.__m = m
		self.__h = h

	def __add__(self,oth):
		h1= self.__h +oth.__h + (self.__m + oth.__m+ (self.__s+ oth.__s) // 60) // 60
		m1= (self.__m + oth.__m +(self.__s+ oth.__s)//60)%60
		s1= (self.__s + oth.__s) % 60
		
		print(" total time  : %d : %d : %d  "%(h1,m1,s1))

r1= time(5,55,30)
r2= time(7,55,45)

r1+r2

