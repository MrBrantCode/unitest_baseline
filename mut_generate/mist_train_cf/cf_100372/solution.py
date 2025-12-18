"""
QUESTION:
Create a function named `concatenate_sequences` that takes a list of protein sequences as input. The function should concatenate the sequences, calculate the amino acid composition for each sequence, and return a table displaying the counts of each amino acid for each sequence. The table should have a header row with column names "Amino acid" and "Sequence X" where X is the sequence number. Each subsequent row should contain the counts for a single amino acid across all sequences.
"""

def concatenate_sequences(sequences):
    # Concatenate the sequences
    concatenated_sequence = "".join(sequences)
    
    # Count the amino acid composition for each sequence
    amino_acid_counts = []
    for sequence in sequences:
        count = {}
        for amino_acid in sequence:
            if amino_acid in count:
                count[amino_acid] += 1
            else:
                count[amino_acid] = 1
        amino_acid_counts.append(count)
    
    # Create a table of counts for each sequence
    table = []
    header = ["Amino acid"]
    for i in range(len(sequences)):
        header.append("Sequence " + str(i+1))
    table.append(header)
    amino_acids = list(set(concatenated_sequence))
    amino_acids.sort()
    for amino_acid in amino_acids:
        row = [amino_acid]
        for i in range(len(sequences)):
            count = amino_acid_counts[i].get(amino_acid, 0)
            row.append(count)
        table.append(row)
    
    # Return the table
    return table