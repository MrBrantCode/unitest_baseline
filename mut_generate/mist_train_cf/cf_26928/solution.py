"""
QUESTION:
Implement a function named `parse_gnucash_xml` that takes a GnuCash XML file as input and returns a list of transactions. Each transaction should be represented as a list containing the transaction date, description, account name, and amount. The function should be able to handle various GnuCash file structures and produce well-formatted output regardless of the complexity of the input data.

The XML file is expected to contain information about accounts and transactions, with account names stored in the 'act:name' element and transaction details stored in 'trn:date-posted/ts:date', 'trn:description', and 'split:value/commodity:quantity' elements. The function should extract this information and return it in a tabular format suitable for CSV export.

The output list should include the transaction date, description, account name, and amount for each transaction, with account names matched to their corresponding IDs. The function should be flexible, efficient, and well-documented to ensure that it can be easily maintained and extended in the future.
"""

import xml.etree.ElementTree as ET

def parse_gnucash_xml(input_file):
    """
    Parse a GnuCash XML file and return a list of transactions.
    
    Each transaction is represented as a list containing the transaction date, 
    description, account name, and amount.
    
    Parameters:
    input_file (str): The path to the GnuCash XML file.
    
    Returns:
    list: A list of transactions.
    """
    
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    # Define the namespaces for the GnuCash XML elements
    namespaces = {
        'gnc': 'http://www.gnucash.org/XML/gnc',
        'act': 'http://www.gnucash.org/XML/act',
        'trn': 'http://www.gnucash.org/XML/trn',
        'ts': 'http://www.gnucash.org/XML/ts',
        'split': 'http://www.gnucash.org/XML/split',
        'commodity': 'http://www.gnucash.org/XML/commodity'
    }
    
    # Create a dictionary to store the account names with their IDs
    accounts = {}
    
    # Iterate over all account elements in the XML file
    for account in root.findall('.//gnc:account', namespaces=namespaces):
        account_id = account.find('act:id', namespaces=namespaces).text
        account_name = account.find('act:name', namespaces=namespaces).text
        accounts[account_id] = account_name
    
    # Create a list to store the transactions
    transactions = []
    
    # Iterate over all transaction elements in the XML file
    for transaction in root.findall('.//gnc:transaction', namespaces=namespaces):
        trn_date = transaction.find('trn:date-posted/ts:date', namespaces=namespaces).text
        trn_desc = transaction.find('trn:description', namespaces=namespaces).text
        splits = transaction.findall('trn:splits/trn:split', namespaces=namespaces)
        
        # Iterate over all split elements within the transaction
        for split in splits:
            split_acct = split.find('split:account', namespaces=namespaces).text
            split_val = split.find('split:value/commodity:quantity', namespaces=namespaces).text
            transactions.append([trn_date, trn_desc, accounts[split_acct], split_val])
    
    return transactions