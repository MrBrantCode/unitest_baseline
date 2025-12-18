"""
QUESTION:
When Sasha was studying in the seventh grade, he started listening to music a lot. In order to evaluate which songs he likes more, he introduced the notion of the song's prettiness. The title of the song is a word consisting of uppercase Latin letters. The prettiness of the song is the prettiness of its title.

Let's define the simple prettiness of a word as the ratio of the number of vowels in the word to the number of all letters in the word.

Let's define the prettiness of a word as the sum of simple prettiness of all the substrings of the word.

More formally, let's define the function vowel(c) which is equal to 1, if c is a vowel, and to 0 otherwise. Let s_{i} be the i-th character of string s, and s_{i}..j be the substring of word s, staring at the i-th character and ending at the j-th character (s_{is}_{i} + 1... s_{j}, i ≤ j).

Then the simple prettiness of s is defined by the formula:$\operatorname{simple}(s) = \frac{\sum_{i = 1}^{|s|} \operatorname{vowel}(s_{i})}{|s|}$

The prettiness of s equals $\sum_{1 \leq i \leq j \leq|s|} \operatorname{simple}(s_{i . . j})$

Find the prettiness of the given song title.

We assume that the vowels are I, E, A, O, U, Y.


-----Input-----

The input contains a single string s (1 ≤ |s| ≤ 5·10^5) — the title of the song.


-----Output-----

Print the prettiness of the song with the absolute or relative error of at most 10^{ - 6}.


-----Examples-----
Input
IEAIAIO

Output
28.0000000

Input
BYOB

Output
5.8333333

Input
YISVOWEL

Output
17.0500000



-----Note-----

In the first sample all letters are vowels. The simple prettiness of each substring is 1. The word of length 7 has 28 substrings. So, the prettiness of the song equals to 28.
"""

def calculate_song_prettiness(song_title: str) -> float:
    # Convert the song title into a list of boolean values indicating whether each character is a vowel
    ss = list(map(lambda c: c in 'IEAOUY', song_title))
    n = len(ss)
    
    # Initialize the weight array
    w = [0] * n
    
    # Calculate the initial weight for the first position
    w[0] = sum(1 / i for i in range(1, n + 1))
    
    # The weight for the last position is the same as the first position
    w[n - 1] = w[0]
    
    # Calculate the sigma value
    sigma = w[0]
    for i in range(1, (n - 1) // 2 + 1):
        sigma -= 1 / i + 1 / (n + 1 - i)
        w[n - i - 1] = w[i] = w[i - 1] + sigma
    
    # Calculate the prettiness of the song title
    ans = sum(ss[i] * w[i] for i in range(n))
    
    return ans