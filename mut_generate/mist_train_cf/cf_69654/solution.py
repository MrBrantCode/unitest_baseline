"""
QUESTION:
Create a function called `IntegerToWritten` that takes an integer `num` as input and returns its written form as a string. The function should handle numbers up to billions without using a massive look-up table. It should return the written form of the number with hyphens between words where necessary (e.g., "Twenty-One") and with an "and" between the hundreds and tens/ones places where necessary (e.g., "One Hundred and Twenty-One").
"""

def IntegerToWritten(num):
    single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def helper(n):
        if n < 10:
            return single_digits[n]
        elif n < 20:
            return teens[n-10]
        elif n < 100:
            if n % 10 == 0:
                return tens[n//10]
            else:
                return tens[n//10] + "-" + single_digits[n%10]
        elif n < 1000:
            if n % 100 == 0:
                return single_digits[n//100] + " hundred"
            else:
                return single_digits[n//100] + " hundred and " + helper(n%100)

    i = 0
    result = ""
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + " " + thousands[i] + " " + result
        num //= 1000
        i += 1
    return result.strip()