"""
QUESTION:
Create a function called `apply_voucher` that accepts a voucher code and calculates the total cost of items in a shopping list after applying the voucher discount. The function should handle voucher codes that offer a fixed discount amount (prefix 'F') or a percentage off the total cost (prefix 'P'). The function should ensure that the total cost does not go below zero after applying the voucher discount. The voucher codes are in the format 'F' or 'P' followed by a number. If an invalid voucher code is provided, the function should handle the error and print an error message.
"""

def apply_voucher(shopping_list, voucher_code):
    total = sum(item['quantity'] * item['cost'] for item in shopping_list.values())
    
    if voucher_code[0] == 'F':
        try:
            discount = int(voucher_code[1:])
            total -= discount
            if total < 0: 
                total = 0
        except ValueError:
            print("Invalid voucher code.")
    elif voucher_code[0] == 'P':
        try:
            discount = int(voucher_code[1:])
            total *= (1 - discount/100)
        except ValueError:
            print("Invalid voucher code.")
    else:
        print("Invalid voucher code.")
    return total