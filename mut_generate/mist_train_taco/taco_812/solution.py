"""
QUESTION:
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:


Input: 123
Output: "One Hundred Twenty Three"


Example 2:


Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:


Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Example 4:


Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

def number_to_words(num: int) -> str:
    V1 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    V2 = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    V3 = ['Thousand', 'Million', 'Billion']

    def convert_hundred(num: int) -> str:
        answer = ''
        a = num // 100
        b = num % 100
        c = num % 10
        if b < 20:
            answer = V1[b]
        else:
            following = ' ' + V1[c] if c > 0 else ''
            answer = V2[b // 10] + following
        if a > 0:
            following = ' ' + answer if answer else ''
            answer = V1[a] + ' Hundred' + following
        return answer

    if num == 0:
        return 'Zero'
    
    answer = convert_hundred(num % 1000)
    for i in range(3):
        num //= 1000
        if num % 1000 > 0:
            following = ' ' + answer if answer else ''
            answer = convert_hundred(num % 1000) + ' ' + V3[i] + following
    
    return answer