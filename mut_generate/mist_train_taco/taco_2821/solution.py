"""
QUESTION:
Almost Identical Programs

The programming contest named Concours de Programmation Comtemporaine Interuniversitaire (CPCI) has a judging system similar to that of ICPC; contestants have to submit correct outputs for two different inputs to be accepted as a correct solution. Each of the submissions should include the program that generated the output. A pair of submissions is judged to be a correct solution when, in addition to the correctness of the outputs, they include an identical program.

Many contestants, however, do not stop including a different version of their programs in their second submissions, after modifying a single string literal in their programs representing the input file name, attempting to process different input. The organizers of CPCI are exploring the possibility of showing a special error message for such close submissions, indicating contestants what's wrong with such submissions. Your task is to detect such close submissions.

Input

The input consists of at most 100 datasets, each in the following format.


s1
s2


Each of s1 and s2 is a string written in a line, with the length between 1 and 200, inclusive. They are the first and the second submitted programs respectively. A program consists of lowercase letters (`a`, `b`, ..., `z`), uppercase letters (`A`, `B`, ..., `Z`), digits (`0`, `1`, ..., `9`), double quotes (`"`), and semicolons (`;`). When double quotes occur in a program, there are always even number of them.

The end of the input is indicated by a line containing one '`.`' (period).

Output

For each dataset, print the judge result in a line.

If the given two programs are identical, print `IDENTICAL`. If two programs differ with only one corresponding string literal, print `CLOSE`. Otherwise, print `DIFFERENT`. A string literal is a possibly empty sequence of characters between an odd-numbered occurrence of a double quote and the next occurrence of a double quote.

Sample Input


print"hello";print123
print"hello";print123
read"B1input";solve;output;
read"B2";solve;output;
read"C1";solve;output"C1ans";
read"C2";solve;output"C2ans";
""""""""
"""42"""""
slow"program"
fast"code"
"super"fast"program"
"super"faster"program"
X""
X
I"S""CREAM"
I"CE""CREAM"
11"22"11
1"33"111
.


Output for the Sample Input


IDENTICAL
CLOSE
DIFFERENT
CLOSE
DIFFERENT
DIFFERENT
DIFFERENT
CLOSE
DIFFERENT






Example

Input

print"hello";print123
print"hello";print123
read"B1input";solve;output;
read"B2";solve;output;
read"C1";solve;output"C1ans";
read"C2";solve;output"C2ans";
""""""""
"""42"""""
slow"program"
fast"code"
"super"fast"program"
"super"faster"program"
X""
X
I"S""CREAM"
I"CE""CREAM"
11"22"11
1"33"111
.


Output

IDENTICAL
CLOSE
DIFFERENT
CLOSE
DIFFERENT
DIFFERENT
DIFFERENT
CLOSE
DIFFERENT
"""

def compare_programs(s1: str, s2: str) -> str:
    # Split the programs by double quotes
    sl1 = s1.split('"')
    sl2 = s2.split('"')
    
    # If the number of segments is different, the programs are different
    if len(sl1) != len(sl2):
        return "DIFFERENT"
    
    diff_count = 0
    
    # Iterate through the segments
    for i in range(len(sl1)):
        if i % 2 == 0:
            # Non-string literal parts should be identical
            if sl1[i] != sl2[i]:
                return "DIFFERENT"
        else:
            # String literal parts can differ by one
            if sl1[i] != sl2[i]:
                diff_count += 1
    
    # Determine the result based on the number of differences
    if diff_count == 0:
        return "IDENTICAL"
    elif diff_count == 1:
        return "CLOSE"
    else:
        return "DIFFERENT"