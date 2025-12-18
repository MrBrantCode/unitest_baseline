"""
QUESTION:
Design a Python function named `process_queries` that calculates the disparity, positions, and average of the maximum and minimum integers within each query array in a given list of queries. The function should efficiently handle arrays with up to 10^6 elements, duplicate integers, negative integers, and empty arrays. It should also process up to 10^3 queries without surpassing time and space complexity limitations. The function should return a list of dictionaries containing the difference, minimum index, maximum index, and average for each query. If a query is empty, it should return the difference as 0, indexes as -1, and average as 0.
"""

def process_queries(queries):
    result = []
    for query in queries:
        if len(query) == 0: # handle case for empty array
            result.append({
                "difference": 0,
                "minimum_index": -1,
                "maximum_index": -1,
                "average": 0
            })
            continue

        min_i = max_i = 0
        min_n = max_n = query[0]
        for i, num in enumerate(query):
            if num < min_n: # update minimum if current number is less
                min_n = num
                min_i = i
            elif num > max_n: # update maximum if current number is greater
                max_n = num
                max_i = i

        result.append({
            "difference": max_n - min_n,
            "minimum_index": min_i,
            "maximum_index": max_i,
            "average": round((min_n + max_n) / 2)
        })

    return result