"""
QUESTION:
Implement the `process_data` method in the `DataProcessor` class to perform the specified operation on the `data` attribute, which contains a collection of elements. The method should take an `operation` parameter and support the following operations: 'sum', 'product', 'maximum', 'minimum', and 'average'. If the operation is not supported, return an error message.
"""

def process_data(data, operation):
    if operation == 'sum':
        return sum(data)
    elif operation == 'product':
        result = 1
        for num in data:
            result *= num
        return result
    elif operation == 'maximum':
        return max(data)
    elif operation == 'minimum':
        return min(data)
    elif operation == 'average':
        return sum(data) / len(data)
    else:
        return "Invalid operation"