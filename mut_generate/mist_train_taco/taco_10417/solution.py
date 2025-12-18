"""
QUESTION:
You are given a string s and should process m queries. Each query is described by two 1-based indices l_{i}, r_{i} and integer k_{i}. It means that you should cyclically shift the substring s[l_{i}... r_{i}] k_{i} times. The queries should be processed one after another in the order they are given.

One operation of a cyclic shift (rotation) is equivalent to moving the last character to the position of the first character and shifting all other characters one position to the right.

For example, if the string s is abacaba and the query is l_1 = 3, r_1 = 6, k_1 = 1 then the answer is abbacaa. If after that we would process the query l_2 = 1, r_2 = 4, k_2 = 2 then we would get the string baabcaa.


-----Input-----

The first line of the input contains the string s (1 ≤ |s| ≤ 10 000) in its initial state, where |s| stands for the length of s. It contains only lowercase English letters.

Second line contains a single integer m (1 ≤ m ≤ 300) — the number of queries.

The i-th of the next m lines contains three integers l_{i}, r_{i} and k_{i} (1 ≤ l_{i} ≤ r_{i} ≤ |s|, 1 ≤ k_{i} ≤ 1 000 000) — the description of the i-th query.


-----Output-----

Print the resulting string s after processing all m queries.


-----Examples-----
Input
abacaba
2
3 6 1
1 4 2

Output
baabcaa



-----Note-----

The sample is described in problem statement.
"""

def process_cyclic_shifts(s: str, queries: list) -> str:
    """
    Process a series of cyclic shift queries on a given string.

    Parameters:
    - s (str): The initial string.
    - queries (list): A list of tuples where each tuple contains three integers (l, r, k).
                      Each tuple represents a query to cyclically shift the substring s[l...r] k times.
                      Indices l and r are 1-based.

    Returns:
    - str: The resulting string after processing all queries.
    """
    
    class ShiftCommand:
        def __init__(self, left, right, shift_step):
            self.left = left
            self.right = right
            self.shift_range = self.right - self.left
            self.shift_step = self._remove_circles(shift_step)

        def _remove_circles(self, shift_step):
            return shift_step % self.shift_range

        def apply_command(self, characters):
            buff = characters[self.left:self.right]
            for i in range(self.left, self.right):
                characters[i] = buff[(i - self.left - self.shift_step) % self.shift_range]
            return characters

    characters = list(s)
    for query in queries:
        l, r, k = query
        command = ShiftCommand(l - 1, r, k)
        characters = command.apply_command(characters)
    
    return ''.join(characters)