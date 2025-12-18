"""
QUESTION:
The height of the student was measured at the medical examination. Create a program that takes height data as input, creates a frequency distribution, and outputs it. The frequency distribution is divided into 6 classes in 5 cm increments, and the number of people is indicated by * (half-width asterisk). However, if the frequency (number of people) of that class is 0, output only the class heading.



Input

The input is given in the following format:


n
h1
h2
::
hn


The number of students n (1 ≤ n ≤ 40) is given to the first line, and the real number hi (150.0 ≤ hi ≤ 190.0, up to the first decimal place) representing the height of the i-th person is given to each line after the second line. ..

Output

Display the frequency distribution in the following format.


Line 1 Heading "1:" followed by * for people less than 165.0 cm *
2nd line Heading "2:" followed by people 165.0 cm or more and less than 170.0 cm *
3rd line Heading "3:" followed by the number of people from 170.0 cm or more to less than 175.0 cm *
4th line Heading "4:" followed by the number of people from 175.0 cm to less than 180.0 cm *
Line 5 Heading "5:" followed by the number of people between 180.0 cm and 185.0 cm *
Line 6 Heading "6:" followed by * for people over 185.0 cm *


Examples

Input

4
180.3
168.2
165.5
175.3


Output

1:
2:**
3:
4:*
5:*
6:


Input

21
179.4
171.5
156.6
173.0
169.4
181.2
172.4
170.0
163.6
165.9
173.5
168.2
162.5
172.0
175.1
172.3
167.5
175.9
186.2
168.0
178.6


Output

1:***
2:*****
3:*******
4:****
5:*
6:*
"""

def generate_height_frequency_distribution(heights):
    # Initialize the frequency distribution list with 6 zeros
    ranks = [0] * 6
    
    # Calculate the frequency for each class
    for h in heights:
        if h < 160.0:
            h = 160.0
        if h >= 190.0:
            h = 189.9
        pos = int((h - 160.0) / 5)
        ranks[pos] += 1
    
    # Generate the output format
    result = []
    for i, f in enumerate(ranks):
        result.append('{}:{}'.format(i + 1, '*' * f))
    
    return result