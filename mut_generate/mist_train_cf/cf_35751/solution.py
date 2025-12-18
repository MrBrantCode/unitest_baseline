"""
QUESTION:
Calculate the VCO frequency based on the provided RF configuration settings and VCO specifications. The function should be named `calculate_vco_frequency` and take the following parameters: `rfConfig`, which is an object containing the RF configuration settings, and `input_frequency`, which is the reference frequency provided to the VCO. The function should return the calculated VCO frequency. The VCO frequency is calculated using the formula: VCO Frequency = (input_frequency / rfConfig.R1.rfDivideBy2) * (2^rfConfig.R1.vcoBias) * (2^rfConfig.R1.vcoInductor). The VCO operates in the frequency range of 80 - 200 MHz.
"""

def calculate_vco_frequency(rfConfig, input_frequency):
    """
    Calculate the VCO frequency based on the provided RF configuration settings and VCO specifications.

    Args:
        rfConfig (object): An object containing the RF configuration settings.
        input_frequency (float): The reference frequency provided to the VCO.

    Returns:
        float: The calculated VCO frequency.
    """

    # Extract the required configuration settings from the rfConfig object
    rfDivideBy = rfConfig.R1.rfDivideBy2
    vcoBias = rfConfig.R1.vcoBias
    vcoInductor = rfConfig.R1.vcoInductor

    # Calculate the VCO frequency using the formula
    vco_frequency = (input_frequency / rfDivideBy) * (2 ** vcoBias) * (2 ** vcoInductor)

    return vco_frequency