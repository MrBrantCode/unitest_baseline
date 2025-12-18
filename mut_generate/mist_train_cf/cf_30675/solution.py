"""
QUESTION:
Implement a function `process_transactions(transactions)` that takes a list of dictionaries as input, where each dictionary represents a payment transaction with keys 'payer', 'iban', 'bic', 'id', and 'amount', and returns a dictionary containing the aggregated information of the transactions, including total number of transactions, total amount of all transactions, list of unique payers, list of unique IBANs, list of unique BICs, and list of unique transaction IDs.

Each transaction dictionary has the following structure:
- 'payer': the name of the payer in the format "Last, First Last"
- 'iban': the International Bank Account Number (IBAN) of the payer
- 'bic': the Bank Identifier Code (BIC) of the payer's bank
- 'id': a comma-separated string of unique identifiers for the transaction
- 'amount': the amount of the transaction as a Decimal object

The function should return the aggregated information in the following format:
- 'total_transactions': the total number of transactions
- 'total_amount': the total amount of all transactions as a Decimal object
- 'unique_payers': a list of unique payer names
- 'unique_iban': a list of unique IBANs
- 'unique_bic': a list of unique BICs
- 'unique_ids': a list of unique transaction IDs
"""

from decimal import Decimal

def process_transactions(transactions):
    aggregated_info = {
        'total_transactions': len(transactions),
        'total_amount': sum(transaction['amount'] for transaction in transactions),
        'unique_payers': list(set(transaction['payer'] for transaction in transactions)),
        'unique_iban': list(set(transaction['iban'] for transaction in transactions)),
        'unique_bic': list(set(transaction['bic'] for transaction in transactions)),
        'unique_ids': list(set(id.strip() for transaction in transactions for id in transaction['id'].split(',')))
    }
    return aggregated_info