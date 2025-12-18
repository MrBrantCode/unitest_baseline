"""
QUESTION:
Write a function `calculateRT` that takes seven parameters: `R` (reflectance component for reflection), `T` (transmittance component for transmission), `isSpecular` (a boolean indicating whether the material has a specular component), `distrib` (microfacet distribution component for transmission), `fresnel` (Fresnel component for reflection), `eta` (index of refraction component for transmission), and `mode` (mode component for transmission). The function should return a tuple `(reflectance, transmittance)` representing the total reflectance and transmittance of a material. All input parameters are valid and within the specified ranges.
"""

def calculateRT(R, T, isSpecular, distrib, fresnel, eta, mode):
    reflectance = R * fresnel if R > 0 else 0
    transmittance = T if isSpecular and T > 0 else T * (1 - distrib) if T > 0 else 0
    return reflectance, transmittance