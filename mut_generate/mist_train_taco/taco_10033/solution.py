"""
QUESTION:
International Carpenters Professionals Company (ICPC) is a top construction company with a lot of expert carpenters. What makes ICPC a top company is their original language.

The syntax of the language is simply given in CFG as follows:


S -> SS | (S) | )S( | ε


In other words, a right parenthesis can be closed by a left parenthesis and a left parenthesis can be closed by a right parenthesis in this language.

Alex, a grad student mastering linguistics, decided to study ICPC's language. As a first step of the study, he needs to judge whether a text is well-formed in the language or not. Then, he asked you, a great programmer, to write a program for the judgement.

Alex's request is as follows: You have an empty string S in the beginning, and construct longer string by inserting a sequence of '(' or ')' into the string. You will receive q queries, each of which consists of three elements (p, c, n), where p is the position to insert, n is the number of characters to insert and c is either '(' or ')', the character to insert. For each query, your program should insert c repeated by n times into the p-th position of S from the beginning. Also it should output, after performing each insert operation, "Yes" if S is in the language and "No" if S is not in the language.

Please help Alex to support his study, otherwise he will fail to graduate the college.



Input

The first line contains one integer q (1 \leq q \leq 10^5) indicating the number of queries, follows q lines of three elements, p_i, c_i, n_i, separated by a single space (1 \leq i \leq q, c_i = '(' or ')', 0 \leq p_i \leq  length of S before i-th query, 1 \leq n \leq 2^{20}). It is guaranteed that all the queries in the input are valid.

Output

For each query, output "Yes" if S is in the language and "No" if S is not in the language.

Examples

Input

3
0 ( 10
10 ) 5
10 ) 5


Output

No
No
Yes


Input

3
0 ) 10
10 ( 5
10 ( 5


Output

No
No
Yes


Input

3
0 ( 10
10 ) 20
0 ( 10


Output

No
No
Yes
"""

def check_icpc_language(q: int, queries: list) -> list:
    """
    Determines if the string S is in the ICPC language after each query.

    Parameters:
    q (int): The number of queries.
    queries (list): A list of tuples where each tuple contains three elements:
                    - p (int): The position to insert.
                    - c (str): The character to insert ('(' or ')').
                    - n (int): The number of times to insert the character.

    Returns:
    list: A list of strings where each string is either "Yes" or "No", indicating
          whether the string S is in the ICPC language after each query.
    """
    t = 0  # Balance counter
    results = []
    
    for query in queries:
        p, c, n = query
        if c == '(':
            t -= n
        else:
            t += n
        
        if t == 0:
            results.append('Yes')
        else:
            results.append('No')
    
    return results