"""
QUESTION:
Write a function `generate_input_file(numLambda, numStepsEquilib)` that takes two integers `numLambda` and `numStepsEquilib` as input and returns a string representing the contents of the input file for a batch job. The contents should include the number of lambda values, the number of equilibration steps, and a list of logarithmically spaced lambda values from 10^-6 to 10^6. The format of the output string should be:
```
# testInput.n
# Input file for batch job n
numLambda = <numLambda>
numStepsEquilib = <numStepsEquilib>
lambdaValues = [<lambda1>, <lambda2>, ..., <lambdaN>]
```
"""

import math

def generate_input_file(numLambda, numStepsEquilib):
    lambda_values = [10 ** (i / (numLambda - 1) * 12 - 6) for i in range(numLambda)]
    input_content = f"# testInput.{numLambda}\n"
    input_content += f"# Input file for batch job {numLambda}\n"
    input_content += f"numLambda = {numLambda}\n"
    input_content += f"numStepsEquilib = {numStepsEquilib}\n"
    input_content += f"lambdaValues = {lambda_values}\n"
    return input_content