"""
QUESTION:
Vera adores poems. All the poems Vera knows are divided into quatrains (groups of four lines) and in each quatrain some lines contain rhymes.

Let's consider that all lines in the poems consist of lowercase Latin letters (without spaces). Letters "a", "e", "i", "o", "u" are considered vowels.

Two lines rhyme if their suffixes that start from the k-th vowels (counting from the end) match. If a line has less than k vowels, then such line can't rhyme with any other line. For example, if k = 1, lines commit and hermit rhyme (the corresponding suffixes equal it), and if k = 2, they do not rhyme (ommit ≠ ermit).

Today on a literature lesson Vera learned that quatrains can contain four different schemes of rhymes, namely the following ones (the same letters stand for rhyming lines): 

  * Clerihew (aabb); 
  * Alternating (abab); 
  * Enclosed (abba). 



If all lines of a quatrain pairwise rhyme, then the quatrain can belong to any rhyme scheme (this situation is represented by aaaa).

If all quatrains of a poem belong to the same rhyme scheme, then we can assume that the whole poem belongs to this rhyme scheme. If in each quatrain all lines pairwise rhyme, then the rhyme scheme of the poem is aaaa. Let us note that it doesn't matter whether lines from different quatrains rhyme with each other or not. In other words, it is possible that different quatrains aren't connected by a rhyme.

Vera got a long poem as a home task. The girl has to analyse it and find the poem rhyme scheme. Help Vera cope with the task.

Input

The first line contains two integers n and k (1 ≤ n ≤ 2500, 1 ≤ k ≤ 5) — the number of quatrains in the poem and the vowel's number, correspondingly. Next 4n lines contain the poem. Each line is not empty and only consists of small Latin letters. The total length of the lines does not exceed 104.

If we assume that the lines are numbered starting from 1, then the first quatrain contains lines number 1, 2, 3, 4; the second one contains lines number 5, 6, 7, 8; and so on.

Output

Print the rhyme scheme of the poem as "aabb", "abab", "abba", "aaaa"; or "NO" if the poem does not belong to any of the above mentioned schemes.

Examples

Input

1 1
day
may
sun
fun


Output

aabb


Input

1 1
day
may
gray
way


Output

aaaa


Input

2 1
a
a
a
a
a
a
e
e


Output

aabb


Input

2 1
day
may
sun
fun
test
hill
fest
thrill


Output

NO

Note

In the last sample both quatrains have rhymes but finding the common scheme is impossible, so the answer is "NO".
"""

def determine_rhyme_scheme(n, k, poem):
    def z(a, b):
        c = 0
        d = ''
        for i in range(len(a) - 1, -1, -1):
            d += a[i]
            if a[i] in ['a', 'e', 'i', 'o', 'u']:
                c += 1
            if c == k:
                break
        f = c == k
        c = 0
        e = ''
        for i in range(len(b) - 1, -1, -1):
            e += b[i]
            if b[i] in ['a', 'e', 'i', 'o', 'u']:
                c += 1
            if c == k:
                break
        return d == e and c == k and f

    a = 0
    b = 0
    c = 0
    d = 0
    
    for i in range(n):
        e = poem[4 * i]
        f = poem[4 * i + 1]
        g = poem[4 * i + 2]
        h = poem[4 * i + 3]
        
        a1 = z(e, f)
        a2 = z(e, g)
        a3 = z(e, h)
        a4 = z(f, g)
        a5 = z(f, h)
        a6 = z(g, h)
        
        if a1 and a2 and a3 and a4 and a5 and a6:
            d += 1
        elif a1 and a6:
            a += 1
        elif a2 and a5:
            b += 1
        elif a3 and a4:
            c += 1
    
    if a + b + c + d != n:
        return 'NO'
    elif b == 0 and c == 0:
        return 'aaaa' if a == 0 else 'aabb'
    elif a == 0 and c == 0:
        return 'aaaa' if b == 0 else 'abab'
    elif a == 0 and b == 0:
        return 'aaaa' if c == 0 else 'abba'
    else:
        return 'NO'