"""
QUESTION:
Implement the `parse_unspent_response` method for the `ElectrumAPI` class. The method should take a JSON response from the Electrum blockchain API as input and return a list of unspent transaction outputs (UTXOs) in the following format:
```
[
    {
        "tx_hash": "transaction_hash_1",
        "output_index": 0,
        "value": 100000000
    },
    {
        "tx_hash": "transaction_hash_2",
        "output_index": 1,
        "value": 50000000
    },
    ...
]
```
Assume that the input JSON response contains a key 'result' with a list of UTXOs, where each UTXO is a dictionary containing keys 'tx_hash', 'output_n', and 'value'.
"""

def parse_unspent_response(response):
    unspent_outputs = []
    for utxo in response['result']:
        unspent_outputs.append({
            "tx_hash": utxo['tx_hash'],
            "output_index": utxo['vout'] if 'vout' in utxo else utxo['output_n'],
            "value": utxo['value']
        })
    return unspent_outputs