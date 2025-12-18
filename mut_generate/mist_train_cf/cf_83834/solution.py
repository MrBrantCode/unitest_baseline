"""
QUESTION:
Write a function `countPairs` that takes two strings `firstString` and `secondString` as input and returns the number of index quintuples `(i, j, a, b, l)` that satisfy the following conditions:

- `0 <= i <= j < firstString.length`
- `0 <= a <= b < secondString.length`
- The substring of `firstString` from `i` to `j` is equal to the substring of `secondString` from `a` to `b`.
- `j - a` is the minimum possible value among all quintuples.
- `l` is the length of the substring and it should be the maximum possible length among all quintuples.

The function should have a time complexity of less than O(n^4) due to the large string lengths (up to 2 * 10^5).
"""

def countPairs(firstString, secondString):
  store1 = {}  
  store2 = {}  

  for i in range(len(firstString)):
      for j in range(i, len(firstString)):
          subStr = firstString[i:j+1]
          if subStr in store1:  
              store1[subStr][1] = j
          else:  
              store1[subStr] = [i,j]
  
  for a in range(len(secondString)):
      for b in range(a, len(secondString)):
          subStr = secondString[a:b+1]
          if subStr in store2:  
              store2[subStr][0] = min(a, store2[subStr][0])
          else:  
              store2[subStr] = [a, b]
  
  count = 0
  minDiff = float('inf')
  maxLen = 0
  for subStr in store1:
      if subStr in store2:  
          i, j = store1[subStr]
          a, b = store2[subStr]
          if j-a<minDiff:  
              minDiff = j-a
              maxLen = j-i+1
              count = 1
          elif j-a==minDiff and j-i+1>maxLen:  
              maxLen = j-i+1
              count = 1
          elif j-a==minDiff and j-i+1==maxLen:  
              count += 1
  return count