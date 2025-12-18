"""
QUESTION:
Having stayed home alone, Petya decided to watch forbidden films on the Net in secret. "What ungentlemanly behavior!" — you can say that, of course, but don't be too harsh on the kid. In his country films about the Martians and other extraterrestrial civilizations are forbidden. It was very unfair to Petya as he adored adventure stories that featured lasers and robots. 

Today Petya is watching a shocking blockbuster about the Martians called "R2:D2". What can "R2:D2" possibly mean? It might be the Martian time represented in the Martian numeral system. Petya knows that time on Mars is counted just like on the Earth (that is, there are 24 hours and each hour has 60 minutes). The time is written as "a:b", where the string a stands for the number of hours (from 0 to 23 inclusive), and string b stands for the number of minutes (from 0 to 59 inclusive). The only thing Petya doesn't know is in what numeral system the Martian time is written.

Your task is to print the radixes of all numeral system which can contain the time "a:b".

Input

The first line contains a single string as "a:b" (without the quotes). There a is a non-empty string, consisting of numbers and uppercase Latin letters. String a shows the number of hours. String b is a non-empty string that consists of numbers and uppercase Latin letters. String b shows the number of minutes. The lengths of strings a and b are from 1 to 5 characters, inclusive. Please note that strings a and b can have leading zeroes that do not influence the result in any way (for example, string "008:1" in decimal notation denotes correctly written time).

We consider characters 0, 1, ..., 9 as denoting the corresponding digits of the number's representation in some numeral system, and characters A, B, ..., Z correspond to numbers 10, 11, ..., 35.

Output

Print the radixes of the numeral systems that can represent the time "a:b" in the increasing order. Separate the numbers with spaces or line breaks. If there is no numeral system that can represent time "a:b", print the single integer 0. If there are infinitely many numeral systems that can represent the time "a:b", print the single integer -1.

Note that on Mars any positional numeral systems with positive radix strictly larger than one are possible.

Examples

Input

11:20


Output

3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22

Input

2A:13


Output

0


Input

000B:00001


Output

-1

Note

Let's consider the first sample. String "11:20" can be perceived, for example, as time 4:6, represented in the ternary numeral system or as time 17:32 in hexadecimal system. 

Let's consider the second sample test. String "2A:13" can't be perceived as correct time in any notation. For example, let's take the base-11 numeral notation. There the given string represents time 32:14 that isn't a correct time.

Let's consider the third sample. String "000B:00001" can be perceived as a correct time in the infinite number of numeral systems. If you need an example, you can take any numeral system with radix no less than 12.
"""

def find_valid_radixes(time_str: str) -> list or int:
    a, b = time_str.split(':')
    
    # Remove leading zeros
    a2 = a.lstrip('0')
    b2 = b.lstrip('0')
    
    # If all characters were zeros, keep one zero
    if not a2:
        a2 = '0'
    if not b2:
        b2 = '0'
    
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    apos = [values.index(char) for char in a2]
    bpos = [values.index(char) for char in b2]
    
    minradix = max(max(apos, default=0), max(bpos, default=0))
    
    results = []
    
    for radix in range(minradix + 1, 60):
        aresult = sum(apos[j] * radix ** (len(apos) - j - 1) for j in range(len(apos)))
        bresult = sum(bpos[j] * radix ** (len(bpos) - j - 1) for j in range(len(bpos)))
        
        if aresult <= 23 and bresult <= 59:
            results.append(radix)
    
    if len(results) == 0:
        return 0
    elif (len(a2) == 1 and len(b2) == 1 and values.index(a2) <= 23 and values.index(b2) <= 59) or (apos == [0] and bpos == [0]):
        return -1
    else:
        return results