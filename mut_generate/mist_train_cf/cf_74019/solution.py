"""
QUESTION:
Create a function `is_nds_transaction` that identifies whether a given transaction is an NDS (Negotiated Dealing System) transaction based on the following parameters: trading platform, currency, security type, and negotiation method. The function should return `True` if the transaction meets the NDS criteria and `False` otherwise.

Restrictions: The function should only consider the following parameters:
- Trading platform: NDS
- Currency: Indian National Rupee (INR)
- Security type: Indian government securities or other securities approved by RBI
- Negotiation method: Negotiation rather than bid or offer system.
"""

def is_nds_transaction(trading_platform, currency, security_type, negotiation_method):
    """
    This function identifies whether a given transaction is an NDS transaction.

    Parameters:
    trading_platform (str): The trading platform used for the transaction.
    currency (str): The currency in which the transaction is conducted.
    security_type (str): The type of security being traded.
    negotiation_method (str): The method used to agree on the transaction terms.

    Returns:
    bool: True if the transaction is an NDS transaction, False otherwise.
    """

    # Define the approved security types
    approved_security_types = ["Indian government securities", "Other RBI approved securities"]

    # Check if the transaction meets the NDS criteria
    if (trading_platform == "NDS" and 
        currency == "INR" and 
        security_type in approved_security_types and 
        negotiation_method == "Negotiation"):
        return True
    else:
        return False