"""
QUESTION:
You are given a message string S consisting of lowercase English alphabet letters. "ada" is a noise word and all the words that can be formed by adding “da” any number of times at the end of any noise word is also considered as a noise word. For example, the words “adada”, “adadadadada”, ”adada” are noise words but “dada”, ”ad”, ”aad” are not considered noise words.
You have to move all the noise words present in the message signal to the end of the message (in the same order as they occur in the message S) so that the filter can truncate the noise from the end.
Example 1:
Input:
S = "heyadadahiadahi"
Output: "heyhihiadadaada" 
Explanation: ”adada” and “ada” are the 
noise words. Noises are moved to the end 
in the same order as they appear in the 
string S.
Example 2:
Input:
S = "heyheyhello"
Output: "heyheyhello"
Explanation: There is no noise in the signal.
Your Task:
You need not take any input or print anything. Your task is to complete the function updateString() which takes string S as input parameter and returns the message string with noise words at the end. 
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).
Constraints:
1 ≤ length (string) ≤ 10^5
"""

def filter_noise_words(S: str) -> str:
    noise = ''
    output = ''
    i = 0
    j = 0
    while i < len(S):
        if S[i:i + 3] == 'ada':
            output += S[j:i]
            j = i
            i += 3
            while i + 1 < len(S) and S[i:i + 2] == 'da':
                i += 2
            noise += S[j:i]
            j = i
        else:
            i += 1
    output += S[j:i]
    return output + noise