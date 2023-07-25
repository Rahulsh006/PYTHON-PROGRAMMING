class bank:

	def __init__(self,an,na,at,b):
		self.acno=an
		self.name=name
		self.acty=ty
		self.bal=b

	def deposit(self):
		amount=int(input("enter amount to deposit "))
		self.bal=self.bal+amount

	def withdraw(self):
		amount=int(input("enter the withdraw amount: "))
		if(amount>self.bal):
			print("balance is not sufficient ")
		else:
			self.bal = self.bal - amount

	def checkbalance(self):
		print("a/c balance:",self.bal)

name=input("enter name of a/c holder: ")
an=input("Enter a/c no: ")
ty=input("enter a/c type: ")
b=int(input("enter balance: "))

ac1=bank(name,an,ty,b)

print("1.Deposit\n 2.Withdraw \n 3.check balance \n")

while(True):
	choice=int(input("enter options: "))
	if choice == 1:
		ac1.deposit()
	elif choice == 2:
		ac1.withdraw()
	elif choice == 3:
		ac1.checkbalance()
	else:
		print("enter the correct choice ")
