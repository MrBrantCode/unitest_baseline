"""
QUESTION:
Create a function called `classify_number` that takes a North American phone number as input, identifies the phone number type (mobile, landline, toll-free) based on the North American Numbering Plan (NANP), and returns the corresponding type. Assume every phone number starts with an area code. 

The function should use the latest NANP guidelines for area codes. 

Example of a phone number input: (123) 456-7890.
"""

import re

# North American Numbering Plan (NANP) area codes
MOBILE_CODES = ['201', '202', '203', '205', '207', '208', '209', '210', '212', '213', '214', '215', '216', '217', '218',
                '219', '224', '225', '227', '228', '229', '231', '234', '239', '240', '242', '246', '248', '251', '252',
                '253', '254', '256', '260', '262', '264', '267', '268', '269', '270', '272', '274', '276', '278', '281',
                '283', '284', '289', '301', '302', '303', '304', '305', '307', '308', '309', '310', '312', '313', '314',
                '315', '316', '317', '318', '319', '320', ]
LANDLINE_CODES = ['321', '323', '325', '327', '330', '331', '334', '336', '337', '339', '340', '341', '343', '345', 
                  '347', '351', '352', '360', '361', '364', '365', '369', '380', '385']
TOLL_FREE_CODES = ['800', '833', '844', '855', '866', '877', '888']

def classify_number(number):
    area_code = number[1:4]
    if area_code in MOBILE_CODES:
        return 'mobile'
    elif area_code in LANDLINE_CODES:
        return 'landline'
    elif area_code in TOLL_FREE_CODES:
        return 'toll-free'
    else:
        return 'unknown'