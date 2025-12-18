"""
QUESTION:
Create a function called `analyze_simulation_results` that takes two parameters: `photon_intensity_results` and `k_ratio_results`. The function should calculate the average photon intensity from the `photon_intensity_results` and the average K-ratios for each element from the `k_ratio_results`. The function should return the average photon intensity and a dictionary where the keys are elements and the values are their corresponding average K-ratios. Assume that `photon_intensity_results` and `k_ratio_results` are lists of objects with `intensity` and `element` and `value` attributes respectively. The function should handle cases where the input lists are empty.
"""

def analyze_simulation_results(photon_intensity_results, k_ratio_results):
    """
    Calculate the average photon intensity and K-ratios for each element from simulation results.

    Parameters:
    photon_intensity_results (list): A list of PhotonIntensityResult objects.
    k_ratio_results (list): A list of KRatioResult objects.

    Returns:
    tuple: A tuple containing the average photon intensity and a dictionary of average K-ratios.
    """

    # Calculate the average photon intensity
    total_intensity = sum(result.intensity for result in photon_intensity_results if hasattr(result, 'intensity'))
    num_samples = sum(1 for result in photon_intensity_results if hasattr(result, 'intensity'))
    average_intensity = total_intensity / num_samples if num_samples > 0 else 0

    # Calculate the K-ratios
    k_ratios = {}
    for result in k_ratio_results:
        if hasattr(result, 'element') and hasattr(result, 'value'):
            element = result.element
            k_ratio = result.value
            if element in k_ratios:
                k_ratios[element].append(k_ratio)
            else:
                k_ratios[element] = [k_ratio]

    # Calculate the average K-ratios
    average_k_ratios = {element: sum(ratios) / len(ratios) for element, ratios in k_ratios.items()}

    return average_intensity, average_k_ratios