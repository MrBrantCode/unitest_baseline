"""
QUESTION:
In vardhaman college of engineering, there is competition with name treasure lock.
To make this competition the key for the lock should satisfy following rules.
1 .3, 5, or both as its digits. No other digit is allowed.
2. Number of times 3 appears is divisible by 5.
3. Number of times 5 appears is divisible by 3.

Rakesh is very eager to win the championship. He is developing a code for that key.Assume yourself in that situation and solve for the key.

INPUT:
first line contains T testcases.
Next T lines consists of the number.
OUTPUT:
Output the number satisfying the above conditions.
if n cannot satisfy the above conditions print -1.

0<t<10
0<n<1000

SAMPLE INPUT
4
1
3
5
17

SAMPLE OUTPUT
-1
555
33333
55555555555533333
"""

def generate_treasure_key(T, numbers):
    results = []
    
    for n in numbers:
        if n < 3:
            results.append("-1")
            continue
        
        if n % 15 == 0 or n % 3 == 0:
            sum_digits = 0
            for _ in range(n):
                sum_digits = sum_digits * 10 + 5
            results.append(str(sum_digits))
            continue
        
        if n % 5 == 0:
            sum_digits = 0
            for _ in range(n):
                sum_digits = sum_digits * 10 + 3
            results.append(str(sum_digits))
            continue
        
        temp = n
        while n > 5:
            n -= 5
            if n % 3 == 0 and (temp - n) % 5 == 0:
                sum_digits = 0
                for _ in range(n):
                    sum_digits = sum_digits * 10 + 5
                for _ in range(temp - n):
                    sum_digits = sum_digits * 10 + 3
                results.append(str(sum_digits))
                break
        else:
            results.append("-1")
    
    return results