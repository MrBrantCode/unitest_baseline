"""
QUESTION:
Given an unsorted array arr of size n. The task is to find all the star and super star elements in the array. Star are those elements which are strictly greater than all the elements on its right side. Super star are those elements which are strictly greater than all the elements on its left and right side.
Note: Assume first element (arr[0]) is greater than all the elements on its left side, And last element (arr[n-1]) is greater than all the elements on its right side.
Example 1:
Input:
n = 10
arr[] = {1, 6, 5, 4, 7, 8, 4, 3, 2, 1}
Output: 
8 4 3 2 1 
8
Explanation: Star elements are 8, 4, 3, 2 and 1.
Super star element is 8.
Example 2:
Input:
a = 9
arr[] = {1, 2, 10, 3, 4, 5, 8, 10, 4}
Output: 
10 4 
-1
Explanation: Star elements are 10 and 4.
No super star element present here.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getStarAndSuperStar() which takes the array of integers arr and n as parameters and returns an array of integers denoting the answer where first element is the super star element and rest are star elements. Return -1 in first element of the array if no super star element is present. The driver code itself prints the star elements in first line and super star element in second line.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 <= n <= 10^{6}
0 <= |arr[i]| <= 10^{6}
"""

def get_star_and_super_star(arr, n):
    # Initialize the list to store star elements
    star = [arr[-1]]
    
    # Traverse the array from the second last element to the first element
    for i in arr[-2:-len(arr) - 1:-1]:
        if i > star[-1]:
            star.append(i)
    
    # Find the maximum element in the star list
    max_ele = max(star)
    
    # Count the occurrences of the maximum element in the original array
    count = 0
    for i in arr:
        if i == max_ele:
            count += 1
        if count > 1:
            max_ele = -1
            break
    
    # Return the result as a list with the super star element first and then the star elements in reverse order
    return [max_ele] + star[::-1]