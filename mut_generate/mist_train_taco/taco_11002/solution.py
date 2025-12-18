"""
QUESTION:
At the legendary times of Nonsenso wars in ISM Dhanbad, there was a neck to neck competition between Barney Stinson and Sheldon Cooper. They both were on level 19. After trying too hard both of them could not decipher the nonsense, so they decided to play alongside. Sheldon Cooper had to pass a message to Barney Stinson. So he decided to convert each letter of the sentence to their corresponding to their ASCII codes. When Barney received the message he could not get anything. Now you have to design a code which converts the encrypted message to readable format.

-----Input-----
The input will consist of the first line containing the number of test cases ‘n’ followed by n lines of test cases.

-----Output-----

For each input print the decoded line.

-----Example-----
Input:
2
721011081081113287111114108100
871011089911110910132116111327311010010597

Output:
Hello World
Welcome to India
"""

def decode_message(test_cases):
    decoded_messages = []
    
    for code in test_cases:
        code = code.strip() + '0'
        message = ''
        asc = int(code[0])
        
        for i in range(len(code) - 1):
            if int(str(asc) + code[i + 1]) > 256:
                message += chr(asc)
                asc = int(code[i + 1])
            else:
                asc = int(str(asc) + code[i + 1])
        
        decoded_messages.append(message)
    
    return decoded_messages