class MpesaAccount:

	 def __init__(self,name,phone):
			self.name=name
			self.phone = phone
			self.balance=0
			self.deposits = []
			self.withdrawals=[]
			self.loans=[]
			self.loan=0
			

	 def check_balance(self):
	 		check_balance=self.balance
	 		return "hellow {},phone number {},your balance is Ksh.{}".format(self.name,self.phone,self.balance)

	 def deposit(self,n):
	 		deposit = n
	 		self.balance= self.balance + n
	 		self.deposits.append(n)
	 		return "Welcome {}, you have deposited Ksh.{} , your current balance is now Ksh.{}".format(self.name,n,self.balance)
	 def withdraw(self,b):
	 		withdraw = b
	 		if b >= self.balance:
	 			print("cant withdraw")
	 		else:	
	 			self.balance=self.balance - b
	 			self.withdrawals.append(b)
	 			return "Welcome {}, you have withdrew Ksh.{} , your current balance is now Ksh.{}".format(self.name,b,self.balance)			

	 def my_deposit(self):
	 		for d in self.deposits:
	 			print ("these are the deposits {}".format(d))
	 		

	 def all_withdrawal(self):
	 		for w in self.withdrawals:
	 			print("these are all the all_withdraws {}".format(w))
	 		

	 def give_loan(self,amount):
	 	self.loan=self.loan+amount
	 	self.balance=self.balance+amount
	 	if len(self.deposits) >= 5 and amount<(1/3*sum(self.deposits)) and self.loan !=0:
	 		self.loans.append(amount)
	 		self.deposits.append(amount)
	 		print("your have succesfull take a loan of Ksh{}.".format(amount))
	 		
	 	else:
	 		print("you do not qualify for a loan")


	 def all_loans(self):
	 		for l in self.loans:
	 			print("these are all loans {}".format(l))

	 def payment(self,cash):
	 	if cash < self.loan:
	 		self.loan=self.loan-cash
	 		self.balance=self.balance-cash
	 		print("you have repaid Ksh.{} your loan balance is Ksh.{}".format(cash,self.loan)) 

	 	elif cash > self.loan:
	 		extra=cash-self.loan
	 		self.balance=self.balance-self.loan
	 		self.balance=self.balance+extra
	 		print("you have repaid ksh{},loan is fully paid ,amount added to balance ksh{}".format(cash,self.balance))

	 	else:
	 		print("nothing is working gal")

	 			
