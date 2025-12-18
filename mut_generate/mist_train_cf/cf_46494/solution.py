"""
QUESTION:
Write a function to measure the render time of each control on a webpage. The function should work for both standard ASP.NET controls and third-party controls, and should be able to handle a large number of controls on the page.
"""

def measure_render_time(control):
    """
    Measure the render time of a given control.

    Args:
    control (object): The control to measure the render time for.

    Returns:
    float: The render time of the control in seconds.
    """
    import time
    start_time = time.time()
    control.render()
    end_time = time.time()
    render_time = end_time - start_time
    return render_time