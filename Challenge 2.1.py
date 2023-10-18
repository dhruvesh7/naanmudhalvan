class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited {amount}. New balance: {self._account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew {amount}. New balance: {self._account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self._account_holder}: {self._account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount(account_number="123456789", account_holder="MSD", initial_balance=1000.0)

    # Test deposit and withdrawal
    account.display_balance()
    account.deposit(500.0)
    account.withdraw(200.0)
    account.display_balance()
