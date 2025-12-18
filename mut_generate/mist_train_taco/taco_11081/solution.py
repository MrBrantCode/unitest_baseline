"""
QUESTION:
Given an array where each element (arr[i]) represents the height of the tower. Find for each tower, the nearest possible tower that is shorter than it. You can look left or right on both sides.
Note : 
	
	If two smaller towers are at the same distance, pick the smallest tower.
	
	
	If two towers have the same height then we choose the one with a smaller index.
	
Example 1:
Input: 
arr[] = {1,3,2}
Output: 
{-1,0,0}
Explanation:
For 0th Index : no tower is smallest, so -1.
For 1st Index : For 3, here 1 & 2 both are 
small & at a same distance, so we will pick 1, 
beacuse it has smallest value, so 0(Index)
For 2nd Index : here 1 is smaller, so 0(Index)
So the final output will be which consistes 
Indexes are {-1,0,0}.
Example 2:
Input: 
arr[] = {4,8,3,5,3}
Output: 
{2,2,-1,2,-1}
Explanation: 
For 0th Index : here 3 is the smaller, so 2(Index) 
For 1st Index : For 8, here 4 & 3 both are
small & at a same distance, so we will pick 3, so 2(Index)
For 2nd Index : no tower is smallest, so -1.
For 3rd Index : For 5, here 3 & 3 both are
small & at a same distance, so we will pick 
3(2nd Index) because it smaller Index, so 2(Index)
For 4th Index : no tower is smallest, so -1.
So the final output will be which consistes
Indexes are {2,2,-1,2,-1}.
Your Task:
You don't need to read input or print anything. Your task is to complete the function nearestSmallerTower() which takes an array of heights of the towers as input parameter and returns an array of indexes of the nearest smaller tower. If there is no smaller tower on both sides then return -1 for that tower.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N) 
Constraints:
1 <= N <= 10^{5}
1 <= arr[i] <= 10^{5}
"""

def nearest_smaller_tower(arr):
    def nearest_small_right(arr, n):
        st = [(arr[-1], n - 1)]
        ans = [(-1, i) for i in range(n)]
        ans[-1] = (-1, -1)
        for i in range(n - 2, -1, -1):
            if arr[i] <= st[-1][0]:
                while len(st) > 0 and arr[i] <= st[-1][0]:
                    st.pop()
                if len(st) != 0:
                    ans[i] = st[-1]
            else:
                ans[i] = st[-1]
            st.append((arr[i], i))
        return ans

    def nearest_small_left(arr, n):
        st = [(arr[0], 0)]
        ans = [(-1, i) for i in range(n)]
        ans[0] = (-1, -1)
        for i in range(1, n):
            if arr[i] <= st[-1][0]:
                while len(st) > 0 and arr[i] <= st[-1][0]:
                    st.pop()
                if len(st) != 0:
                    ans[i] = st[-1]
            else:
                ans[i] = st[-1]
            st.append((arr[i], i))
        return ans

    n = len(arr)
    ans = [-1 for i in range(n)]
    r = nearest_small_right(arr, n)
    l = nearest_small_left(arr, n)
    
    for i in range(n):
        if r[i][0] == -1 and l[i][0] == -1:
            ans[i] = -1
        elif r[i][0] != -1 and l[i][0] != -1:
            if abs(i - r[i][1]) < abs(i - l[i][1]):
                ans[i] = r[i][1]
            elif abs(i - r[i][1]) > abs(i - l[i][1]):
                ans[i] = l[i][1]
            elif r[i][0] < l[i][0]:
                ans[i] = r[i][1]
            else:
                ans[i] = l[i][1]
        elif r[i][0] != -1:
            ans[i] = r[i][1]
        else:
            ans[i] = l[i][1]
    
    return ans