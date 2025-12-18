"""
QUESTION:
Igor is in 11th grade. Tomorrow he will have to write an informatics test by the strictest teacher in the school, Pavel Denisovich.

Igor knows how the test will be conducted: first of all, the teacher will give each student two positive integers $a$ and $b$ ($a < b$). After that, the student can apply any of the following operations any number of times:

$a := a + 1$ (increase $a$ by $1$),

$b := b + 1$ (increase $b$ by $1$),

$a := a \ | \ b$ (replace $a$ with the bitwise OR of $a$ and $b$).

To get full marks on the test, the student has to tell the teacher the minimum required number of operations to make $a$ and $b$ equal.

Igor already knows which numbers the teacher will give him. Help him figure out what is the minimum number of operations needed to make $a$ equal to $b$.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10^4$). Description of the test cases follows.

The only line for each test case contains two integers $a$ and $b$ ($1 \le a < b \le 10^6$).

It is guaranteed that the sum of $b$ over all test cases does not exceed $10^6$.


-----Output-----

For each test case print one integer — the minimum required number of operations to make $a$ and $b$ equal.


-----Examples-----

Input
5
1 3
5 8
2 5
3 19
56678 164422
Output
1
3
2
1
23329


-----Note-----

In the first test case, it is optimal to apply the third operation.

In the second test case, it is optimal to apply the first operation three times.

In the third test case, it is optimal to apply the second operation and then the third operation.
"""

def min_operations_to_equalize(a: int, b: int) -> int:
    sa = bin(a)[2:]
    sb = bin(b)[2:]
    sa = '0' * (len(sb) - len(sa)) + sa
    res = b - a
    found = False
    for i in range(len(sa)):
        state = sa[i] + sb[i]
        if state == '10':
            found = True
            sbb = sb[:i] + sa[i:]
            cur = int(sbb, 2) - b + 1
            res = min(res, cur)
            j = i
            while sa[j] == '1':
                j -= 1
            saa = sa[:j] + '1' + '0' * (len(sa) - j - 1)
            if sb[j] == '1':
                cur = int(saa, 2) - a
                if int(saa, 2) != b:
                    cur += 1
                res = min(res, cur)
            else:
                sbb = sb[:j] + '1' + '0' * (len(sb) - j - 1)
                cur = int(saa, 2) - a + int(sbb, 2) - b
                if int(saa, 2) != int(sbb, 2):
                    cur += 1
                res = min(res, cur)
            break
    return res if found else 1