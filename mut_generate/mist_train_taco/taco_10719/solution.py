"""
QUESTION:
# Hey You !

Sort these integers for me ...

By name ...

Do it now !


---

## Input

* Range is ```0```-```999```

* There may be duplicates

* The array may be empty

## Example

* Input: 1, 2, 3, 4
* Equivalent names: "one", "two", "three", "four"
* Sorted by name: "four", "one", "three", "two"
* Output: 4, 1, 3, 2

## Notes
* Don't pack words together:
 * e.g. 99 may be "ninety nine" or "ninety-nine"; but not "ninetynine"
 * e.g 101 may be "one hundred one" or "one hundred and one"; but not "onehundredone"
* Don't fret about formatting rules, because if rules are consistently applied it has no effect anyway:
 * e.g. "one hundred one", "one hundred two"; is same order as "one hundred **and** one", "one hundred **and** two"
 * e.g. "ninety eight", "ninety nine"; is same order as "ninety-eight", "ninety-nine"
 
```if:c
* For `C` code the input array may be NULL. The return value is freed if non-NULL.
```
"""

def sort_integers_by_name(arr):
    def int_to_word(num):
        d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
        assert 0 <= num
        if num < 20:
            return d[num]
        if num < 100:
            if num % 10 == 0:
                return d[num]
            else:
                return d[num // 10 * 10] + '-' + d[num % 10]
        if num < 1000:
            if num % 100 == 0:
                return d[num // 100] + ' hundred'
            else:
                return d[num // 100] + ' hundred and ' + int_to_word(num % 100)
    
    return sorted(arr, key=int_to_word)