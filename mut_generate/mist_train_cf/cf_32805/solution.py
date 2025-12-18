"""
QUESTION:
Implement a function `find_best_motifs` that finds the best motifs in a set of DNA sequences. The function should take in three parameters: a list of DNA sequences `dna`, an integer `k` representing the length of the motifs to be found, and an integer `t` representing the number of DNA sequences in the input. The function should use a scoring system to evaluate the quality of motifs and return the best motifs based on this scoring, where the lower the score, the better the motifs.
"""

def find_best_motifs(dna, k, t):
    best_motifs = [sequence[:k] for sequence in dna]
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            transposed = [list(row) for row in zip(*motifs)]
            n = len(motifs)
            profile = {nucleotide: [i.count(nucleotide) / n for i in transposed] for nucleotide in 'ACGT'}
            probabilities = [max([profile[nucleotide][idx] for idx, nucleotide in enumerate(dna[j][x:x + k])]) for x in range(len(dna[j]) - k + 1)]
            max_prob_index = probabilities.index(max(probabilities))
            motifs.append(dna[j][max_prob_index:max_prob_index + k])
        score = sum([sum([1 for nucleotide in column if nucleotide != max(set(column), key=column.count)]) for column in zip(*motifs)])
        if score < sum([sum([1 for nucleotide in column if nucleotide != max(set(column), key=column.count)]) for column in zip(*best_motifs)]):
            best_motifs = motifs
    return best_motifs