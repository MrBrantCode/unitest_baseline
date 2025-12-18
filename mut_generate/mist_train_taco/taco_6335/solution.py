"""
QUESTION:
Is there anything better than going to the zoo after a tiresome week at work? No wonder Grisha feels the same while spending the entire weekend accompanied by pretty striped zebras. 

Inspired by this adventure and an accidentally found plasticine pack (represented as a sequence of black and white stripes), Grisha now wants to select several consequent (contiguous) pieces of alternating colors to create a zebra. Let's call the number of selected pieces the length of the zebra.

Before assembling the zebra Grisha can make the following operation $0$ or more times. He splits the sequence in some place into two parts, then reverses each of them and sticks them together again. For example, if Grisha has pieces in the order "bwbbw" (here 'b' denotes a black strip, and 'w' denotes a white strip), then he can split the sequence as bw|bbw (here the vertical bar represents the cut), reverse both parts and obtain "wbwbb".

Determine the maximum possible length of the zebra that Grisha can produce.


-----Input-----

The only line contains a string $s$ ($1 \le |s| \le 10^5$, where $|s|$ denotes the length of the string $s$) comprised of lowercase English letters 'b' and 'w' only, where 'w' denotes a white piece and 'b' denotes a black piece.


-----Output-----

Print a single integer — the maximum possible zebra length.


-----Examples-----
Input
bwwwbwwbw

Output
5

Input
bwwbwwb

Output
3



-----Note-----

In the first example one of the possible sequence of operations is bwwwbww|bw $\to$ w|wbwwwbwb $\to$ wbwbwwwbw, that gives the answer equal to $5$.

In the second example no operation can increase the answer.
"""

def max_zebra_length(s: str) -> int:
    def check_longest(zebra: str) -> int:
        longest = 0
        curr = 0
        prev = 0
        for i in zebra:
            if ord(i) != prev:
                curr += 1
            else:
                if curr > longest:
                    longest = curr
                curr = 1
            prev = ord(i)
        if curr > longest:
            longest = curr
        return longest

    def finish(zebra: str, longest: int) -> int:
        temp = check_longest(zebra)
        if temp > longest:
            return temp
        else:
            return longest

    def flip(string: str) -> int:
        start = string[0]
        prev = start
        for i in range(1, len(string)):
            if string[i] == prev:
                if start != string[-1]:
                    string = string[0:i][::-1] + string[:i - 1:-1]
                    return flip(string)
                else:
                    return finish(string, longest)
            prev = string[i]
        return finish(string, longest)

    length = len(s)
    longest = check_longest(s)
    
    if longest == length:
        return longest
    if longest == length - 1:
        if s[0] == s[-1]:
            return longest
        else:
            return longest + 1
    
    return flip(s)