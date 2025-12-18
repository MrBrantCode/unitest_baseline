"""
QUESTION:
Create a function called `compare_methods` that takes four parameters: the original DataFrame `df`, and the DataFrames resulting from linear, polynomial, and spline interpolation of `df`. The function should compare the performance of these interpolation methods by calculating the sum of absolute differences between the original DataFrame `df` and each of the interpolated DataFrames, and return a dictionary with keys "Linear", "Poly", and "Spline" representing the performance of each method. Assume that the DataFrames have the same structure and that the interpolation methods do not result in any NaN values.
"""

def compare_methods(df, df_linear, df_poly, df_spline):
    """
    Compare the performance of linear, polynomial, and spline interpolation methods.

    Args:
    df (DataFrame): The original DataFrame.
    df_linear (DataFrame): The DataFrame resulting from linear interpolation of df.
    df_poly (DataFrame): The DataFrame resulting from polynomial interpolation of df.
    df_spline (DataFrame): The DataFrame resulting from spline interpolation of df.

    Returns:
    dict: A dictionary with keys "Linear", "Poly", and "Spline" representing the performance of each method.
    """
    diff_linear = np.abs(df - df_linear).sum().sum()
    diff_poly = np.abs(df - df_poly).sum().sum()
    diff_spline = np.abs(df - df_spline).sum().sum()
    return {"Linear": diff_linear, "Poly": diff_poly, "Spline": diff_spline}