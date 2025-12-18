"""
QUESTION:
Implement a function `retrieve_stats(person)` that retrieves and returns specific statistical information from a person's data. The input `person` is a dictionary representing a person's data with nested structures. The function should return a string representing the statistical information and handle any `IndexError` that occurs during data retrieval by returning the string "IndexError occurred".
"""

def retrieve_stats(person: dict) -> str:
    try:
        stats = person.get("stats")[0].get("splits")[0].get("stat")
        return stats
    except IndexError as e:
        return "IndexError occurred"