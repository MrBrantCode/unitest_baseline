"""
QUESTION:
Write a program which counts and reports the number of each alphabetical letter. Ignore the case of characters.

Constraints

* The number of characters in the sentence < 1200

Input

A sentence in English is given in several lines.

Output

Prints the number of alphabetical letters in the following format:


a : The number of 'a'
b : The number of 'b'
c : The number of 'c'
.
.
z : The number of 'z'


Example

Input

This is a pen.


Output

a : 1
b : 0
c : 0
d : 0
e : 1
f : 0
g : 0
h : 1
i : 2
j : 0
k : 0
l : 0
m : 0
n : 1
o : 0
p : 1
q : 0
r : 0
s : 2
t : 1
u : 0
v : 0
w : 0
x : 0
y : 0
z : 0
"""

def count_alphabetical_letters(sentence: str) -> dict:
    # Convert the sentence to lowercase to ignore case
    sentence = sentence.lower()
    
    # Initialize a dictionary to store the counts of each letter
    letter_counts = {chr(i): 0 for i in range(97, 123)}
    
    # Count each letter in the sentence
    for char in sentence:
        if char in letter_counts:
            letter_counts[char] += 1
    
    return letter_counts