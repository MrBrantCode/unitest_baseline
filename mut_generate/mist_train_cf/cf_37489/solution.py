"""
QUESTION:
Write a function `categorize_files` that takes a list of VCF file names as input and returns a dictionary containing the counts of file types ("SNV" or "indel") by genomic region ("autosome", "chrX_PAR2", "chrX_PAR3", "chrMT"). The file names are in the format "${pre}-type-region.vcf.gz[.tbi]", where "type" is either "snvall" or "indelall" and "region" is one of the specified genomic regions. The function should categorize the file names based on their type and region, and output the counts in a nested dictionary structure.
"""

def categorize_files(file_names):
    counts = {"SNV": {"autosome": 0, "chrX_PAR2": 0, "chrX_PAR3": 0, "chrMT": 0}, 
              "indel": {"autosome": 0, "chrX_PAR2": 0, "chrX_PAR3": 0, "chrMT": 0}}

    for file_name in file_names:
        parts = file_name.split("-")
        file_type = "SNV" if "snv" in parts[1] else "indel"
        region = parts[-1].split(".")[0]

        if region in counts[file_type]:
            counts[file_type][region] += 1

    return counts