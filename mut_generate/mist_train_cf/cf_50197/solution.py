"""
QUESTION:
Function: terra_algorithm
The Terra algorithm is supposed to maintain the value of TerraUSD (UST) stable at approximately $1 USD. It uses two types of tokens: TerraUSD (UST) and Terra's native Luna token. The system mints and burns these tokens in response to market demand. If the value of UST goes above $1 USD, the algorithm mints more UST, increasing supply and thus lowering price. If the value of UST goes below $1 USD, the algorithm burns UST, reducing supply and raising price.

Implement a function terra_algorithm that takes in the initial prices of UST and Luna, the amount of UST to be minted or burned, and the amount of Luna to be burned or minted, and returns the updated prices of UST and Luna after the transaction.
"""

def terra_algorithm(initial_ust_price, initial_luna_price, ust_amount, luna_amount):
    # if the value of UST goes above $1 USD, the algorithm mints more UST
    if initial_ust_price > 1:
        updated_ust_price = initial_ust_price - (ust_amount / (initial_ust_price * 100))
        updated_luna_price = initial_luna_price - (luna_amount / (initial_luna_price * 100))
    
    # if the value of UST goes below $1 USD, the algorithm burns UST
    else:
        updated_ust_price = initial_ust_price + (ust_amount / (initial_ust_price * 100))
        updated_luna_price = initial_luna_price + (luna_amount / (initial_luna_price * 100))
    
    return updated_ust_price, updated_luna_price