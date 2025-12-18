"""
QUESTION:
Akira, the student council president of A High School, decided to investigate which club activities the A High School students belong to. A High School has N students numbered 1 to N and M types of club activities numbered 1 to M. There is no limit to the number of people in each club activity, and there can be 0 club activities. However, according to the school rules of A High School, students can only belong to one club activity. All students follow this school rule.

Akira asked student members to investigate and obtained records for line K, such as each line being one of the following:

* Student a and student b belong to the same club activities.
* Student c belongs to club activity x.



However, there may be a contradiction in this record that would cause someone to violate school rules. Akira decided to look at the first line in order and look for the first line that could be judged to be inconsistent.

Create a program that finds the number of the first line that can be determined to be inconsistent given a record of K lines.



Input

The input is given in the following format.


NMK
record1
record2
::
recordK


The first line gives the number of students N (1 ≤ N ≤ 100000), the number of club activity types M (1 ≤ M ≤ 100000), and the number of recorded lines K (1 ≤ K ≤ 200000). Each line of record, recordi, is given in the following K lines in one of the following formats:


1 a b


Or


2 c x


When the first digit is "1", it indicates that student a (1 ≤ a ≤ N) and student b (1 ≤ b ≤ N) belong to the same club activity. However, a ≠ b.

When the first digit is "2", it indicates that student c (1 ≤ c ≤ N) belongs to club activity x (1 ≤ x ≤ M).

Output

Output the number of the first line that can be determined to be inconsistent on one line. If not found, output 0 on one line.

Examples

Input

3 2 5
1 1 2
1 2 3
2 1 1
2 3 2
2 2 1


Output

4


Input

3 2 4
1 1 2
2 1 1
2 3 2
2 2 1


Output

0


Input

3 2 2
1 1 2
2 1 1


Output

0
"""

def find_first_inconsistent_record(n, m, k, records):
    parent = list(range(n + m))

    def root(x):
        if x == parent[x]:
            return x
        parent[x] = root(parent[x])
        return parent[x]

    def unite(x, y):
        px = root(x)
        py = root(y)
        if px < py:
            parent[py] = px
        else:
            parent[px] = py

    for i, (a, b, c) in enumerate(records):
        b -= 1
        c -= 1
        if a == 1:
            pb = root(m + b)
            pc = root(m + c)
            if pb < m and pc < m and (pb != pc):
                return i + 1
            unite(pb, pc)
        else:
            pb = root(m + b)
            if pb < m and pb != c:
                return i + 1
            unite(c, pb)
    
    return 0