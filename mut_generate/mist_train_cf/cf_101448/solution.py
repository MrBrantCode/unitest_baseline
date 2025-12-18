"""
QUESTION:
Create a function `generate_tassel` that simulates the process of creating beaded tassels. The function should take three parameters: `num_strands`, `lengths`, and `colors`. `num_strands` is the number of strands in the tassel, `lengths` is a list of integers representing the length of each strand, and `colors` is a list of strings representing the color of each strand. The function should return a digital representation of the tassel, including a close-up view of the individual beads and a wider view of the tassel as a whole. 

Assume that each bead has a unique color and pattern, and that the strands are interwoven to create a complex and unique pattern. The function should not handle saving or sharing the tassel design.
"""

def generate_tassel(num_strands, lengths, colors):
    class Bead:
        def __init__(self, color, pattern):
            self.color = color
            self.pattern = pattern

    class Strand:
        def __init__(self, length, color):
            self.length = length
            self.color = color
            self.beads = []

        def add_bead(self, bead):
            self.beads.append(bead)

    class Tassel:
        def __init__(self, num_strands):
            self.num_strands = num_strands
            self.strands = []

        def add_strand(self, strand):
            self.strands.append(strand)

        def generate_tassel(self):
            # Logic to braid the strands and attach them to a cap
            pass

        def display_tassel(self):
            # Logic to display the tassel
            pass

    tassel = Tassel(num_strands)
    for length, color in zip(lengths, colors):
        strand = Strand(length, color)
        for i in range(length):
            bead = Bead(color, 'pattern')
            strand.add_bead(bead)
        tassel.add_strand(strand)
    return tassel