"""
QUESTION:
Create a regular expression pattern to identify date strings in the format MM/DD/YYYY, where the month (MM) is between 01 and 12, the day (DD) is between 01 and 31, and the year (YYYY) is between 1000 and 2999. The pattern should ensure that the date is a standalone string, not part of a larger string or number. Note that the pattern does not need to validate the date's validity (e.g., 02/30/2000), only its format.
"""

import re

def date_pattern(date):
    return re.compile(r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([1-2]\d{3})\b')

# date_pattern = re.compile(r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([1-2]\d{3})\b') 

# Let us break down what the pattern `r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/([1-2]\d{3})\b'` does.

# 1. `\b` - stands for word boundary. This ensures that the date matched is not part of a larger string or number.
# 2. `(0[1-9]|1[0-2])` - this matches the month part of the date. The month must start with '0' and close with any digit between 1 and 9, or start with '1' and close with either '0', '1' or '2'.
# 3. `/` - this matches exactly the slash symbol, which is a common date separator.
# 4. `(0[1-9]|[12][0-9]|3[01])` - this matches the day part of the date. The day must start with '0' and close with any digit from 1 to 9, or start with '1' or '2' followed by any digit, or be '30' or '31'.
# 5. `/` - this matches exactly the slash symbol, which is a common date separator.
# 6. `([1-2]\d{3})` - this matches the year part of the date. The year must start with either '1' or '2' and then be followed by three digits. This is to cover years from 1000 to 2999.
# 7. `\b` - this matches a word boundary, ensuring the date is not part of a larger number or string.

# Please note that this regular expression will accept dates like "02/30/2000" which aren't actually valid. If you need to account for different days in different months/leap years, you'll have to use some actual coding logic, as regular expressions are not capable of that.