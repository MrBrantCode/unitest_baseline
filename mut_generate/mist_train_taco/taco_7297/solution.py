"""
QUESTION:
This is the second part of a two-part challenge. See [part I](https://www.codewars.com/kata/587387d169b6fddc16000002) if you haven't done so already.
The problem is the same, only with longer lists and larger values.

Imagine you have a number of jobs to execute. Your workers are not permanently connected to your network, so you have to distribute all your jobs in the beginning. Luckily, you know exactly how long each job is going to take. 

Let 
```
x = [2,3,4,6,8,2]
```
be the amount of time each of your jobs is going to take.

Your task is to write a function ```splitlist(x)```, that will return two lists ```a``` and ```b```, such that ```abs(sum(a)-sum(b))``` is minimised.

One possible solution to this example would be 
```
a=[2, 4, 6]
b=[3, 8, 2]
```
with  ```abs(sum(a)-sum(b)) == 1```.

The order of the elements is not tested, just make sure that you minimise ```abs(sum(a)-sum(b))``` and that ```sorted(a+b)==sorted(x)```.

You may assume that ```len(x)<=40``` and ```0<=x[i]<=1000```.
"""

def minimize_partition_difference(x):
    half = sum(x) // 2
    sums = [(0, [])]
    
    for (i, n) in enumerate(x):
        sums = sums + [(m + n, a + [i]) for (m, a) in sums if m + n <= half]
        if max((s[0] for s in sums)) == half:
            break
    
    sums.sort(key=lambda v: abs(v[0] - half))
    indices = sums[0][1]
    
    a = [n for (i, n) in enumerate(x) if i in indices]
    b = [n for (i, n) in enumerate(x) if i not in indices]
    
    return a, b