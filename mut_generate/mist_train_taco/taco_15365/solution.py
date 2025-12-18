"""
QUESTION:
In the International System of Units (SI), various physical quantities are expressed in the form of "numerical value + prefix + unit" using prefixes such as kilo, mega, and giga. For example, "3.5 kilometers", "5.1 milligrams", and so on.

On the other hand, these physical quantities can be expressed as "3.5 * 10 ^ 3 meters" and "5.1 * 10 ^ -3 grams" using exponential notation.

Measurement of physical quantities always includes errors. Therefore, there is a concept of significant figures to express how accurate the measured physical quantity is. In the notation considering significant figures, the last digit may contain an error, but the other digits are considered reliable. For example, if you write "1.23", the true value is 1.225 or more and less than 1.235, and the digits with one decimal place or more are reliable, but the second decimal place contains an error. The number of significant digits when a physical quantity is expressed in the form of "reliable digit + 1 digit including error" is called the number of significant digits. For example, "1.23" has 3 significant digits.

If there is a 0 before the most significant non-zero digit, that 0 is not included in the number of significant digits. For example, "0.45" has two significant digits. If there is a 0 after the least significant non-zero digit, whether or not that 0 is included in the number of significant digits depends on the position of the decimal point. If there is a 0 to the right of the decimal point, that 0 is included in the number of significant digits. For example, "12.300" has 5 significant digits. On the other hand, when there is no 0 to the right of the decimal point like "12300", it is not clear whether to include the 0 on the right side in the number of significant digits, but it will be included in this problem. That is, the number of significant digits of "12300" is five.

Natsume was given a physics problem as a school task. I have to do calculations related to significant figures and units, but the trouble is that I still don't understand how to use significant figures and units. Therefore, I would like you to create a program that automatically calculates them and help Natsume.

What you write is a program that, given a prefixed notation, converts it to exponential notation with the same number of significant digits. The following 20 prefixes are used.

* yotta = 10 ^ 24
* zetta = 10 ^ 21
* exa = 10 ^ 18
* peta = 10 ^ 15
* tera = 10 ^ 12
* giga = 10 ^ 9
* mega = 10 ^ 6
* kilo = 10 ^ 3
* hecto = 10 ^ 2
* deca = 10 ^ 1
* deci = 10 ^ -1
* centi = 10 ^ -2
* milli = 10 ^ -3
* micro = 10 ^ -6
* nano = 10 ^ -9
* pico = 10 ^ -12
* femto = 10 ^ -15
* ato = 10 ^ -18
* zepto = 10 ^ -21
* yocto = 10 ^ -24

Notes on Submission

Multiple datasets are given in the above format. The first line of input data gives the number of datasets. Create a program that outputs the output for each data set in order in the above format.



Input

The input consists of only one line, which contains numbers, unit prefixes (if any), and units. Each is separated by a blank. In some cases, there is no unit prefix, in which case only numbers and units are included in the line. Units with the same name as the unit prefix do not appear. The most significant digit is never 0, except for the ones digit when a decimal is given. The number given is positive. The number given is 1000 digits or less including the decimal point, and the unit name is 50 characters or less.

Output

Output the quantity expressed in exponential notation in the form of a * 10 ^ b [unit]. However, 1 <= a <10. The difference between the singular and plural forms of the unit name is not considered. Output the unit name given to the input as it is.

Example

Input

7
12.3 kilo meters
0.45 mega watts
0.000000000000000000000001 yotta grams
1000000000000000000000000 yocto seconds
42 amperes
0.42 joules
1234.56789012345678901234567890 hecto pascals


Output

1.23 * 10^4 meters
4.5 * 10^5 watts
1 * 10^0 grams
1.000000000000000000000000 * 10^0 seconds
4.2 * 10^1 amperes
4.2 * 10^-1 joules
1.23456789012345678901234567890 * 10^5 pascals
"""

def convert_to_exponential_notation(value_with_prefix: str, prefix_dict: dict = None) -> str:
    if prefix_dict is None:
        prefix_dict = {
            'yotta': 24, 'zetta': 21, 'exa': 18, 'peta': 15, 'tera': 12, 'giga': 9, 'mega': 6, 
            'kilo': 3, 'hecto': 2, 'deca': 1, 'deci': -1, 'centi': -2, 'milli': -3, 'micro': -6, 
            'nano': -9, 'pico': -12, 'femto': -15, 'ato': -18, 'zepto': -21, 'yocto': -24
        }
    
    (v, *b) = value_with_prefix.split()
    if len(b) == 2:
        (k, b) = (b[0], b[1])
        a = prefix_dict[k]
    else:
        b = b[0]
        a = 0
    
    s = 0
    for i in range(len(v)):
        if v[i] in '123456789':
            if i != 0:
                a -= i - 1
                if i != len(v) - 1:
                    v = v[i] + '.' + v[i + 1:]
                else:
                    v = v[i]
            else:
                try:
                    j = v[i:].index('.')
                    a += j - 1
                    v = v[0] + '.' + v[1:j] + v[j + 1:]
                except:
                    a += len(v) - 1
                    v = v[0] + '.' + v[1:]
            break
    
    return '{} * 10^{} {}'.format(v, a, b)