"""
QUESTION:
Create a function `classifyObject` that takes an object with attributes 'shape', 'color', and 'size' as input and returns a string classifying the object. The classification rules are as follows: 
- If the object is round, return 'object is round'. 
- If the object is not round but red, return 'object is red'. 
- If the object is neither round nor red but its size is less than or equal to 8, return 'object is small'. 
- Otherwise, return 'object is large'.
"""

def classify_object(obj):
    if obj['shape'] == 'round':
        return 'object is round'
    elif obj['color'] == 'red':
        return 'object is red'
    elif obj['size'] <= 8:
        return 'object is small'
    else:
        return 'object is large'