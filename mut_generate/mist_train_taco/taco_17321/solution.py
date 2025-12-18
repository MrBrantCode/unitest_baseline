"""
QUESTION:
A long time ago, in a galaxy far far away two giant IT-corporations Pineapple and Gogol continue their fierce competition. Crucial moment is just around the corner: Gogol is ready to release it's new tablet Lastus 3000.

This new device is equipped with specially designed artificial intelligence (AI). Employees of Pineapple did their best to postpone the release of Lastus 3000 as long as possible. Finally, they found out, that the name of the new artificial intelligence is similar to the name of the phone, that Pineapple released 200 years ago. As all rights on its name belong to Pineapple, they stand on changing the name of Gogol's artificial intelligence.

Pineapple insists, that the name of their phone occurs in the name of AI as a substring. Because the name of technology was already printed on all devices, the Gogol's director decided to replace some characters in AI name with "#". As this operation is pretty expensive, you should find the minimum number of characters to replace with "#", such that the name of AI doesn't contain the name of the phone as a substring.

Substring is a continuous subsequence of a string.


-----Input-----

The first line of the input contains the name of AI designed by Gogol, its length doesn't exceed 100 000 characters. Second line contains the name of the phone released by Pineapple 200 years ago, its length doesn't exceed 30. Both string are non-empty and consist of only small English letters.


-----Output-----

Print the minimum number of characters that must be replaced with "#" in order to obtain that the name of the phone doesn't occur in the name of AI as a substring.


-----Examples-----
Input
intellect
tell

Output
1
Input
google
apple

Output
0
Input
sirisiri
sir

Output
2


-----Note-----

In the first sample AI's name may be replaced with "int#llect".

In the second sample Gogol can just keep things as they are.

In the third sample one of the new possible names of AI may be "s#ris#ri".
"""

def min_replacements_to_avoid_substring(ai_name: str, phone_name: str) -> int:
    # Initialize the count of replacements needed
    replacements = 0
    
    # Find the length of the phone name
    phone_len = len(phone_name)
    
    # Iterate over the ai_name to find occurrences of phone_name
    for i in range(len(ai_name) - phone_len + 1):
        # Check if the substring of ai_name matches phone_name
        if ai_name[i:i + phone_len] == phone_name:
            replacements += 1
    
    return replacements