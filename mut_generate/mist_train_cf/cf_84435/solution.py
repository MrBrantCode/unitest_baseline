"""
QUESTION:
Develop a function `same_product(lst)` that takes a list of integers as input and returns `True` if it's possible to rearrange the list into two non-empty subsets with an identical count of elements and product, and `False` otherwise. The function should work for lists containing positive, negative numbers, zero, and duplicates.
"""

def can_rearrange(lst):
    lst.sort()
    N=len(lst)
    half=N//2
    memo=dict()
    def helper(i=0,j=0,product1=1,product2=1,p1=0,p2=0):
        if (p1,p2,product1,product2,i,j) in memo:
            return memo[(p1,p2,product1,product2,i,j)]
        if p1>half or p2>half or i>j:
            return None
        if p1==p2==half:
            if product1==product2:  
                return {product1}
            return None
        answer=helper(i+1,j+1,product1*lst[i],product2,p1+1,p2) or \
               helper(i+1,j+1,product1,product2*lst[j],p1,p2+1)
        if i<j-1:
            answer=answer or helper(i+1,j,product1*lst[i],product2,p1+1,p2) or \
                   helper(i,j-1,product1,product2*lst[j],p1,p2+1)
        memo[(p1,p2,product1,product2,i,j)]=answer
        return answer
    return bool(helper())