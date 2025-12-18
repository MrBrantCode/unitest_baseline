"""
QUESTION:
Arjit has his own printing press, Bainik Dhaskar (BD). He feels that words on their own simply aren't beautiful enough. So, he wishes to make a Super Manuscript (SM) machine. Now what does this machine do?
The SM machine aims to make words as beautiful as they can be by making a word as lexicographically small as possible. Arjit, being the resourceful person he is, has a reserve string from which we can choose characters that will replace characters in the original word that BD's SM machine wishes to transform.
Keep in mind that once you have used a letter in the reserve string, it is removed from the reserve.
As Arjit is busy with other work at BD, it's your work to take care of programming SM :)
Note that you cannot modify the original order of the letters in the word that has to be transformed. You can only replace its letters with those in the reserve.  

Input:
The first line of input contains T. T test cases follow.
Each test case has 2 lines.
The first line of each test case has the word W, that has to be transformed.
The second line of each test case has a reserve R from which we will pick letters.  

Output:
The output should contain T lines with the answer to each test on a new line.
Print a word P which is the lexicographically smallest that can be obtained on replacing letters of W with letters from R.

Constraints:
1 ≤ T ≤ 10
1 ≤ |W| ≤ 10  ^4 
1 ≤ |R| ≤ 10  ^4 
W and R will contain only lowercase characters.  

See the example to understand this better.

SAMPLE INPUT
3
bbbb
aaa
zxewya
abcd
ac
zzzb

SAMPLE OUTPUT
aaab
abcdya
ab

Explanation

In the first test case, we have 3 a's, so we simply replace the first 3 letters of the word.
In the second test case, again we just replace the first 4 letters with 'a', 'b', 'c' and 'd'.
In the third case, 'b' is lexicographically smaller than 'c', so 'ac' becomes 'ab'.
"""

def transform_word_to_lexicographically_smallest(word: str, reserve: str) -> str:
    # Sort the reserve string to get characters in lexicographical order
    sorted_reserve = sorted(reserve)
    
    # Initialize the transformed word with the original word
    transformed_word = list(word)
    
    # Index to track the position in the sorted reserve string
    reserve_index = 0
    
    # Length of the word and reserve string
    word_length = len(word)
    reserve_length = len(sorted_reserve)
    
    # Iterate through each character in the word
    for i in range(word_length):
        # If the current character in the word can be replaced by a smaller character from the reserve
        if reserve_index < reserve_length and transformed_word[i] > sorted_reserve[reserve_index]:
            transformed_word[i] = sorted_reserve[reserve_index]
            reserve_index += 1
        
        # If we have used all characters from the reserve, break the loop
        if reserve_index == reserve_length:
            break
    
    # Join the list back into a string and return
    return ''.join(transformed_word)