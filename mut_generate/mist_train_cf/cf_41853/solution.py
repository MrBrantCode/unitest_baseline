"""
QUESTION:
Write a function `process_json_data(js)` that takes a JSON object `js` as input and returns a dictionary containing processed data. The JSON object `js` contains three keys: `Data_fundInfo`, `Data_fluctuationScale`, and `Data_holderStructure`. The function should return a dictionary with three keys: `fund_info`, `fluctuation_scale_asset`, and `holder_structure_data`.

The `fund_info` key should contain a list of tuples, where each tuple consists of fund ID, date (in the format 'YYYY-MM-DD'), and a floating-point number. The date should be converted from the input format 'YYYYMMDD' to 'YYYY-MM-DD'.

The `fluctuation_scale_asset` key should contain a dictionary with categories as keys and scaled asset values (scaled by a factor of 8) as values.

The `holder_structure_data` key should contain a dictionary with categories as keys and a list of corresponding data values.

The input JSON object `js` has the following structure:
- `Data_fundInfo`: A list of tuples containing fund ID, date, and a floating-point number.
- `Data_fluctuationScale`: A dictionary with 'categories' and 'series' keys.
- `Data_holderStructure`: A dictionary with 'categories' and 'series' keys.
"""

from datetime import datetime

def process_json_data(js: dict) -> dict:
    fund_info = [(fund[0], datetime.strptime(fund[1], '%Y%m%d').strftime('%Y-%m-%d'), fund[2]) for fund in js['Data_fundInfo']]
    
    fluctuation_scale_asset = {k: int(row['y'] * 8) for k, row in zip(js['Data_fluctuationScale']['categories'], js['Data_fluctuationScale']['series'])}
    
    holder_structure_data = {k: list(val) for k, val in zip(js['Data_holderStructure']['categories'], zip(*(r['data'] for r in js['Data_holderStructure']['series'])))}
    
    return {
        'fund_info': fund_info,
        'fluctuation_scale_asset': fluctuation_scale_asset,
        'holder_structure_data': holder_structure_data
    }