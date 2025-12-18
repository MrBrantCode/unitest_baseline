"""
QUESTION:
The median of $\mbox{M}$ numbers is defined as the middle number after sorting them in order if $\mbox{M}$ is odd. Or it is the average of the middle two numbers if $\mbox{M}$ is even. You start with an empty number list. Then, you can add numbers to the list, or remove existing numbers from it. After each add or remove operation, output the median.

Example: 

For a set of $M=5$ numbers $9,2,8,4,1$ the median is the third number in the sorted set $1,2,4,8,9$, which is $\begin{array}{c}4\end{array}$. Similarly, for a set of $M=4$ numbers, $5,2,10,4$, the median is the average of the second and the third element in the sorted set $2,4,5,10$, which is $(4+5)/2=4.5$.  

Input: 

The first line is an integer, $N$, that indicates the number of operations. Each of the next $N$ lines is either a x or r x. a x indicates that $\boldsymbol{x}$ is added to the set, and r x indicates that $\boldsymbol{x}$ is removed from the set.

Output: 

For each operation: If the operation is add, output the median after adding $\boldsymbol{x}$ in a single line. If the operation is remove and the number $\boldsymbol{x}$ is not in the list, output Wrong! in a single line. If the operation is remove and the number $\boldsymbol{x}$ is in the list, output the median after deleting $\boldsymbol{x}$ in a single line. (If the result is an integer DO NOT output decimal point. And if the result is a real number, DO NOT output trailing 0s.)

Note 

If your median is 3.0, print only 3. And if your median is 3.50, print only 3.5. Whenever you need to print the median and the list is empty, print Wrong!

Constraints: 

$0<N\leq10^5$


For each a x or r x, $\boldsymbol{x}$ will always be a signed integer (which will fit in 32 bits).

Sample Input:  

7  
r 1  
a 1  
a 2  
a 1  
r 1  
r 2  
r 1  

Sample Output:  

Wrong!  
1  
1.5  
1  
1.5  
1  
Wrong!

Note: As evident from the last line of the input, if after remove operation the list becomes empty, you have to print Wrong!.
$$
"""

from bisect import bisect_left

def process_operations(operations):
    class MedianFinder:
        def __init__(self):
            self.items = []

        def addItem(self, num):
            position = bisect_left(self.items, num)
            self.items.insert(position, num)
            return self.median()

        def remItem(self, num):
            position = bisect_left(self.items, num)
            if position >= len(self.items) or self.items[position] != num:
                return 'Wrong!'
            else:
                del self.items[position]
                return self.median()

        def median(self):
            l = len(self.items)
            if l == 0:
                return 'Wrong!'
            elif l & 1:
                return self.items[int(l / 2)]
            else:
                ans = self.items[int(l / 2)] + self.items[int(l / 2) - 1]
                if ans == 0:
                    return 0
                elif ans & 1:
                    return ans / 2
                else:
                    return int(ans / 2)

    arr = MedianFinder()
    results = []
    for operation in operations:
        Q = operation.split(' ')
        num = int(Q[1])
        if Q[0] == 'a':
            results.append(arr.addItem(num))
        elif Q[0] == 'r':
            results.append(arr.remItem(num))
    return results