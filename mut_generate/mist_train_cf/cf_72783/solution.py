"""
QUESTION:
Create a function `fruit_distribution` that takes three parameters: a list `s` of strings representing the quantity of various fruits in a basket, an integer `n` signifying the total number of fruits, and a list `fruits` of all possible fruit types. The function should return a dictionary containing the quantity of each fruit not mentioned in the list `s`. 

The input list `s` will contain at least two fruit types and at most all fruit types, and the numbers in the list are non-negative integers. The total number of fruits `n` is between 1 and 10^5. The result dictionary should only include fruits with a non-zero count.
"""

def entance(s, n, fruits):
    """
    In this task, you will receive a list of strings signifying the quantity of various fruits
    present in a basket. The basket holds apples, oranges, mangoes, bananas, strawberries, and cherries.
    The list will appear as follows: ["X apples", "Y oranges", "Z mangoes",...]

    Given this list and an integer signifying the sum of fruits in the basket (1 <= n <= 10^5),
    return a dictionary reflecting the quantity of each fruit not mentioned in the list.

    Constraints:

    * The input list, 's', will contain at least two fruit types and at most all fruit types.
    * The numbers in the input list are non-negative integers.

    :param s: A list of strings representing the quantity of various fruits.
    :param n: An integer signifying the total number of fruits.
    :param fruits: A list of all possible fruit types.
    :return: A dictionary containing the quantity of each fruit not mentioned in the list.
    """

    fruit_counts = {}
    for fruit_info in s:
        count, fruit = fruit_info.split()
        fruit_counts[fruit] = int(count)

    remaining_fruits = n - sum(fruit_counts.values())
    result = {}

    for fruit in fruits:
        if fruit not in fruit_counts:
            if remaining_fruits > 0:
                result[fruit] = remaining_fruits
                remaining_fruits = 0
            else:
                break

    return result