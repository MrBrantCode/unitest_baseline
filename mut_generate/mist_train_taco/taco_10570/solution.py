"""
QUESTION:
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1.  If the count is 1, no digits will follow.  For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula.  For example, H2O2He3Mg4 is also a formula.  

A formula placed in parentheses, and a count (optionally added) is also a formula.  For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:

Input: 
formula = "H2O"
Output: "H2O"
Explanation: 
The count of elements are {'H': 2, 'O': 1}.



Example 2:

Input: 
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.



Example 3:

Input: 
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.



Note:
All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""

def count_atoms(formula: str) -> str:
    loc = 0
    lastloc = -1

    def getNext(formular, locked=False):
        nonlocal loc, lastloc
        stype = 0
        ret = 0
        if loc == lastloc:
            return (0, 0)
        i = loc
        while i < len(formular):
            if stype in (0, 1) and formular[i].isnumeric():
                ret = int(formular[i]) + ret * 10
                stype = 1
            elif stype == 0 and formular[i].isupper():
                stype = 20
                ret = formular[i]
            elif stype in (20, 2) and formular[i].islower():
                stype = 2
                ret += formular[i]
            elif stype == 0 and formular[i] in '()':
                stype = 3 + '()'.index(formular[i])
                ret = formular[i]
            else:
                break
            i += 1
        if not locked:
            lastloc = loc
            loc = i
        return (stype, ret)

    stk = []
    cnt = {}
    r = ''
    loc = 0
    n = getNext(formula)
    while n != (0, 0):
        if n[0] in (2, 3, 20):
            stk.append([n[1], 1])
        elif n[0] == 1:
            stk[-1][1] = n[1]
        elif n[0] == 4:
            time = 1
            i = -1
            if getNext(formula, True)[0] == 1:
                time = getNext(formula)[1]
            while stk[i][0] != '(':
                stk[i][1] *= time
                i -= 1
            stk[i][0] = '$'
        n = getNext(formula)
    while any(stk):
        n = stk.pop()
        if n[0] != '$':
            cnt[n[0]] = cnt.get(n[0], 0) + n[1]
    for i in sorted(cnt.keys()):
        r += '%s%d' % (i, cnt[i]) if cnt[i] > 1 else i
    return r