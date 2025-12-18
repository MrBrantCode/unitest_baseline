"""
QUESTION:
Given a list of registered domain names for each top-level domain, implement the function `find_top_level_domains()` to find all top-level domains for the TLD ".org" that have at least one domain name registered with more than 100 subdomains and the sum of the subdomain lengths is a prime number. Assume a top-level domain can be any combination of letters from a-z or digits from 0-9, considering two-character top-level domains.
"""

import math

def find_top_level_domains(subdomains):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    if len(subdomains) > 100:
        sum_lengths = sum(len(subdomain) for subdomain in subdomains)
        if is_prime(sum_lengths):
            result.append("org")
    return result