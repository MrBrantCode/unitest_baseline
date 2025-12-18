"""
QUESTION:
Implement the `calculate_total_cost` method within the `BookOrder` class to calculate the total cost of the book order based on its specifications. The method should consider the following attributes: `cover_lamination`, `flat_cover_print_cols`, `printed_flyleafs`, `paper_type_bn`, `paper_type_col`, `paper_grams_bn`, `paper_grams_col`, `jacket_paper_type`, `jacket_lamination`, and `legatures`. Replace the placeholder cost calculation logic with actual cost calculation based on the specifications. 

Assume the cost of each attribute as follows: 
- `flat_cover_print_cols`: $10 per printed column
- `printed_flyleafs`: $5 per printed flyleaf
- Add more cost calculations based on other attributes.
"""

def calculate_total_cost(cover_lamination, flat_cover_print_cols, printed_flyleafs, paper_type_bn, paper_type_col, paper_grams_bn, paper_grams_col, jacket_paper_type, jacket_lamination, legatures):
    """
    Calculates the total cost of the book order based on its specifications.

    Args:
        cover_lamination (str): Type of cover lamination.
        flat_cover_print_cols (int): Number of flat cover print columns.
        printed_flyleafs (int): Number of printed flyleafs.
        paper_type_bn (str): Type of paper for black and white pages.
        paper_type_col (str): Type of paper for color pages.
        paper_grams_bn (int): Grams per square meter of black and white paper.
        paper_grams_col (int): Grams per square meter of color paper.
        jacket_paper_type (str): Type of paper for the jacket.
        jacket_lamination (str): Type of lamination for the jacket.
        legatures (int): Number of legatures.

    Returns:
        float: The total cost of the book order.

    """
    # Cost per unit of each attribute
    cover_lamination_cost = 5
    flat_cover_print_cols_cost = 10
    printed_flyleafs_cost = 5
    paper_type_bn_cost = 1.5
    paper_type_col_cost = 2.5
    paper_grams_bn_cost = 0.1
    paper_grams_col_cost = 0.15
    jacket_paper_type_cost = 3
    jacket_lamination_cost = 4
    legatures_cost = 2

    # Calculate the total cost
    total_cost = (
        (cover_lamination == "matte") * cover_lamination_cost + 
        (cover_lamination == "glossy") * cover_lamination_cost * 2 + 
        flat_cover_print_cols * flat_cover_print_cols_cost + 
        printed_flyleafs * printed_flyleafs_cost + 
        (paper_type_bn == "standard") * paper_type_bn_cost + 
        (paper_type_bn == "premium") * paper_type_bn_cost * 2 + 
        (paper_type_col == "standard") * paper_type_col_cost + 
        (paper_type_col == "premium") * paper_type_col_cost * 2 + 
        paper_grams_bn * paper_grams_bn_cost + 
        paper_grams_col * paper_grams_col_cost + 
        (jacket_paper_type == "standard") * jacket_paper_type_cost + 
        (jacket_paper_type == "premium") * jacket_paper_type_cost * 2 + 
        (jacket_lamination == "matte") * jacket_lamination_cost + 
        (jacket_lamination == "glossy") * jacket_lamination_cost * 2 + 
        legatures * legatures_cost
    )

    return total_cost