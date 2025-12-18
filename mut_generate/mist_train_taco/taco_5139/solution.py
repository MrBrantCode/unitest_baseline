"""
QUESTION:
Consider a big party where N guests came to it and a log register for guest’s entry and exit times was maintained. Find the minimum time at which there were maximum guests at the party. Note that entries in the register are not in any order.
Note: Guests are leaving after the exit times.
Example 1:
Input:
N = 5
Entry= {1, 2,10, 5, 5}
Exit = {4, 5, 12, 9, 12}
Output: 3 5
Explanation: At time 5 there were 
             guest number 2, 4 and 5 present.
Example 2:
Input:
N = 7
Entry= {13, 28, 29, 14, 40, 17, 3}
Exit = {107, 95, 111, 105, 70, 127, 74}
Output: 7 40
Explanation: At time 40 there were 
             all 7 guests present in the party.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxGuests() which takes 3 arguments(Entry array, Exit array, N) and returns the maximum number of guests present at a particular time and that time as a pair.
Expected Time Complexity: O(N*Log(N) ).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N <= 10^{5}
1 <= Entry[i],Exit[i] <= 10^{5}
"""

def find_max_guests(Entry, Exit, N):
    ans = 0
    count = 0
    data = []
    time = 0
    
    # Create a combined list of entry and exit times with markers
    for i in range(N):
        data.append([Entry[i], 'x'])
        data.append([Exit[i], 'y'])
    
    # Sort the combined list
    data = sorted(data)
    
    # Traverse the sorted list to find the maximum number of guests and the corresponding time
    for i in range(len(data)):
        if data[i][1] == 'x':
            count += 1
        if data[i][1] == 'y':
            count -= 1
        if ans < count:
            ans = count
            time = data[i][0]
    
    return (ans, time)