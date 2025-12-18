"""
QUESTION:
In the world of Latin Alphabets, there seemed to be a catastrophe! All the vowels went missing. The other alphabets got disturbed and began the search operation.
While searching they stumbled upon a garbage of letters. Can you help them find if the this garbage contains ALL the vowels ?  

Input:
FIrst line contains N , the size of the garbage of letters.
Second line contains the letters (only lowercase).  

Output:
Print "YES" (without the quotes) if all vowels are found in the garbage, "NO" (without the quotes) otherwise.   

Constraints:
1 ≤ N ≤ 10000  

SAMPLE INPUT
8
atuongih

SAMPLE OUTPUT
NO
"""

def contains_all_vowels(N: int, letters: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    found_vowels = set()
    
    for char in letters:
        if char in vowels:
            found_vowels.add(char)
    
    if found_vowels == vowels:
        return "YES"
    else:
        return "NO"