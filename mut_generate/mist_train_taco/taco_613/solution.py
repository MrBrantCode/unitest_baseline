"""
QUESTION:
Construct a sequence a = {a_1,\ a_2,\ ...,\ a_{2^{M + 1}}} of length 2^{M + 1} that satisfies the following conditions, if such a sequence exists.
 - Each integer between 0 and 2^M - 1 (inclusive) occurs twice in a.
 - For any i and j (i < j) such that a_i = a_j, the formula a_i \ xor \ a_{i + 1} \ xor \ ... \ xor \ a_j = K holds.
What is xor (bitwise exclusive or)?
The xor of integers c_1, c_2, ..., c_n is defined as follows:
 - When c_1 \ xor \ c_2 \ xor \ ... \ xor \ c_n is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if the number of integers among c_1, c_2, ...c_m whose binary representations have 1 in the 2^k's place is odd, and 0 if that count is even.
For example, 3 \ xor \ 5 = 6. (If we write it in base two: 011 xor 101 = 110.)

-----Constraints-----
 - All values in input are integers.
 - 0 \leq M \leq 17
 - 0 \leq K \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
M K

-----Output-----
If there is no sequence a that satisfies the condition, print -1.
If there exists such a sequence a, print the elements of one such sequence a with spaces in between.
If there are multiple sequences that satisfies the condition, any of them will be accepted.

-----Sample Input-----
1 0

-----Sample Output-----
0 0 1 1

For this case, there are multiple sequences that satisfy the condition.
For example, when a = {0, 0, 1, 1}, there are two pairs (i,\ j)\ (i < j) such that a_i = a_j: (1, 2) and (3, 4). Since a_1 \ xor \ a_2 = 0 and a_3 \ xor \ a_4 = 0, this sequence a satisfies the condition.
"""

def construct_sequence(M: int, K: int) -> list:
    """
    Constructs a sequence a of length 2^(M + 1) that satisfies the given conditions, if such a sequence exists.

    Parameters:
    - M (int): The exponent used to determine the range of integers in the sequence.
    - K (int): The value used to check the XOR condition.

    Returns:
    - list: A list representing the sequence a if it exists, or -1 if no such sequence exists.
    """
    if K == 0:
        return [i // 2 for i in range(2 ** (M + 1))]
    elif K >= 2 ** M or M <= 1:
        return -1
    else:
        nums = []
        for i in range(2 ** M):
            if i != K:
                nums.append(i)
        a = [nums[0], K, nums[0]]
        b = []
        for i in range(1, 2 ** M - 1):
            b.append(nums[i])
        b.append(K)
        for i in range(1, 2 ** M - 1):
            b.append(nums[2 ** M - 1 - i])
        return a + b