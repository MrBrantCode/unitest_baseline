"""
QUESTION:
Implement a function `significant_genes` that takes a list of genes and a minimum size as input and returns a list of genes that have a significant effect. A gene has a significant effect if its occurrence count is greater than or equal to the specified minimum size. The function should return a list of unique genes that meet this condition.

The function signature is:
```python
def significant_genes(genes: List[str], effect_min_size: int) -> List[str]
```

The function should only consider the unique genes in the input list when calculating the occurrence count.
"""

from typing import List

def significant_genes(genes: List[str], effect_min_size: int) -> List[str]:
    gene_counts = {}
    for gene in genes:
        gene_counts[gene] = gene_counts.get(gene, 0) + 1
    
    significant_genes = [gene for gene, count in gene_counts.items() if count >= effect_min_size]
    return significant_genes