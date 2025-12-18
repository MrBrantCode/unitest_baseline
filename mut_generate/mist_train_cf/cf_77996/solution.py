"""
QUESTION:
Create a function `invalid_transactions(transactions)` that takes a list of strings `transactions` as input, where each string represents a transaction in the format `"{name},{time},{amount},{city}".` The function should return a list of potentially invalid transactions, where a transaction is deemed potentially invalid if its amount exceeds `$1000` or if it takes place within (and inclusive of) `60` minutes of another transaction involving the same individual but in a different city. The length of `transactions` is less than or equal to `1000`.
"""

def invalid_transactions(transactions):
    transactions_list = [t.split(',') for t in transactions]
    invalid_transactions = set()
    
    for transaction in transactions_list:
        is_valid = True
        if int(transaction[2]) > 1000: 
            is_valid = False
        else:
            for other_transaction in transactions_list:
                if (transaction[0] == other_transaction[0] and 
                    transaction[3] != other_transaction[3] and 
                    abs(int(transaction[1]) - int(other_transaction[1])) <= 60):
                        
                    is_valid = False
                    invalid_transactions.add(','.join(other_transaction))
                    
        if not is_valid:
            invalid_transactions.add(','.join(transaction))
            
    return list(invalid_transactions)