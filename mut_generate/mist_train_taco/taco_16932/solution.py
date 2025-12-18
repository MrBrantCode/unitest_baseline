"""
QUESTION:
Given a sequence of integers $a$, a triplet $(a[i],a[j],a[k])$ is beautiful if:

$i\lt j\lt k$
$a[j]-a[i]=a[k]-a[j]=d$

Given an increasing sequenc of integers and the value of $\boldsymbol{d}$, count the number of beautiful triplets in the sequence.

Example 

$arr=[2,2,3,4,5]$ 

$\boldsymbol{d}=1$    

There are three beautiful triplets, by index: $[i,j,k]=[0,2,3],[1,2,3],[2,3,4]$.  To test the first triplet, $ar r[j]-ar r[i]=3-2=1$ and $ar r[k]-ar r[j]=4-3=1$.  

Function Description  

Complete the beautifulTriplets function in the editor below.     

beautifulTriplets has the following parameters:  

int d: the value to match   
int arr[n]:  the sequence, sorted ascending   

Returns   

int: the number of beautiful triplets   

Input Format

The first line contains $2$ space-separated integers, $n$ and $\boldsymbol{d}$, the length of the sequence and the beautiful difference. 

The second line contains $n$ space-separated integers $arr\left[i\right]$.

Constraints

$1\leq n\leq10^4$
$1\leq d\leq20$
$0\leq\textit{arr}[i]\leq2\times10^4$
$ar r[i]>ar r[i-1]$

Sample Input
STDIN           Function
-----           --------
7 3             arr[] size n = 7, d = 3
1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]

Sample Output
3

Explanation

There are many possible triplets $(arr[i],ar r[j],ar r[k])$, but our only beautiful triplets are $(1,4,7)$ , $(4,7,10)$ and $(2,5,8)$ by value, not index. Please see the equations below:    

$7-4=4-1=3=d$ 

$10-7=7-4=3=d$ 

$8-5=5-2=3=d$  

Recall that a beautiful triplet satisfies the following equivalence relation: $arr[j]-arr[i]=arr[k]-arr[j]=d$ where $i\lt j\lt k$.
"""

def count_beautiful_triplets(arr, d):
    cnt = {}
    left = []
    
    # Step 1: Populate the left array with counts of elements that satisfy the first condition (a[j] - a[i] = d)
    for x in arr:
        left.append(cnt.get(x - d, 0))
        if x not in cnt:
            cnt[x] = 0
        cnt[x] += 1
    
    # Step 2: Reverse the left array to align with the reversed sequence
    left = left[::-1]
    
    # Step 3: Initialize a new count dictionary for the second condition (a[k] - a[j] = d)
    cnt = {}
    res = 0
    
    # Step 4: Calculate the number of beautiful triplets
    for i, x in enumerate(arr[::-1]):
        res += left[i] * cnt.get(x + d, 0)
        cnt[x] = cnt.get(x, 0) + 1
    
    return res