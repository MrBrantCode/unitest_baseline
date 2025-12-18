"""
QUESTION:
Implement a function `PitchTimeAmdf` to calculate the Average Magnitude Difference Function (AMDF) for a given input signal. The function should take the input signal `x`, block length `iBlockLength`, hop length `iHopLength`, and sampling frequency `f_s` as parameters. The function should return a list of AMDF values calculated using the formula: 
\[ AMDF[m] = \frac{1}{N} \sum_{n=0}^{N-1} |x[n] - x[n+m]| \]

The input parameters are:
- `x` (list of floats): The input signal with a length greater than `iBlockLength`
- `iBlockLength` (int): The block length for AMDF calculation, a positive integer
- `iHopLength` (int): The hop length for AMDF calculation, a positive integer
- `f_s` (float): The sampling frequency of the input signal, a positive float

The output is:
- `AMDF` (list of floats): The calculated AMDF values
"""

def PitchTimeAmdf(x, iBlockLength, iHopLength, f_s):
    AMDF = []
    N = iBlockLength
    for m in range(N):
        amdf_sum = 0
        for n in range(N):
            if n+m < len(x):
                amdf_sum += abs(x[n] - x[n+m])
        AMDF.append(amdf_sum / N)
    return AMDF