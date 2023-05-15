from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
class CheckingAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
class BusinessAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


def main():
    checking = CheckingAccount()
    savings = SavingsAccount()
    business = BusinessAccount()
    
    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            account_type = input("Enter account type (checking, savings, or business): ")
            if account_type == "checking":
                print("Checking account balance: $", checking.balance)
            elif account_type == "savings":
                print("Savings account balance: $", savings.balance)
            elif account_type == "business":
                print("Business account balance: $", business.balance)
            else:
                print("Invalid account type")
        elif choice == 2:
            account_type = input("Enter account type (checking, savings, or business): ")
            amount = float(input("Enter amount to deposit: "))
            if account_type == "checking":
                checking.deposit(amount)
            elif account_type == "savings":
                savings.deposit(amount)
            elif account_type == "business":
                business.deposit(amount)
            else:
                print("Invalid account type")
        elif choice == 3:
            account_type = input("Enter account type (checking, savings, or business): ")
            amount = float(input("Enter amount to withdraw: "))
            if account_type == "checking":
                checking.withdraw(amount)
            elif account_type == "savings":
                savings.withdraw(amount)
            elif account_type == "business":
                business.withdraw(amount)
            else:
                print("Invalid account type")
        elif choice == 4:
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()