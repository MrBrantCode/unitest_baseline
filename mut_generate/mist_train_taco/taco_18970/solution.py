"""
QUESTION:
Email address in Berland is a string of the form A@B, where A and B are arbitrary strings consisting of small Latin letters. 

Bob is a system administrator in «Bersoft» company. He keeps a list of email addresses of the company's staff. This list is as a large string, where all addresses are written in arbitrary order, separated by commas. The same address can be written more than once.

Suddenly, because of unknown reasons, all commas in Bob's list disappeared. Now Bob has a string, where all addresses are written one after another without any separators, and there is impossible to determine, where the boundaries between addresses are. Unfortunately, on the same day his chief asked him to bring the initial list of addresses. Now Bob wants to disjoin addresses in some valid way. Help him to do that.

Input

The first line contains the list of addresses without separators. The length of this string is between 1 and 200, inclusive. The string consists only from small Latin letters and characters «@».

Output

If there is no list of the valid (according to the Berland rules) email addresses such that after removing all commas it coincides with the given string, output No solution. In the other case, output the list. The same address can be written in this list more than once. If there are several solutions, output any of them.

Examples

Input

a@aa@a


Output

a@a,a@a


Input

a@a@a


Output

No solution


Input

@aa@a


Output

No solution
"""

def restore_email_list(email_string: str) -> str:
    # Split the input string by '@' to get components
    comps = email_string.split('@')
    
    # Check if the input string contains '@'
    if '@' not in email_string:
        return 'No solution'
    
    # Validate the components
    for i in range(len(comps)):
        if i == 0 or i == len(comps) - 1:
            if len(comps[i]) < 1:
                return 'No solution'
        elif len(comps[i]) < 2:
            return 'No solution'
    
    # If there are only two components, join them directly
    if len(comps) == 2:
        return '@'.join(comps)
    
    # Reconstruct the email addresses
    ans = []
    for i in range(len(comps) - 1):
        if i == 0:
            ans.append(comps[i] + '@' + comps[i + 1][:1])
        elif i == len(comps) - 2:
            ans.append(comps[i][1:] + '@' + comps[i + 1])
        else:
            ans.append(comps[i][1:] + '@' + comps[i + 1][:1])
    
    # Join the reconstructed email addresses with commas
    return ','.join(ans)