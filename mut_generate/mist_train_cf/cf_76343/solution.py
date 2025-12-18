"""
QUESTION:
Create a function named `extract_and_count_emails` that takes a string `text` and a list of valid top-level domains `valid_tlds` as input, and returns a tuple containing the total number of valid email addresses found and a dictionary with TLDs as keys and their occurrence counts as values. The function should use a regex pattern to extract email addresses from the text and validate the TLDs against the provided list. The list of valid TLDs should be in the format of a list containing strings, e.g., `['.com', '.org', '.net']`.
"""

import re
from typing import List, Dict, Tuple
from collections import Counter

def extract_and_count_emails(text: str, valid_tlds: List[str]) -> Tuple[int, Dict[str, int]]:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    matches = re.findall(pattern, text)
    valid_emails = [email for email in matches if any(email.endswith(tld) for tld in valid_tlds)]
    tld_counts = Counter(email[email.rindex('.'):].lower() for email in valid_emails)
    return len(valid_emails), dict(tld_counts)