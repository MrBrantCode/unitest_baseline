"""
QUESTION:
Create a function called `complex2words` that takes a complex number as input and returns a string describing the complex number in words, along with its phase angle in both radians and degrees. The function should handle the following cases: 
- both the real and imaginary parts are non-zero
- the real part is zero
- the imaginary part is zero
- both the real and imaginary parts are zero.
"""

import cmath

def complex2words(z):
    real = int(z.real)
    imag = int(z.imag)
    
    # Handle corner cases
    if real == 0 and imag == 0:
        word = 'Zero'
    elif real == 0:
        word = str(imag) + ' i'
    elif imag == 0:
        word = str(real)
    else:
        word = str(real) + ' plus ' + str(imag) + ' i'
        
    phase_radians = cmath.phase(z)
    phase_degrees = phase_radians * (180.0 / cmath.pi)
    return "{}; phase angle is {:.2f} radians or {:.2f} degrees.".format(word, phase_radians, phase_degrees)