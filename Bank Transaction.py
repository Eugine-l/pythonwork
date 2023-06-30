import datetime
#create a class BankAccount
class BankAccount:
    def _init_(self, account_number, account_balance, customer_name):
        #input the attributes provided
        #assign the parameter passed to the attribute of the current instance self
        self.account_number = account_number
        self.account_balance = account_balance
        self.date_of_opening = datetime.date.today()
        self.customer_name = customer_name

    def deposit(self, amount):#this method is responsible for depositing an amount into the bank
        self.account_balance += amount#here the balance of the account is increased by adding the deposit
        return amount#shows final amount

    def withdraw(self, amount):#this method is responsible for withdrawing an amount from the bank
        if self.account_balance < amount:#checks if balance is less than amount withdrawn and if so returns insufficient balance
            return "Insufficient balance"
        else:
            self.account_balance -= amount
            return amount

    def check_balance(self):#method used to check current balance
        print("Current balance:", self.account_balance)

    def customer_details(self):#this method is responsible for printing the customer's details
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Current balance:", self.account_balance)

# Creating an instance of the BankAccount class
account_number = input("Enter your account number:\n ")
customer_name = input("Enter your name: \n")
account_balance = float(input("Enter your bank balance: \n"))

account = BankAccount(account_number, account_balance, customer_name)
#use the instance 'account' to call the methods; deposit,withdraw,check_balance,customer_balance

# Depositing amount and printing the returned value
deposited_amount = float(input("Enter the amount to deposit:\n "))
print("Amount Deposited:", account.deposit(deposited_amount))

# Withdrawing amount and printing the returned value
withdrawn_amount = float(input("Enter the amount to withdraw:\n "))
print("Amount Withdrawn:", account.withdraw(withdrawn_amount))

# Checking the balance
account.check_balance()

# Printing customer details
account.customer_details()