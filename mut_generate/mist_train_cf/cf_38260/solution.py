"""
QUESTION:
Write a function `identify_fast_markets(prev_data, latest_data, config)` that takes in three parameters: `prev_data` (a list of dictionaries representing historical cryptocurrency data), `latest_data` (a dictionary representing the most recent cryptocurrency data), and `config` (a module containing the predefined threshold `FASTTICK_MIN_RATE`). 

The function should return a list of cryptocurrency names with an average percentage price change greater than or equal to `FASTTICK_MIN_RATE` between consecutive time intervals in `prev_data`.
"""

def entrance(prev_data, latest_data, config):
    fast_markets = []
    for name in latest_data:
        prev_changes = []
        for i in range(len(prev_data)-1):
            old_price = float(prev_data[i].get(name, {}).get('Summary', {}).get('Last', 0.0))
            new_price = float(prev_data[i+1].get(name, {}).get('Summary', {}).get('Last', 0.0))
            if old_price != 0:
                change = (((new_price - old_price) / old_price) * 100)
                prev_changes.append(change)
        if prev_changes:
            volume = float(latest_data.get(name, {}).get('Summary', {}).get('BaseVolume', 0.0))
            average_rate = float((sum(prev_changes) / len(prev_changes)))
            if average_rate >= config.FASTTICK_MIN_RATE:
                fast_markets.append(name)
    return fast_markets