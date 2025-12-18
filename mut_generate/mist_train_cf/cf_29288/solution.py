"""
QUESTION:
Implement a class method `indirect_decode` that takes two arguments: `solution` and `sf` (scaling factor). The method should return the decoded `solution` by applying the `sf` to each value in `solution`. The decoding process depends on the number of inputs and hidden layers, which can be obtained from `self.config` dictionary with keys 'input' and 'hiddens'.
"""

def indirect_decode(self, solution, sf):
    num_input = self.config['input']
    shapes = [[num_input, h, 1] for h in self.config['hiddens']]
    decoded_solution = [val * sf for val in solution]  # Apply scaling factor to each value in the solution
    return decoded_solution