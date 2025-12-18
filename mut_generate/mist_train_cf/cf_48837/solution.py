"""
QUESTION:
Create a function `find_largest_sum` that takes a list of integers as input and returns the maximum sum of non-adjacent elements in the list. The function should handle edge cases such as an empty list, a list with only one element, and invalid inputs. The function should also handle exceptions that may occur during execution.
"""

def find_largest_sum(array: list) -> int:
    try:
        # special cases: empty array and array with only one element
        if not array:
            return 0
        if len(array) == 1:
            return array[0]

        # auxiliary array for dynamic programming
        # initialise with 0 for the first element, and max between first and second element for the second
        dp = [0]*len(array)
        dp[0] = array[0]
        dp[1] = max(array[0], array[1])

        # dynamic programming: find maximum sum considering non-adjacent elements for each position
        for i in range(2, len(array)):
            dp[i] = max(dp[i-1], dp[i-2]+array[i])

        return dp[-1] # return last element in dp, which consider all elements in the array
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Invalid input")
    except Exception as e:
        print("Error:", e)