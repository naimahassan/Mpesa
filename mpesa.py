class MpesaAccount:

	 def __init__(self,name,phone,balance,):
			self.name=name
			self.phone = phone
			self.balance=balance
			

	 def check_balance(self):
	 		check_balance=self.balance
	 		return "hellow {},phone number {},your balance is Ksh.{}".format(self.name,self.phone,self.balance)

	 def deposit(self,n):
	 		deposit = n
	 		self.balance= self.balance + n
	 		return "Welcome {}, you have deposited Ksh.{} , your current balance is now Ksh.{}".format(self.name,n,self.balance)
	 def withdraw(self,b):
	 		withdraw = b
	 		self.balance=self.balance - b
	 		return "Welcome {}, you have withdrew Ksh.{} , your current balance is now Ksh.{}".format(self.name,b,self.balance)			