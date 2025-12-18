"""
QUESTION:
Implement the function `find_integers(word)` that takes a string `word` consisting of digits and lowercase English letters as input. The function should replace every non-digit character with a space, split the string into integers, and return a dictionary where the keys are the different integers and the values are their respective frequencies. Two integers are considered different if their decimal representations without any leading zeros are different. The length of `word` is between 1 and 1000.
"""

def find_integers(word):
    num = ""
    num_list = []
    num_dict = {}
  
    for char in word:
        if char.isdigit():
            num+=char
        else:
            num_list.append(num)
            num=""
  
    num_list.append(num)
    for n in num_list:
        if n.lstrip('0'):
            if n.lstrip('0') not in num_dict:
                num_dict[n.lstrip('0')] = 1
            else:
                num_dict[n.lstrip('0')] += 1
          
    return num_dict