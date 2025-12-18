"""
QUESTION:
Peter decided to wish happy birthday to his friend from Australia and send him a card. To make his present more mysterious, he decided to make a chain. Chain here is such a sequence of envelopes A = {a1, a2, ..., an}, where the width and the height of the i-th envelope is strictly higher than the width and the height of the (i - 1)-th envelope respectively. Chain size is the number of envelopes in the chain. 

Peter wants to make the chain of the maximum size from the envelopes he has, the chain should be such, that he'll be able to put a card into it. The card fits into the chain if its width and height is lower than the width and the height of the smallest envelope in the chain respectively. It's forbidden to turn the card and the envelopes. 

Peter has very many envelopes and very little time, this hard task is entrusted to you.

Input

The first line contains integers n, w, h (1 ≤ n ≤ 5000, 1 ≤ w, h ≤ 106) — amount of envelopes Peter has, the card width and height respectively. Then there follow n lines, each of them contains two integer numbers wi and hi — width and height of the i-th envelope (1 ≤ wi, hi ≤ 106).

Output

In the first line print the maximum chain size. In the second line print the numbers of the envelopes (separated by space), forming the required chain, starting with the number of the smallest envelope. Remember, please, that the card should fit into the smallest envelope. If the chain of maximum size is not unique, print any of the answers.

If the card does not fit into any of the envelopes, print number 0 in the single line.

Examples

Input

2 1 1
2 2
2 2


Output

1
1 


Input

3 3 3
5 4
12 11
9 8


Output

3
1 3 2
"""

def find_max_envelope_chain(n, w, h, envelopes):
    # Filter envelopes that can fit the card
    valid_envelopes = [(wi, hi, wi * hi, i + 1) for i, (wi, hi) in enumerate(envelopes) if wi > w and hi > h]
    
    if not valid_envelopes:
        return 0, []
    
    # Sort envelopes by their area (width * height)
    valid_envelopes.sort(key=lambda x: x[2])
    
    # Initialize arrays for chain lengths and back pointers
    chain_lengths = [1] * len(valid_envelopes)
    back_pointers = [-1] * len(valid_envelopes)
    
    # Dynamic programming to find the longest chain
    for i in range(len(valid_envelopes)):
        for j in range(i):
            if (valid_envelopes[i][0] > valid_envelopes[j][0] and 
                valid_envelopes[i][1] > valid_envelopes[j][1] and 
                chain_lengths[j] + 1 > chain_lengths[i]):
                chain_lengths[i] = chain_lengths[j] + 1
                back_pointers[i] = j
    
    # Find the maximum chain length and its index
    max_chain_length = max(chain_lengths)
    max_index = chain_lengths.index(max_chain_length)
    
    # Reconstruct the chain indices
    chain_indices = []
    while max_index != -1:
        chain_indices.append(valid_envelopes[max_index][3])
        max_index = back_pointers[max_index]
    
    chain_indices.reverse()
    
    return max_chain_length, chain_indices