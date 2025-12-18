"""
QUESTION:
You were strolling outside the restaurant at the end of the universe. On a metaspiral path you stumble upon a weird device which takes a three-digit number as input and processes it. The Hitchhiker's guide to the galaxy explains that it processes the input in the following manner: 
- Multiplies it with 13, followed by 11 and then 7          
- Outputs all the distinct three-digit numbers possible from the digits of the new number (each digit can only be used once)          
Your friend Zaphod is in a playful mood, and does the following with the device-           
- Given a three-digit positive number $K$, he feeds it to the device for processing.          
- He then takes the numbers it gives as output, and send each of them through the device and again collect all the numbers sent out.          
- Repeats the above step $N$ times.          
To test your wit, he challenges you to find the number of distinct 3-digit numbers which the device outputs over the $N$ steps. Can you?

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $K, N$.

-----Output:-----
For each testcase, output a single integer denoting the number of distinct 3-digit numbers which the device outputs over the $N$ steps.

-----Constraints-----
- $1 \leq T \leq 1000$ 
- $5 \leq N \leq 10^9$ 
- Each digit of $K$ is non-zero           

-----Sample Input:-----
1

123 5         

-----Sample Output:-----
27
"""

def count_distinct_numbers(K: str, N: int) -> int:
    # Convert K to a string if it's not already
    K = str(K)
    
    # Calculate the initial number after processing through the device
    processed_number = int(K) * 13 * 11 * 7
    processed_number_str = str(processed_number)
    
    # Extract distinct digits from the processed number
    distinct_digits = set(processed_number_str)
    
    # Calculate the number of distinct 3-digit numbers
    distinct_count = len(distinct_digits) ** 3
    
    # Since the process stabilizes after the first iteration, we only need to consider N=1
    return distinct_count