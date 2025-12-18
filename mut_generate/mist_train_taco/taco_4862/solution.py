"""
QUESTION:
Being a Programmer you have to learn how to make your output looks better. According to the company, its company programmers have to present its output in a different manner as: If your output is 10.000000 you can save the decimal places and thus your output becomes 10. Now u have the learn the way to output.  You are given elements of an array A[N] and you have to divide N by total no. of +ve integers, N by total no. of -ve integers, and N by total no. of zero value integers.
 
Example 1:
Input : 
N = 10
A[] = {7, 7, 7, 7, 7, 7, -9, -9, -9, 0}
Output : 
1.66667
3.33333
10
Explanation :
Positive count = 6, therefore 10/6 = 1.66667
Negative count = 3, therefore 10/3 = 3.33333
Zero's count = 1, therefore 10/1 = 10
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function Learning() which takes the array A[], its size N, pos, neg and zero as inputs and stores the answers in the reference variables pos, neg and zero the following:-
N by Total no. of +ve integers
N by Total no. of -ve integers
N by Total no. of zero value integers
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints :
1 ≤ N ≤ 10^{5}
-10^{5} ≤ A[i] ≤ 10^{5}
"""

def calculate_ratios(arr, n):
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    # Count the number of positive, negative, and zero elements
    for i in range(n):
        if arr[i] > 0:
            pos_count += 1
        elif arr[i] < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    # Calculate the ratios
    if pos_count != 0:
        pos_ratio = round(n / pos_count, 5)
    else:
        pos_ratio = 0
    
    if neg_count != 0:
        neg_ratio = round(n / neg_count, 5)
    else:
        neg_ratio = 0
    
    if zero_count != 0:
        zero_ratio = round(n / zero_count, 5)
    else:
        zero_ratio = 0
    
    return (pos_ratio, neg_ratio, zero_ratio)