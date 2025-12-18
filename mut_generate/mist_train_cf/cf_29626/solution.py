"""
QUESTION:
Implement the `applyRule` function to update the term summary based on the `commonSupertermInListRepresentsSubtermsWithLessRepresentativePower` rule. The function should take a term summary, a dictionary of gene sets, a threshold value, and a rule function as input. It should return an updated term summary where each term's representative power is updated based on its subterms and filtered by the threshold. The representative power of a term is the size of the smallest gene set among the term and its subterms. A subterm is considered if its gene set is a subset of the current term's gene set and has a smaller or equal size than the current representative power.
"""

def applyRule(term_summary, gene_sets_dict, threshold, rule_function):
    """
    Updates the term summary based on the commonSupertermInListRepresentsSubtermsWithLessRepresentativePower rule.

    Args:
    - term_summary (list): A list of term information, where each term is represented as [term, subterms, representative_power].
    - gene_sets_dict (dict): A dictionary of gene sets, where each key is a term and its value is a set of genes.
    - threshold (int): The maximum representative power for a term to be included in the updated term summary.
    - rule_function (function): The rule function to apply (not used in this implementation).

    Returns:
    - updated_term_summary (list): The updated term summary with representative powers and subterms updated based on the rule.
    """
    updated_term_summary = []
    for term_info in term_summary:
        term = term_info[0]
        subterms = term_info[1]
        representative_power = term_info[2]
        for subterm, gene_set in gene_sets_dict.items():
            if subterm != term and gene_set.issubset(gene_sets_dict[term]):
                if len(gene_set) < representative_power:
                    representative_power = len(gene_set)
                    subterms = [subterm]
                elif len(gene_set) == representative_power:
                    subterms.append(subterm)
        if representative_power <= threshold:
            updated_term_summary.append([term, subterms, representative_power])
    return updated_term_summary