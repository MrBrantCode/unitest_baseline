"""
QUESTION:
Create a program that converts data based on the given conversion table.

The characters used in the data are letters or numbers, and the letters are case sensitive. There is no regularity in the order of the characters that appear in the conversion table.

The conversion table has two characters (not a string), one before and one after, with a space in between. The conversion method is to convert the character before the line in the conversion table to the character after each time it appears in the data and output it. It is converted only once, and even if the converted character becomes the character to be converted again, it is not converted. Characters that do not appear in the conversion table are not converted and are output as they are.

In the input file, the conversion table (first n + 1 line) is followed by the data to be converted (n + 2nd line and after). The number of lines in the conversion table is n on the first line, each line of the following n lines is two characters with a blank, and then the number of lines of data to be converted on the n + second line m, and each line of the following m lines. Is a single character. Let m ≤ 105. Output should be one line without blanks or line breaks as in the output example.

Input example
---
3
A a
0 5
5 4
Ten
A
B
C
0
1
Four
Five
a
b b
A
Output example
aBC5144aba

input

The input consists of multiple datasets. Input ends when n is 0. The number of datasets does not exceed 5.

output

For each data set, the converted character string is output on one line.





Example

Input

3
A a
0 5
5 4
10
A
B
C
0
1
4
5
a
b
A
3
A a
0 5
5 4
10
A
B
C
0
1
4
5
a
b
A
0


Output

aBC5144aba
aBC5144aba
"""

def convert_data(conversion_table, data):
    # Create a dictionary from the conversion table
    conversion_dict = {before: after for before, after in conversion_table}
    
    # Convert the data based on the conversion dictionary
    converted_data = ''.join(conversion_dict.get(char, char) for char in data)
    
    return converted_data