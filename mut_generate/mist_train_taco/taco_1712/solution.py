"""
QUESTION:
When multiple master devices are connected to a single bus (https://en.wikipedia.org/wiki/System_bus), there needs to be an arbitration in order to choose which of them can have access to the bus (and 'talk' with a slave).

We implement here a very simple model of bus mastering. Given `n`, a number representing the number of **masters** connected to the bus, and a fixed priority order (the first master has more access priority than the second and so on...), the task is to choose the selected master.
In practice, you are given a string `inp` of length `n` representing the `n` masters' requests to get access to the bus, and you should return a string representing the masters, showing which (only one) of them was granted access:

```
The string 1101 means that master 0, master 1 and master 3 have requested
access to the bus. 
Knowing that master 0 has the greatest priority, the output of the function should be: 1000
```

## Examples

## Notes

* The resulting string (`char* `) should be allocated in the `arbitrate` function, and will be free'ed in the tests.

* `n` is always greater or equal to 1.
"""

def arbitrate_bus_access(inp, n):
    # Find the index of the first '1' in the input string
    first_request_index = inp.find('1')
    
    # If no master requested access, return a string of '0's
    if first_request_index == -1:
        return '0' * n
    
    # Create the result string with '1' at the position of the highest priority master
    # and '0's for all other positions
    result = ['0'] * n
    result[first_request_index] = '1'
    
    return ''.join(result)