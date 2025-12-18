"""
QUESTION:
In a far away country called AlgoLandia, there are `N` islands numbered `1` to `N`. Each island is denoted by `k[i]`. King Algolas, king of AlgoLandia, built `N - 1` bridges in the country. A bridge is built between islands `k[i]` and `k[i+1]`. Bridges are two-ways and are expensive to build.

The problem is that there are gangs who wants to destroy the bridges. In order to protect the bridges, the king wants to assign elite guards to the bridges. A bridge between islands `k[i]` and `k[i+1]` is safe when there is an elite guard in island `k[i]` or `k[i+1]`. There are already elite guards assigned in some islands.

Your task now is to determine the minimum number of additional elite guards that needs to be hired to guard all the bridges.

### Note:
You are given a sequence `k` with `N` length.
`k[i] = true`, means that there is an elite guard in that island; `k[i] = false` means no elite guard. It is guaranteed that AlgoLandia have at least `2` islands.

### Sample Input 1
```
k = [true, true, false, true, false]
```

### Sample Output 1
```
0
```

### Sample Input 2
```
k = [false, false, true, false, false]
```
### Sample Output 2
```
2
```
"""

def calculate_minimum_guards(islands):
    # Initialize the count of additional guards needed
    additional_guards = 0
    
    # Iterate through the islands to find segments of consecutive islands without guards
    i = 0
    while i < len(islands):
        if not islands[i]:  # If the current island does not have a guard
            # Start of a segment without guards
            start = i
            # Find the end of this segment
            while i < len(islands) and not islands[i]:
                i += 1
            # Calculate the length of this segment
            segment_length = i - start
            # Each segment of length L needs (L + 1) // 2 guards
            additional_guards += (segment_length + 1) // 2
        else:
            i += 1
    
    return additional_guards