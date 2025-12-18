"""
QUESTION:
Write a function `loopList` that takes an array `arr` as input and returns its sum. The function should be able to handle arrays of varying lengths and optimize performance for large inputs. Implement exception handling to catch and handle potential runtime errors.
"""

def loopList(arr):
    try:
        return sum(arr)
    except Exception as e:
        print(f"An exception occurred: {e}")