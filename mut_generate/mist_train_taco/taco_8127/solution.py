"""
QUESTION:
Tyndex is again well ahead of the rivals! The reaction to the release of Zoozle Chrome browser was the release of a new browser Tyndex.Brome!

The popularity of the new browser is growing daily. And the secret is not even the Tyndex.Bar installed (the Tyndex.Bar automatically fills the glass with the finest 1664 cognac after you buy Tyndex.Bottles and insert in into a USB port). It is highly popular due to the well-thought interaction with the user.

Let us take, for example, the system of automatic address correction. Have you entered codehorses instead of codeforces? The gloomy Zoozle Chrome will sadly say that the address does not exist. Tyndex.Brome at the same time will automatically find the closest address and sent you there. That's brilliant!

How does this splendid function work? That's simple! For each potential address a function of the F error is calculated by the following rules:

  * for every letter ci from the potential address c the closest position j of the letter ci in the address (s) entered by the user is found. The absolute difference |i - j| of these positions is added to F. So for every i (1 ≤ i ≤ |c|) the position j is chosen such, that ci = sj, and |i - j| is minimal possible. 
  * if no such letter ci exists in the address entered by the user, then the length of the potential address |c| is added to F. 



After the values of the error function have been calculated for all the potential addresses the most suitable one is found. 

To understand the special features of the above described method better, it is recommended to realize the algorithm of calculating the F function for an address given by the user and some set of potential addresses. Good luck!

Input

The first line contains two integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ 105). They are the number of potential addresses and the length of the address entered by the user. The next line contains k lowercase Latin letters. They are the address entered by the user (s). Each next i-th (1 ≤ i ≤ n) line contains a non-empty sequence of lowercase Latin letters. They are the potential address. It is guaranteed that the total length of all the lines does not exceed 2·105.

Output

On each n line of the output file print a single number: the value of the error function when the current potential address is chosen.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d).

Examples

Input

2 10
codeforces
codeforces
codehorses


Output

0
12


Input

9 9
vkontakte
vcontacte
vkontrakte
vkollapse
vkrokodile
vtopke
vkapuste
vpechke
vk
vcodeforcese


Output

18
14
36
47
14
29
30
0
84
"""

from bisect import bisect_left

def calculate_error_function(user_address, potential_addresses):
    # Initialize a dictionary to store positions of each character in the user_address
    char_positions = {chr(i): [] for i in range(ord('a'), ord('z') + 1)}
    
    # Populate the dictionary with positions of each character in the user_address
    for index, char in enumerate(user_address):
        char_positions[char].append(index)
    
    # Function to generate midpoints for binary search optimization
    def generate_midpoints(positions):
        return [(positions[i] + positions[i - 1]) // 2 for i in range(1, len(positions))]
    
    # Generate midpoints for each character
    midpoints = {char: generate_midpoints(positions) for char, positions in char_positions.items()}
    
    # Function to calculate the error for a single potential address
    def calculate_error(potential_address):
        error_sum = 0
        for index, char in enumerate(potential_address):
            if char_positions[char]:
                if midpoints[char]:
                    closest_index = bisect_left(midpoints[char], index)
                    error_sum += abs(index - char_positions[char][closest_index])
                else:
                    error_sum += abs(index - char_positions[char][0])
            else:
                error_sum += len(potential_address)
        return error_sum
    
    # Calculate the error for each potential address and store the results
    errors = [calculate_error(address) for address in potential_addresses]
    
    return errors