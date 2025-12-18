"""
QUESTION:
In Pragyan, every shop has their own discount methods to attract the customers. One discount method called Buy 1 Get 1 caught your friend's attention. That is, if your friend buys one object, then your friend can get one additional object with the same color without charge by Buy 1 Get 1.
Your friend lists the needed objects as a string S, each letter denotes one object, and the same letters denote the same object, and the different letters denote the different objects. The cost of each object is 1. Your task is to calculate the minimum cost for getting all the objects your friend is asking for. Help Him !!!

Input

The first line of input contains a single line T, which represents the number of test cases. Then T lines will follow, and each contains a string S, which represents the objects your friend needs.

Output

Output the minimum cost for each test case.

Constraints

1 ≤ T ≤ 100
1 ≤ |S| ≤ 200, where |S| represents the length of the string S. 
The string S is case sensitive, and will contain only English characters in the range [a-z], [A-Z].

SAMPLE INPUT
ssss

SAMPLE OUTPUT
2
"""

def calculate_minimum_cost(test_cases: list) -> list:
    """
    Calculate the minimum cost to buy all objects listed in each test case string,
    considering the Buy 1 Get 1 discount method.

    Parameters:
    test_cases (list): A list of strings where each string represents the objects needed.

    Returns:
    list: A list of integers where each integer represents the minimum cost for the corresponding test case.
    """
    results = []
    
    for s in test_cases:
        obj_count = {}
        
        # Count the occurrences of each object
        for char in s:
            if char in obj_count:
                obj_count[char] += 1
            else:
                obj_count[char] = 1
        
        total_cost = 0
        
        # Calculate the minimum cost for the current test case
        for count in obj_count.values():
            total_cost += (count + 1) // 2  # This handles the Buy 1 Get 1 logic
        
        results.append(total_cost)
    
    return results