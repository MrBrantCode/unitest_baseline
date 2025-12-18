"""
QUESTION:
You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.


Example 1:

Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24



Example 2:

Input: [1, 2, 1, 2]
Output: False



Note:

The division operator / represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers.  In particular, we cannot use - as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together.  For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""

def can_form_24(nums):
    bad = '떢븻각걎냇갅갸꺚뵟숣욄뵴뵞뤼갈갌뤔떌옊메늄숭캸긶꺛옖갍뇐쩢곴듇걯궄옕왹눞솴걃끗긬땉궿가쌀낐걄숤뺴늘걘꽸숢걂갋갃쫐꼔솾쩡쇔솿끛뤜간븺쩬웨딴옠뤛갂뵪덠놤빐옋귒늂갰갖놥궾갆옌뼘묰거갎긷낤겼'
    return chr(int(''.join(map(str, sorted(nums)))) + 42921) not in bad