"""
QUESTION:
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

```if:python
Complete the function `get_issuer()` that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string `Unknown`.
```
```if-not:python
Complete the function `getIssuer()` that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string `Unknown`.
```
```if:typescript
Where `Issuer` is defined with the following enum type.
~~~typescript
enum Issuer {
  VISA = 'VISA',
  AMEX = 'AMEX',
  Mastercard = 'Mastercard',
  Discover = 'Discover',
  Unknown = 'Unknown',
}
~~~
```

```markdown
| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      |
```

```if:c,cpp
**C/C++ note:** The return value in C is not freed.
```

## Examples

```if-not:python
~~~js
getIssuer(4111111111111111) == "VISA"
getIssuer(4111111111111) == "VISA"
getIssuer(4012888888881881) == "VISA"
getIssuer(378282246310005) == "AMEX"
getIssuer(6011111111111117) == "Discover"
getIssuer(5105105105105100) == "Mastercard"
getIssuer(5105105105105106) == "Mastercard"
getIssuer(9111111111111111) == "Unknown"
~~~
```
```if:python
~~~py
get_issuer(4111111111111111) == "VISA"
get_issuer(4111111111111) == "VISA"
get_issuer(4012888888881881) == "VISA"
get_issuer(378282246310005) == "AMEX"
get_issuer(6011111111111117) == "Discover"
get_issuer(5105105105105100) == "Mastercard"
get_issuer(5105105105105106) == "Mastercard"
get_issuer(9111111111111111) == "Unknown"
~~~
```
"""

def get_issuer(number):
    s = str(number)
    if len(s) == 15 and s[:2] in ('34', '37'):
        return 'AMEX'
    elif len(s) == 16 and s.startswith('6011'):
        return 'Discover'
    elif len(s) == 16 and s[0] == '5' and s[1] in '12345':
        return 'Mastercard'
    elif len(s) in [13, 16] and s[0] == '4':
        return 'VISA'
    else:
        return 'Unknown'