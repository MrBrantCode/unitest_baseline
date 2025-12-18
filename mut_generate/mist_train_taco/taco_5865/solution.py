"""
QUESTION:
You are storing an integer array of length m in a database. To maintain internal integrity and protect data, the database stores n copies of this array.

Unfortunately, the recent incident may have altered the stored information in every copy in the database.

It's believed, that the incident altered at most two elements in every copy. You need to recover the original array based on the current state of the database.

In case there are multiple ways to restore the array, report any. If there is no array that differs from every copy in no more than two positions, report that as well.

Input

The first line contains integers n and m (2 ≤ n; 1 ≤ m; n ⋅ m ≤ 250 000) — the number of copies and the size of the array.

Each of the following n lines describes one of the currently stored copies in the database, it consists of m integers s_{i, 1}, s_{i, 2}, ..., s_{i, m} (1 ≤ s_{i, j} ≤ 10^9).

Output

If there is an array consistent with all given copies, print "Yes" and then the array itself. The array must have length m and contain integers between 1 and 10^9 only.

Otherwise, print "No".

If there are multiple possible arrays, print any of them.

Examples

Input


3 4
1 10 10 100
1 1 1 100
10 100 1 100


Output


Yes
1 10 1 100


Input


10 7
1 1 1 1 1 1 1
1 1 1 1 1 1 2
1 1 1 1 1 2 2
1 1 1 1 2 2 1
1 1 1 2 2 1 1
1 1 2 2 1 1 1
1 2 2 1 1 1 1
2 2 1 1 1 1 1
2 1 1 1 1 1 1
1 1 1 1 1 1 1


Output


Yes
1 1 1 1 1 1 1


Input


2 5
2 2 1 1 1
1 1 2 2 2


Output


No

Note

In the first example, the array [1, 10, 1, 100] differs from first and second copies in just one position, and from the third copy in two positions.

In the second example, array [1, 1, 1, 1, 1, 1, 1] is the same as the first copy and differs from all other copies in at most two positions.

In the third example, there is no array differing in at most two positions from every database's copy.
"""

def recover_original_array(n, m, db):
    def solve_helper(n, m, db, start=True):
        found_candidate = -1
        max_diffs = 0
        for i in range(1, n):
            diffs = [j for j in range(m) if db[i][j] != db[0][j]]
            ldiff = len(diffs)
            if ldiff > 4:
                return 'No', []
            if ldiff < 3:
                continue
            if ldiff > max_diffs:
                found_candidate = i
                max_diffs = ldiff
        if found_candidate == -1:
            return 'Yes', db[0]
        diffs = [j for j in range(m) if db[found_candidate][j] != db[0][j]][:]
        for attempt in range(1, 1 + (1 << len(diffs))):
            current = db[0][:]
            for i in range(len(diffs)):
                if attempt >> i & 1:
                    current[diffs[i]] = db[found_candidate][diffs[i]]
            for i in range(n):
                cdiffs = [j for j in range(m) if db[i][j] != current[j]]
                if len(cdiffs) > 2:
                    break
            else:
                return 'Yes', current
        if start:
            (db[0], db[found_candidate]) = (db[found_candidate], db[0])
            return solve_helper(n, m, db, False)
        return 'No', []
    
    return solve_helper(n, m, db)