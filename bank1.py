'''class user:
	def __init__(self,name,mob_no,address=""):
		self.name=name
		self.mobile_no=mob_no
		self.address=address'''
class BankAccount:
	def __init__(self,name,ph_no):
		self.name=name # accesing by using self .methods
		self.phone_no=ph_no
		#self.acc_no=acc_no
		self.generate_acc_no()
		self.balance=0
	
	def generate_acc_no(self):
		import uuid
		self.account_no=str(uuid.uuid4())
	
	def deposit(self,amount):
		self.balance+=amount
	
	def withdraw(self,amount):
		if amount > self.balance:
			print("Insufficient funds")
		else:
			self.balance-=amount
		
ac=BankAccount("jai","9999955555")
print(ac.name,ac.phone_no,ac.balance,ac.account_no)
#print(ac.generate_acc_no())
ac.deposit(100)
print(ac.balance)
ac.deposit(1000)
print(ac.balance)
ac.withdraw(500)
print(ac.balance)
ac.withdraw(800)
print(ac.balance)







	
