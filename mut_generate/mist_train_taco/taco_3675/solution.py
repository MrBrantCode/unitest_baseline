"""
QUESTION:
Example

Input

6
2
3
1
1
4
2


Output

Yes
Yes
Yes
No
Yes
No
"""

def check_bit_sequence(n, sequence):
    bits = set()
    c1 = 0
    count = 0
    ans = []
    
    for x in sequence:
        if x in bits:
            y = x
            while c1 < y and y in bits:
                y -= 1
            if y <= c1:
                y = 0
            if y == 0 and count != x:
                c1 = max(x, c1)
                ans.append('No')
            else:
                bits.add(y)
                ans.append('Yes')
                count += 1
                if y == 0:
                    if len(sequence) - 1 - sequence.index(x) <= 1:
                        ans.extend(['No'] * (len(sequence) - 1 - sequence.index(x)))
                    break
                for i in range(y + 1, x + 1):
                    bits.remove(i)
                    count -= 1
        else:
            bits.add(x)
            count += 1
            ans.append('Yes')
    
    return ans