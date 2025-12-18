"""
QUESTION:
Given a number k and string num of digits (0 to 9) denoting a positive integer. Find a string denoting the lowest integer number possible by removing k digits from num, without changing their order.
Note: num will not contain any leading zero.
 
Example 1:
Input:
k = 2
num = "143729"
Output: "1329"
Explanation: 1329 is the minimum number
possible after removing '4' and '7'.
 
Example 2:
Input:
k = 3
num = "10056"
Output: "0"
Explanation: 0 is the minimum number
possible after removing '1' , '5' and '6'.
 
Your Task:  
You dont need to read input or print anything. Complete the function buildLowestNumber() which accepts string num and integer k as input parameters and returns a string denoting the smallest integer possible after removing k digits from num without changing the order.
Expected Time Complexity: O(Length of num) 
Expected Auxiliary Space: O(Length of num) 
Constraints:
1 <= Length of num <= 10^{5}
0 <= k < Length of num
"""

def build_lowest_number(num: str, k: int) -> str:
    st = []
    st.append(int(num[0]))
    length = len(num)
    
    for i in range(1, length):
        num_i = int(num[i])
        while len(st) != 0 and k > 0 and (num_i < st[-1]):
            st.pop()
            k -= 1
        st.append(num_i)
    
    while len(st) != 0 and k > 0:
        st.pop()
        k -= 1
    
    ans = ''
    li = list(map(str, st))
    
    while li and li[0] == '0':
        li.pop(0)
    
    if li:
        ans = ''.join(li)
        return ans
    
    return '0'