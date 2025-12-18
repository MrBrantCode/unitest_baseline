"""
QUESTION:
Write a function named `all_triplets_with_k_sum` that takes a list of integers and an integer `k` as input, and returns all unique triplets in the list that sum up to `k`. If no such triplets exist, return an empty list. The function must have a time complexity of O(n^2).
"""

def all_triplets_with_k_sum(nums: list, k: int):
    """
    This function returns all unique triplets in the list that sum up to 'k'. 
    If no such triplets exist, it returns an empty list.

    Args:
    nums (list): A list of integers.
    k (int): The target sum.

    Returns:
    list: A list of unique triplets that sum up to 'k'.
    """
    
    nums.sort()  # O(nlogn)
    answer = []
    length = len(nums)

    # For every element in nums
    for i in range(length - 2):

        # To avoid counting duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        start = i + 1
        end = length - 1

        while start < end:
            
            # If sum of elements at start, end and i is greater than k, end must be decreased
            if nums[i] + nums[start] + nums[end] > k:
                end -= 1

            # If sum of elements at start, end and i is less than k, start must be increased    
            elif nums[i] + nums[start] + nums[end] < k:
                start += 1

            else:
                answer.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1

                # Skip duplicate triplets
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                    
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1

    return answer