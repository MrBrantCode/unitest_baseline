"""
QUESTION:
Create a function `calculate_expected_offspring` that calculates the expected number of offspring displaying the dominant phenotype in a population. The function takes seven parameters: `offsprings`, `AA_AA`, `AA_Aa`, `AA_aa`, `Aa_Aa`, `Aa_aa`, and `aa_aa`, which represent the number of offspring pairs produced in the population and the number of offspring pairs with specific genotypes, respectively. The function should return the expected number of offspring displaying the dominant phenotype. 

The probability of producing offspring with the dominant phenotype for each genotype pair is: 
- 1 for AA-AA, AA-Aa, AA-aa
- 0.75 for Aa-Aa
- 0.5 for Aa-aa
- 0 for aa-aa
"""

def calculate_expected_offspring(offsprings, AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa):
    allel_prob = [1, 1, 1, 0.75, 0.5, 0]
    expected_offspring = sum([offsprings * prob for offsprings, prob in zip([AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa], allel_prob)])
    return expected_offspring