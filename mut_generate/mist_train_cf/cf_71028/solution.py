"""
QUESTION:
Write a function `common_substring(arr, k)` that takes an array of strings `arr` and an integer `k` as input, and returns the smallest occasional alphabetic substring that is common among at least `k` strings in the array. The substring must start and end with the same character.
"""

def rolling_hash(sub_string):
    hash_val = 0
    mod = 1e9 + 7  
    p = 31  
    p_pow = 1
    
    for ch in sub_string:
        hash_val = (hash_val + (ord(ch) - ord('a') + 1) * p_pow) % mod
        p_pow = (p_pow * p) % mod

    return hash_val

def common_substring(arr, k):
    hash_map = dict()
    for string in arr:
        for i in range(len(string)):
            for j in range(i, len(string)):
                if string[i] == string[j]:
                    sub_string = string[i:j+1]
                    hash_val = rolling_hash(sub_string)
                    if hash_val not in hash_map:
                        hash_map[hash_val] = [1, len(sub_string), sub_string]
                    else:
                        hash_map[hash_val][0] += 1
                        if len(sub_string) < hash_map[hash_val][1]:
                            hash_map[hash_val][1] = len(sub_string)
                            hash_map[hash_val][2] = sub_string

    result = ''
    min_len = float('inf')
    for value in hash_map.values():
        if value[0] >= k and value[1] < min_len:
            result = value[2]
            min_len = value[1]

    return result