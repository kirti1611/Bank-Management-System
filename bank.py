import mysql.connector
mydb=mysql.connector.connect(user='root',
							passwd='root',
							host='localhost',
							auth_plugin='mysql_native_password',
							database='Bankdbq'
							)
mycursor=mydb.cursor(buffered=True)
def mainMenu():
	print("*"*140)
	print("MAIN MENU".center(140))
	print("1. Account excutive/Customer".center(140))
	print("2. Cashier/Teller".center(140))
	print("3. Exit".center(140))

def Menu(): #Function to display the menu
	print("*"*140)
	print("MAIN MENU".center(140))
	print("1. Insert Record/Records".center(140))
	print("2. Display Records as per Account Number".center(140))
	print("3. Search Record Details as per the account number".center(140))
	print("4. Update Record".center(140))
	print("5. Delete Record".center(140))
	print("6. Exit".center(140))
	print("*"*140)


def MenuTransaction():
	print("TransactionsDebit/Withdraw from the account".center(140))
	print(" a. Debit/Withdraw from the account".center(140))
	print(" b. Credit into the account".center(140))
	print(" c. Display Balance details".center(140))
	print(" d. Back".center(140))


def Insert():
	while True: #Loop for accepting records
		Acc=input("Enter account no: ")
		Name=input("Enter Name: ")
		Age=input("Enter Age: ")
		Add=input("Enter Address: ")
		City=input("Enter City: ")
		State=input("Enter State: ")
		#Bal=float(input("Enter Balance"))
		Rec=[Acc,Name.upper(),Age,Add.upper(),City.upper(),State.upper()]
		Cmd="insert into bank values(%s,%s,%s,%s,%s,%s)"
		mycursor.execute(Cmd,Rec)
		mydb.commit()
		print("Customer creation initiated successfully")
		ch=input("Do you want to enter more records: ")
		if ch=='N' or ch=='n':
			break

def DispSortAcc(): #Function to Display records as per ascending order of Account Number
	try:
		cmd="select * from BANK order by ACCNO"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		F="%15s %15s %15s %15s %15s %15s"
		print(F % ("ACCNO","NAME","AGE","COMPLETE ADDRESS","CITY","STATE"))
		print("="*125)
		for i in S:
			for j in i:
				print("%14s" % j, end=' ')
			print()
		print("="*125)
	except:
		print("Table doesn't exist")

def DispSearchAcc(): #Function to Search for the Record from the File with respect to the account number
	try:
		cmd="select * from BANK"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		ch=input("Enter the accountno to be searched: ")
		for i in S:
			if i[0]==ch:
				print("="*125)
				F="%15s %15s %15s %15s %15s %15s"
				print(F % ("ACCNO","NAME","AGE","COMPLETE ADDRESS","CITY","STATE"))
				print("="*125)
				for j in i:
					print('%14s' % j,end=' ')
				print()
				break
		else:
			print("Record Not found")
	except:
		print("Table doesn't exist")

def Update(): #Function to change the details of a customer
	try:
		cmd="select * from BANK"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		A=input("Enter the accound no whose details to be changed: ")
		for i in S:
			i=list(i)
			if i[0]==A:
				ch=input("Change Name(Y/N): ")
				if ch=='y' or ch=='Y':
					i[1]=input("Enter Name: ")
					i[1]=i[1].upper()

				ch=input("Change Age(Y/N): ")
				if ch=='y' or ch=='Y':
					i[2]=input("Enter Age: ")

				ch=input("Change Address(Y/N): ")
				if ch=='y' or ch=='Y':
					i[3]=input("Enter Address: ")
					i[3]=i[3].upper()

				ch=input("Change city(Y/N): ")
				if ch=='y' or ch=='Y':
					i[4]=input("Enter City: ")
					i[4]=i[4].upper()

				ch=input("Change State(Y/N): ")
				if ch=='y' or ch=='Y':
					i[5]=input("Enter State: ")
					i[5]=i[5].upper()

				

				cmd="UPDATE BANK SET NAME=%s,AGE=%s,ADDRESS=%s,CITY=%s,STATE=%s WHERE ACCNO=%s"
				val=(i[1],i[2],i[3],i[4],i[5],i[0])
				mycursor.execute(cmd,val)
				mydb.commit()
				print("Customer updation initiated successfully")
				break
		else:
			print("Record not found")
	except:
		print("No such table")

def Delete(): #Function to delete the details of a customer
	try:
		cmd="select * from BANK"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		A=input("Enter the account no to be deleted: ")
		for i in S:
			i=list(i)
			if i[0]==A:
				cmd="delete from bank where accno=%s"
				val=(i[0],)
				mycursor.execute(cmd,val)
				mydb.commit()
				print("Customer deletion initiated successfully")
				break
		else:
			print("Record not found")
	except:
		print("No such Table")

def Withdraw(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
	#try:
		cmd="select * from balance"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		print("Please Note that the money can only be debited if min balance of Rs 2000 exists")
		acc=input("Enter the account no from which the money is to be withdrawn: ")
		for i in S:
			i=list(i)
			if i[0]==acc:
				Amt=float(input("Enter the amount to be withdrawn: "))
				if i[1]-Amt>=2000:
					i[1]-=Amt
					cmd="UPDATE Balance SET BALANCE=%s WHERE ACCNO=%s"
					val=(i[1],i[0])
					mycursor.execute(cmd,val)
					mydb.commit()
					print("Amount withdrawn successfully")
					break
				else:
					print("There must be min balance of Rs 2000")
					break
		else:
			print("Record Not found")
	#except:
		#print("Table Doesn't exist")

def Deposit(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
	try:
		cmd="select * from balance"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		acc=input("Enter the account no from which the money is to be debited: ")
		for i in S:
			i=list(i)
			if i[0]==acc:
				Amt=float(input("Enter the amount to be deposited: "))
				i[1]+=Amt
				cmd="UPDATE balance SET BALANCE=%s WHERE ACCNO=%s"
				val=(i[1],i[0])
				mycursor.execute(cmd,val)
				mydb.commit()
				print("Amount deposited successfully")
				break
		else:
			print("Record Not found")
	except:
		print("Table Doesn't exist")

def Display(): #Function to Display records as per ascending order of Account Number
	try:
		cmd="select * from balance order by ACCNO"
		mycursor.execute(cmd)
		S=mycursor.fetchall()
		F="%15s %15s"
		print(F % ("ACCNO","BALANCE"))
		print("="*125)
		for i in S:
			for j in i:
				print("%14s" % j, end=' ')
			print()
		print("="*125)
	except:
		print("Table doesn't exist")

while True:
	mainMenu()
	ch=input("Enter your Choice: ")
	if ch=="1":
		while True:
			Menu()
			ch=input("Enter your Choice: ")
			if ch=="1":
				Insert()
			elif ch=="2":
				DispSortAcc()
			elif ch=="3":
				DispSearchAcc()
			elif ch=="4":
				Update()
			elif ch=="5":
				Delete()
			elif ch=="6":
				print("Exiting...")
				break
			else:
				print("Invalid choice")
	

	elif ch=="2":
		while True:
			MenuTransaction()
			ch1=input("Enter choice a/b/c: ")
			if ch1 in ['a','A']:
				Withdraw()
			elif ch1 in ['b','B']:
				Deposit()
			elif ch1 in ['c','C']:
				Display()
			elif ch1 in ['d','D']:
				print("Back to the main menu")
				break
			else:
				print("Invalid choice")

	elif ch=="3":
			print("Exiting...")
			break
	
	else:
		print("Wrong Choice Entered")

	


