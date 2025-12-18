"""
QUESTION:
This is a follow up from my kata Insert Dashes. 
Write a function ```insertDashII(num)``` that will insert dashes ('-') between each two odd numbers and asterisk ('\*') between each even numbers in ```num``` 
For example: 
```insertDashII(454793)``` --> 4547-9-3  
```insertDashII(1012356895)``` --> 10123-56*89-5 

Zero shouldn't be considered even or odd.
"""

def insert_dash_ii(num):
    prev = 0
    out = ''
    for dig in str(num):
        if int(dig) % 2 == int(prev) % 2 and int(prev) and int(dig):
            out += '*-'[int(prev) % 2]
        out += dig
        prev = dig
    return out