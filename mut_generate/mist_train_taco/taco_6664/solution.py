"""
QUESTION:
A function receives a certain numbers of integers ```n1, n2, n3 ..., np```(all positive and different from 0) and a factor ```k, k > 0```

The function rearranges the numbers ```n1, n2, ..., np``` in such order that generates the minimum number concatenating the digits and this number should be divisible by ```k```.

The order that the function receives their arguments is:
```python
rearranger(k, n1, n2, n3,....,np)
```

## Examples

```python
rearranger(4, 32, 3, 34, 7, 12)  == "Rearrangement: 12, 3, 34, 7, 32 generates: 12334732 divisible by 4"

rearranger(10, 32, 3, 34, 7, 12) == "There is no possible rearrangement"
```
If there are more than one possible arrengement for the same minimum number, your code should be able to handle those cases:
```python
rearranger(6, 19, 32, 2, 124, 20, 22) == "Rearrangements: 124, 19, 20, 2, 22, 32 and 124, 19, 20, 22, 2, 32 generates: 124192022232 divisible by 6"
```

The arrangements should be in sorted order, as you see: `124, 19, 20, 2, 22, 32` comes first than `124, 19, 20, 22, 2, 32`.

Have an enjoyable time!

(Thanks to `ChristianE.Cooper` for his contribution to this kata)
"""

from itertools import permutations

def find_min_divisible_rearrangement(k, *args):
    perms = permutations(map(str, args), len(args))
    divisible_by_k = list(filter(lambda x: int(''.join(x)) % k == 0, perms))
    
    if not divisible_by_k:
        return 'There is no possible rearrangement'
    
    min_number = min(divisible_by_k, key=lambda x: int(''.join(x)))
    min_number_str = ''.join(min_number)
    
    # Find all permutations that generate the same minimum number
    same_min_perms = [perm for perm in divisible_by_k if ''.join(perm) == min_number_str]
    
    if len(same_min_perms) == 1:
        return 'Rearrangement: {} generates: {} divisible by {}'.format(
            ', '.join(min_number), min_number_str, k)
    else:
        sorted_perms = sorted(', '.join(perm) for perm in same_min_perms)
        return 'Rearrangements: {} and {} generates: {} divisible by {}'.format(
            sorted_perms[0], sorted_perms[1], min_number_str, k)