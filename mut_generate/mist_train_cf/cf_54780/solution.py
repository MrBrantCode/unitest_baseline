"""
QUESTION:
Write a function `weighted_median` that calculates the weighted median of 'rating' values across all items in a given list of JSON objects, with the 'price' as the weight factor. The result should be rounded to two decimal places. If the input list is empty, the function should return None. Assume the input list contains JSON objects with 'product' and 'details' keys, where 'details' is another JSON object containing 'price' and 'rating' keys.
"""

def weighted_median(data):
    if not data:
        return None

    total_weight = sum(item['details']['price'] for item in data)
    values_and_weights = [(item['details']['rating'], item['details']['price'])
                          for item in data]

    values_and_weights.sort()
    
    acc_weight = 0
    half_total_weight = total_weight / 2
    for value, weight in values_and_weights:
        acc_weight += weight
        if acc_weight >= half_total_weight:
            return round(value, 2)