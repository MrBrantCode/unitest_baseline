"""
QUESTION:
Write a function `parse_samtools_stats(stats_report)` that takes a string `stats_report` as input, representing the output of the `samtools stats` command. The function should extract the following statistics:

1. Total number of reads
2. Average length of reads
3. Percentage of properly paired reads
4. Percentage of reads mapped to the forward strand

The input `stats_report` will be formatted as follows:
- Each statistic is represented by a line starting with a keyword followed by a colon and a space, then the corresponding value.
- The statistics of interest are labeled as "raw total sequences", "average length", "properly paired in sequencing", and "reads mapped and paired".

The function should return a dictionary with the statistic names as keys and their corresponding values as the dictionary values. The dictionary keys should be "Total number of reads", "Average length of reads", "Percentage of properly paired reads", and "Percentage of reads mapped to the forward strand".
"""

import re

def parse_samtools_stats(stats_report):
    stats_dict = {}
    pattern = r"SN\s+(.+):\s+(\d+|\d+\.\d+)%?"
    matches = re.findall(pattern, stats_report)
    
    for match in matches:
        key = match[0].strip().replace(" ", "_")
        value = float(match[1]) if '.' in match[1] else int(match[1])
        stats_dict[key] = value
    
    return {
        "Total number of reads": stats_dict.get("raw_total_sequences", 0),
        "Average length of reads": stats_dict.get("average_length", 0),
        "Percentage of properly paired reads": stats_dict.get("properly_paired_in_sequencing", 0),
        "Percentage of reads mapped to the forward strand": stats_dict.get("reads_mapped_and_paired", 0)
    }