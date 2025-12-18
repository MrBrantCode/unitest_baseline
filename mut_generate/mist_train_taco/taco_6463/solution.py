"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

Ada has an array of N  crayons, some crayons are pointing upwards and some downwards.
Ada thinks that an array of crayons is beautiful if all the crayons are pointing in the same direction.

In one step you can flip any segment of consecutive crayons. After flipping a segment, all crayons pointing downwards will point upwards and visceversa

What is the minimum number of steps to make the array of crayons beautiful?

------ Input ------ 

The first line of the input contains T the number of test cases.
Each test case is described in one line containing a string S of N characters, the i-th character is 'U' if the i-th crayon is pointing upwards and 'D' if it is pointing downwards.

------ Output ------ 

For each test case, output a single line containing the minimum number of flips needed to make all crayons point to the same direction.

------ Constraints ------ 

$1 ≤ T ≤ 3000$
$1 ≤ N ≤ 50$

----- Sample Input 1 ------ 
1
UUDDDUUU
----- Sample Output 1 ------ 
1
----- explanation 1 ------ 
Example case 1. In one step we can flip all the crayons pointing downwards
"""

def min_flips_to_beautiful_crayons(test_cases):
    results = []
    
    for s in test_cases:
        u = []
        d = []
        nu = 0
        nd = 0
        
        for c in s:
            if c == 'U':
                nu += 1
                if nd > 0:
                    d.append(nd)
                    nd = 0
            else:
                nd += 1
                if nu > 0:
                    u.append(nu)
                    nu = 0
        
        if nu > 0:
            u.append(nu)
        elif nd > 0:
            d.append(nd)
        
        results.append(min(len(u), len(d)))
    
    return results