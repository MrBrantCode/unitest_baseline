"""
QUESTION:
Implement a function called `determine_view_model` that determines the best approach for passing data to a view in ASP.NET MVC, considering the trade-offs between strongly typed views and using ViewData/ViewBag. The function should take into account the criticality of the data to the functionality of the view, the complexity of the data, and the need for compile-time error checking.
"""

def determine_view_model(criticality, complexity, compile_time_checking):
    """
    Determine the best approach for passing data to a view in ASP.NET MVC.

    Args:
    criticality (str): The criticality of the data to the functionality of the view. Can be 'high' or 'low'.
    complexity (str): The complexity of the data. Can be 'high' or 'low'.
    compile_time_checking (bool): Whether compile-time error checking is needed.

    Returns:
    str: The recommended approach. Either 'Strongly Typed Views' or 'ViewData/ViewBag'.
    """

    if criticality == 'high' or complexity == 'high' or compile_time_checking:
        # For critical data, complex data, or when compile-time error checking is needed, 
        # strongly typed views are recommended.
        return 'Strongly Typed Views'
    else:
        # For non-critical data, simple data, and when compile-time error checking is not needed, 
        # ViewData/ViewBag can be used.
        return 'ViewData/ViewBag'