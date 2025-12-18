"""
QUESTION:
Write a function `sort_features` that takes two parameters: `features` and `responses`. 

`features` is a list of unique strings, each representing a feature, where each string consists of lowercase letters. 
`responses` is a list of strings, each containing space-separated words and consisting of lowercase letters and spaces.

The function should return the features in sorted order, first by their popularity (the number of responses that contain the feature) in descending order, then by their frequency (the total number of times they appear in all responses) in descending order, and finally by their original index in `features` in ascending order.
"""

def sort_features(features, responses):
    counts = {f: [0, 0, i] for i, f in enumerate(features)}
    for response in responses:
        seen = set()
        for word in response.split():
            if word not in counts:
                continue
            counts[word][1] += 1
            if word not in seen:
                counts[word][0] += 1
                seen.add(word)
    return [f for f, c in sorted(counts.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))]