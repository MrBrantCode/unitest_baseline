"""
QUESTION:
Create a function named `count_clr_versions` that takes a string of semicolon-separated .NET CLR versions as input. The function should return a count of each unique CLR version along with its frequency. The input string will contain CLR versions in the format "CLR x.x.xxxxxx". The function should parse the input string, count the occurrences of each unique CLR version, and output the version along with its frequency. The function should be case-sensitive and consider ".NET CLR 3.5.30729" and ".net clr 3.5.30729" as different versions.
"""

def count_clr_versions(clr_versions_str):
    clr_versions = clr_versions_str.split('; ')
    clr_count = {}

    for version in clr_versions:
        if version in clr_count:
            clr_count[version] += 1
        else:
            clr_count[version] = 1

    return clr_count