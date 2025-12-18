"""
QUESTION:
«Next please», — the princess called and cast an estimating glance at the next groom.

The princess intends to choose the most worthy groom, this is, the richest one. Whenever she sees a groom who is more rich than each of the previous ones, she says a measured «Oh...». Whenever the groom is richer than all previous ones added together, she exclaims «Wow!» (no «Oh...» in this case). At the sight of the first groom the princess stays calm and says nothing.

The fortune of each groom is described with an integer between 1 and 50000. You know that during the day the princess saw n grooms, said «Oh...» exactly a times and exclaimed «Wow!» exactly b times. Your task is to output a sequence of n integers t1, t2, ..., tn, where ti describes the fortune of i-th groom. If several sequences are possible, output any of them. If no sequence exists that would satisfy all the requirements, output a single number -1.

Input

The only line of input data contains three integer numbers n, a and b (1 ≤ n ≤ 100, 0 ≤ a, b ≤ 15, n > a + b), separated with single spaces.

Output

Output any sequence of integers t1, t2, ..., tn, where ti (1 ≤ ti ≤ 50000) is the fortune of i-th groom, that satisfies the given constraints. If no sequence exists that would satisfy all the requirements, output a single number -1.

Examples

Input

10 2 3


Output

5 1 3 6 16 35 46 4 200 99

Input

5 0 0


Output

10 10 6 6 5

Note

Let's have a closer look at the answer for the first sample test. 

  * The princess said «Oh...» (highlighted in bold): 5 1 3 6 16 35 46 4 200 99. 
  * The princess exclaimed «Wow!» (highlighted in bold): 5 1 3 6 16 35 46 4 200 99.
"""

def generate_groom_fortunes(n, a, b):
    if n < a + b + 1:
        return -1
    
    if b == 0:
        if n >= a + 2:
            result = [1, 1]
            for i in range(1, a + 1):
                result.append(i + 1)
            for i in range(n - a - 2):
                result.append(a + 1)
            return result
        elif a == 0:
            return [1] * n
        else:
            return -1
    else:
        result = [1]
        current_max = 1
        for i in range(b):
            current_max *= 2
            result.append(current_max)
        for i in range(1, a + 1):
            result.append(current_max + i)
        for i in range(n - a - b - 1):
            result.append(1)
        return result