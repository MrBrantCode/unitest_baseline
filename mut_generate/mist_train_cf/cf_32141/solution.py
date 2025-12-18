"""
QUESTION:
Create a function `create_timelock_transaction` that generates data for a time-locked transaction. The function should take in the following parameters: `message_id` (str), `oracle_fees` (float), `miners_fee_satoshi` (int), `return_address` (str), `locktime` (int), `pubkey_list` (list of str), and `req_sigs` (int). It should return a dictionary containing these input parameters and an additional key `protocol_version` with the value set to `'0.12'`.
"""

def create_timelock_transaction(message_id, oracle_fees, miners_fee_satoshi, return_address, locktime, pubkey_list, req_sigs):
    transaction_data = {
        'message_id': message_id,
        'oracle_fees': oracle_fees,
        'miners_fee_satoshi': miners_fee_satoshi,
        'return_address': return_address,
        'locktime': locktime,
        'pubkey_list': pubkey_list,
        'req_sigs': req_sigs,
        'protocol_version': '0.12'
    }
    return transaction_data