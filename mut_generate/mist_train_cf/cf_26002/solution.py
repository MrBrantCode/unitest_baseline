"""
QUESTION:
Design a navigation menu for a GUI-based web application that allows users to order food online. The menu should include options for searching and selecting food items, viewing cart contents, and checkout. Additionally, include user authentication options (sign up, sign in) and a feature for viewing order history, which should only be visible when a user is signed in. The checkout process should allow users to enter payment details and confirm their order.
"""

def navigation_menu(is_signed_in, cart_contents, order_history):
    """
    Navigation menu for a GUI-based web application that allows users to order food online.

    Args:
    is_signed_in (bool): Whether the user is signed in or not.
    cart_contents (list): List of food items in the user's cart.
    order_history (list): List of the user's past orders.

    Returns:
    A string representing the navigation menu.
    """

    menu = ""

    # Search and select food items
    menu += "Search for food items\n"
    menu += "Select food items to add to cart\n"

    # View cart contents
    menu += "View cart contents\n"

    # Checkout
    menu += "Checkout\n"
    menu += "  Enter payment details\n"
    menu += "  Confirm order\n"

    # User authentication
    menu += "Sign up\n"
    menu += "Sign in\n"

    # View order history (only visible when signed in)
    if is_signed_in:
        menu += "View order history\n"

    return menu