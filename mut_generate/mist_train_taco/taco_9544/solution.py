"""
QUESTION:
You are given a dataset consisting of $N$ items. Each item is a pair of a word and a boolean denoting whether the given word is a spam word or not.
We want to use this dataset for training our latest machine learning model. Thus we want to choose some subset of this dataset as training dataset. We want to make sure that there are no contradictions in our training set, i.e. there shouldn't be a word included in the training set that's marked both as spam and not-spam. For example item {"fck", 1}, and item {"fck, 0"} can't be present in the training set, because first item says the word "fck" is a spam, whereas the second item says it is not, which is a contradiction.
Your task is to select the maximum number of items in the training set.
Note that same pair of {word, bool} can appear multiple times in input. The training set can also contain the same pair multiple times.

-----Input-----
- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains a string $w_i$, followed by a space and an integer(boolean) $s_i$, denoting the $i$-th item.

-----Output-----
For each test case, output an integer corresponding to the maximum number of items that can be included in the training set in a single line.

-----Constraints-----
- $1 \le T \le 10$
- $1 \le N \le 25,000$
- $1 \le |w_i| \le 5$ for each valid $i$
- $0 \le s_i \le 1$ for each valid $i$
- $w_1, w_2, \ldots, w_N$ contain only lowercase English letters

-----Example Input-----
3
3
abc 0
abc 1
efg 1
7
fck 1
fck 0
fck 1
body 0
body 0
body 0
ram 0
5
vv 1
vv 0
vv 0
vv 1
vv 1

-----Example Output-----
2
6
3

-----Explanation-----
Example case 1: You can include either of the first and the second item, but not both. The third item can also be taken. This way the training set can contain at the very max 2 items.
Example case 2: You can include all the items except the second item in the training set.
"""

def max_training_set_size(test_cases):
    results = []
    
    for case in test_cases:
        word_count = {}
        
        # Count occurrences of each word with its spam status
        for word, is_spam in case:
            key = f"{word} {is_spam}"
            if key in word_count:
                word_count[key] += 1
            else:
                word_count[key] = 1
        
        max_items = 0
        
        # Process each word to find the maximum non-contradictory items
        for key in list(word_count.keys()):
            if word_count[key] == 0:
                continue
            
            word, is_spam = key.rsplit(' ', 1)
            opposite_key = f"{word} {1 - int(is_spam)}"
            
            if opposite_key in word_count:
                max_items += max(word_count[key], word_count[opposite_key])
                word_count[key] = word_count[opposite_key] = 0
            else:
                max_items += word_count[key]
                word_count[key] = 0
        
        results.append(max_items)
    
    return results