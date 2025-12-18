"""
QUESTION:
Write a function `countCatFaces` that takes a single parameter `inputStr`, a string representing ASCII art, and returns the number of times the cat's face pattern appears in the input string. The cat's face pattern is a 7-line string:
```
                              _ooOoo_
                             o8888888o
                             88" . "88
                             (| -_- |)
                             O\  =  /O
                          ____/`---'\____
```
The function should count each occurrence of the cat's face in the input string, regardless of position.
"""

def countCatFaces(inputStr: str) -> int:
    cat_face = '''
                              _ooOoo_
                             o8888888o
                             88" . "88
                             (| -_- |)
                             O\  =  /O
                          ____/`---'\____
    '''
    cat_lines = cat_face.strip().split('\n')
    input_lines = inputStr.strip().split('\n')
    cat_length = len(cat_lines)
    count = sum(1 for i in range(len(input_lines) - cat_length + 1) if input_lines[i:i+cat_length] == cat_lines)
    return count