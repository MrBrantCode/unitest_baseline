"""
QUESTION:
Construct a function `mongo_query` that generates a MongoDB query to retrieve documents based on specific conditions. The query should filter documents where the field 'name' contains a specified letter and the field 'age' is greater than a specified age. The function should take two parameters: `letter` and `age`. The query should be returned as a dictionary.
"""

def mongo_query(letter, age):
    return {
        "$and": [
            {"name": {"$regex": letter}},
            {"age": {"$gt": age}}
        ]
    }