"""
QUESTION:
Jack and Daniel are friends. Both of them like letters, especially uppercase ones. 

They are cutting uppercase letters from newspapers, and each one of them has his collection of letters stored in a stack. 

One beautiful day, Morgan visited Jack and Daniel. He saw their collections. He wondered what is the lexicographically minimal string made of those two collections. He can take a letter from a collection only when it is on the top of the stack.  Morgan wants to use all of the letters in their collections.  

As an example, assume Jack has collected $a=[A,C,A]$ and Daniel has $b=[B,C,F]$.  The example shows the top at index $\mbox{0}$ for each stack of letters. Assemble the string  as follows:  

Jack	Daniel	result
ACA	BCF
CA	BCF	A
CA	CF	AB
A	CF	ABC
A	CF	ABCA
    	F	ABCAC
    		ABCACF

Note the choice when there was a tie at CA and CF.

Function Description  

Complete the morganAndString function in the editor below.  

morganAndString has the following parameter(s):  

string a: Jack's letters, top at index $\mbox{0}$  
string b: Daniel's letters, top at index $\mbox{0}$  

Returns 

- string: the completed string  

Input Format

The first line contains the an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases.  

The next $\boldsymbol{\boldsymbol{t}}$ pairs of lines are as follows: 

- The first line contains string $\boldsymbol{a}$ 

- The second line contains string $\boldsymbol{b}$.  

Constraints

$1\leq T\leq5$  
$1\leq|a|,|b|\leq10^5$  
$\boldsymbol{\alpha}$ and $\boldsymbol{b}$ contain upper-case letters only, ascii[A-Z].

Sample Input
2
JACK
DANIEL
ABACABA
ABACABA

Sample Output
DAJACKNIEL
AABABACABACABA

Explanation

The first letters to choose from are J and D since they are at the top of the stack. D is chosen and the options now are J and A. A is chosen. Then the two stacks have J and N, so J is chosen. The current string is DA. Continue this way to the end to get the string.
"""

def morgan_and_string(a: str, b: str) -> str:
    len_a = len(a)
    len_b = len(b)
    idx_a = 0
    idx_b = 0
    result = []

    def pick_smaller_char():
        nonlocal idx_a, idx_b
        if idx_a >= len_a:
            idx_b += 1
            return b[idx_b - 1]
        if idx_b >= len_b:
            idx_a += 1
            return a[idx_a - 1]
        if a[idx_a] > b[idx_b]:
            idx_b += 1
            return b[idx_b - 1]
        elif a[idx_a] < b[idx_b]:
            idx_a += 1
            return a[idx_a - 1]
        else:
            i1 = idx_a
            i2 = idx_b
            while i1 < len_a and i2 < len_b and a[i1] == b[i2]:
                i1 += 1
                i2 += 1
            if i1 < len_a and i2 < len_b:
                if a[i1] > b[i2]:
                    idx_b += 1
                    return b[idx_b - 1]
                else:
                    idx_a += 1
                    return a[idx_a - 1]
            elif i1 < len_a:
                idx_a += 1
                return a[idx_a - 1]
            elif i2 < len_b:
                idx_b += 1
                return b[idx_b - 1]
            else:
                if len_a - idx_a > len_b - idx_b:
                    idx_a += 1
                    return a[idx_a - 1]
                else:
                    idx_b += 1
                    return b[idx_b - 1]

    while idx_a < len_a or idx_b < len_b:
        result.append(pick_smaller_char())

    return ''.join(result)