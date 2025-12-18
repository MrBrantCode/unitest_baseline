"""
QUESTION:
Write three functions: `sum_subarray`, `verify_no_adjacent_elements`, and `find_largest_sum`. 

Function `sum_subarray` should take an array and two indices as input and return the sum of the subarray between the given indices. Function `verify_no_adjacent_elements` should take an array and two indices as input and return True if no adjacent elements are found between the specified indices, False otherwise. Function `find_largest_sum` should take an array as input and return the largest possible sum of a subarray such that no two elements in the subarray are adjacent.

All three functions should handle exceptions where the given index is out of the array range or when the input is invalid.
"""

def sum_subarray(array: list, start: int, end: int) -> int:
    try:
        return sum(array[start:end+1])
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Invalid input")
    except Exception as e:
        print("Error:", e)

def verify_no_adjacent_elements(array: list, start: int, end: int) -> bool:
    try:
        for i in range(start, end):
            if array[i] == array[i+1]:
                return False
        return True
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Invalid input")
    except Exception as e:
        print("Error:", e)

def find_largest_sum(array: list) -> int:
    try:
        if not array:
            return 0
        if len(array) == 1:
            return array[0]

        dp = [0]*len(array)
        dp[0] = array[0]
        dp[1] = max(array[0], array[1])

        for i in range(2, len(array)):
            dp[i] = max(dp[i-1], dp[i-2]+array[i])

        return dp[-1]
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Invalid input")
    except Exception as e:
        print("Error:", e)