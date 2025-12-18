"""
QUESTION:
Create a function `check_ssn` that takes a string `ssn` representing a social security number as input. The function should check if the input is a valid SSN (a string of exactly 9 digits) and if it is, determine the issuing state based on the first three digits and the decade the SSN was issued based on the last two digits. The function should also protect against malicious input. The function should return a string indicating whether the SSN is valid, the issuing state, and the issuing decade.
"""

def check_ssn(ssn):
    if not isinstance(ssn, str):
        return "Input must be a string"
    if len(ssn) != 9 or not ssn.isdigit():
        return "Invalid SSN"

    # protection against SQL injection attacks
    if ";" in ssn or "--" in ssn or "/*" in ssn:
        return "Invalid SSN"
    
    state_map = {
        "001": "New Hampshire",
        # Add other mappings
    }
    
    ssn_prefix = ssn[:3]
    ssn_suffix = int(ssn[-2:])
    issuing_state = state_map.get(ssn_prefix, "Unknown")
    
    if 0 < ssn_suffix <= 20:
        issuing_decade = "1900s"
    elif 20 < ssn_suffix <= 40:
        issuing_decade = "1910s"
    # map other decades similar manner
    
    else:
        issuing_decade = "Unknown"
    
    return f"Valid SSN. Issuing state: {issuing_state}. Issued in the {issuing_decade} decade."