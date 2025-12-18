"""
QUESTION:
The name of our college is "Government College of Engineering and Textile Technology Berhampore". There is another college named "Government College of Engineering and Textile Technology Serampore". As the names are quite similar, those who are unaware of existence of both the colleges, often get confused. And mistake one with other.

Given a string, if it contains the word berhampore (case insensitive), print GCETTB or if it contains serampore(case-insensitive), print GCETTS . If the string contains neither print Others. If it contains both Berhampore and Serampore print Both 
Input 
- First line contains single integer T, No. of test case  
- Next line for every test contain case a string S 
Output

Print GCETTB or GCETTS or Others or Both on a new line
Constraints 
- 1 <= T <= 10 
- 0 <= len(S) <= 100  
- S contain a-z and A-Z and space only
Sample Input
3
Government clg Berhampore
SeRaMporE textile college 
Girls college Kolkata

Sample Output

GCETTB

GCETTS

Others       
Explanation

Self-Explanatory
"""

def identify_college(input_string: str) -> str:
    """
    Identifies the college based on the presence of 'berhampore' or 'serampore' in the input string.

    Parameters:
    - input_string (str): The string to be analyzed.

    Returns:
    - str: "GCETTB" if 'berhampore' is found, "GCETTS" if 'serampore' is found,
           "Both" if both are found, and "Others" if neither are found.
    """
    input_string = input_string.lower()
    berhampore = 'berhampore'
    serampore = 'serampore'
    
    contains_berhampore = berhampore in input_string
    contains_serampore = serampore in input_string
    
    if contains_berhampore and contains_serampore:
        return 'Both'
    elif contains_berhampore:
        return 'GCETTB'
    elif contains_serampore:
        return 'GCETTS'
    else:
        return 'Others'