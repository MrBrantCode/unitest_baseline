"""
QUESTION:
Implement a `BankAccount` class with the following methods: `__init__(self, initial_balance)`, `deposit(self, amount)`, `withdraw(self, amount)`, `get_balance(self)`, and `transaction_history(self)`. The class should maintain a record of transactions and update the balance accordingly. The `transaction_history` method should return a list of strings in the format "Transaction: [deposit/withdraw] of [amount]". Ensure that the `withdraw` method checks for sufficient funds before processing the transaction.
"""

def BankAccount(initial_balance):
    balance = initial_balance
    transactions = []

    def deposit(amount):
        nonlocal balance
        balance += amount
        transactions.append(f"Transaction: deposit of {amount}")

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            transactions.append(f"Transaction: withdraw of {amount}")
        else:
            print("Insufficient funds")

    def get_balance():
        return balance

    def transaction_history():
        return transactions

    def entance(amount, action):
        if action == 'deposit':
            deposit(amount)
        elif action == 'withdraw':
            withdraw(amount)
        else:
            print("Invalid action")

    return entance

# usage
account = BankAccount(100)
account(50, 'deposit')
account(20, 'withdraw')
print(account(0, 'withdraw')) # Should print: None
account(20, 'withdraw') # Should print: Insufficient funds