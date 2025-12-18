"""
QUESTION:
A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help. 

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, $\boldsymbol{\mathrm{~S~}}$, determine how many letters of the SOS message have been changed by radiation.

Example  

$s=\text{'SOSTOT'}$  

The original message was SOSSOS.  Two of the message's characters were changed in transit.  

Function Description

Complete the marsExploration function in the editor below.  

marsExploration has the following parameter(s):

string s: the string as received on Earth  

Returns  

int: the number of letters changed during transmission  

Input Format

There is one line of input: a single string, $\boldsymbol{\mathrm{~S~}}$. 

Constraints

$1\leq\ \text{length of}\ s\leq99$
$\textbf{length of}~s~\textbf{modulo}~~3=0$
$\boldsymbol{\mathrm{~S~}}$ will contain only uppercase English letters, ascii[A-Z].

Sample Input 0
SOSSPSSQSSOR

Sample Output 0
3

Explanation 0

$\boldsymbol{\mathrm{~S~}}$ = SOSSPSSQSSOR, and signal length $\textbf{|s|}=\textbf{12}$. They sent $4$ SOS messages (i.e.: $12/3=4$).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR
Difference:          X  X   X

Sample Input 1
SOSSOT

Sample Output 1
1

Explanation 1

$\boldsymbol{\mathrm{~S~}}$ = SOSSOT, and signal length $|s|=6$. They sent $2$ SOS messages (i.e.: $6/3=2$).

Expected Signal: SOSSOS     
Received Signal: SOSSOT
Difference:           X

Sample Input 2
SOSSOSSOS

Sample Output 2
0

Explanation 2

Since no character is altered, return 0.
"""

def mars_exploration(s: str) -> int:
    # Calculate the expected SOS message
    expected_message = 'SOS' * (len(s) // 3)
    
    # Initialize a counter for altered characters
    altered_count = 0
    
    # Compare each character in the received message with the expected message
    for i in range(len(s)):
        if s[i] != expected_message[i]:
            altered_count += 1
    
    return altered_count