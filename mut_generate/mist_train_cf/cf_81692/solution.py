"""
QUESTION:
Calculate the PCA Decomposition of a Bond's Return

Write a function `pca_decomposition` that takes in a bond's return and the coefficients of the first three principal components (PCs) as inputs. The function should output a dictionary showing the contribution of each PC to the bond's return.

Restrictions: 
- Assume that the first three PCs account for 98% of the variance in returns.
- The coefficients of the first three PCs are obtained from a regression analysis using the changes in yield as the dependent variable and the changes of the first three principal components as independent variables.
"""

def pca_decomposition(bond_return, pc_coefficients):
    """
    Calculate the contribution of each principal component to a bond's return.

    Args:
    - bond_return (float): The return of the bond.
    - pc_coefficients (list of floats): A list containing the coefficients of the first three principal components.

    Returns:
    - dict: A dictionary showing the contribution of each principal component to the bond's return.
    """
    contributions = {}
    for i, coefficient in enumerate(pc_coefficients):
        pc_contribution = bond_return * coefficient
        contributions[f'PC{i+1}'] = pc_contribution
    return contributions