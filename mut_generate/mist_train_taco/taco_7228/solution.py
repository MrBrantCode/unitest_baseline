"""
QUESTION:
Given a string S containing only digits, Your task is to complete the function genIp() which returns a vector containing all possible combinations of valid IPv4 IP addresses and takes only a string S as its only argument.
Note: Order doesn't matter. A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.
For string 11211 the IP address possible are 
1.1.2.11
1.1.21.1
1.12.1.1
11.2.1.1
Example 1:
Input:
S = 1111
Output: 1.1.1.1
Example 2:
Input:
S = 55
Output: -1
Your Task:
Your task is to complete the function genIp() which returns a vector containing all possible combinations of valid IPv4 IP addresses or -1 if no such IP address could be generated through the input string S, the only argument to the function.
Expected Time Complexity: O(N * N * N)
Expected Auxiliary Space: O(N * N * N * N)
Constraints:
1<=N<=16
here, N = length of S.
S only contains digits(i.e. 0-9)
"""

def generate_ip_addresses(s: str) -> list:
    def is_valid_part(part: str) -> bool:
        """Helper function to check if a given part of the IP address is valid."""
        if len(part) == 0 or len(part) > 3 or (part[0] == '0' and len(part) > 1) or (int(part) > 255):
            return False
        return True

    n = len(s)
    if n > 12:
        return ['-1']
    
    valid_ips = []
    
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                part1 = s[0:i]
                part2 = s[i:j]
                part3 = s[j:k]
                part4 = s[k:n]
                
                if is_valid_part(part1) and is_valid_part(part2) and is_valid_part(part3) and is_valid_part(part4):
                    valid_ips.append(f"{part1}.{part2}.{part3}.{part4}")
    
    return valid_ips if valid_ips else ['-1']