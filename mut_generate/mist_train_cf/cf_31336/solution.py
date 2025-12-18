"""
QUESTION:
Implement a function `generate_menu(user_role)` that generates HTML code for a navigation menu based on the user's role. The function should take a user role as input and return the corresponding HTML code for the navigation menu. The HTML code should include anchor tags with `href` attributes generated using the `route` function provided by the web framework. The function should support user roles "admin" and "user", and return an error message for any other user role.
"""

def generate_menu(user_role):
    if user_role == "admin":
        return """
        <ul>
            <li class="liadmin"><a class="aadmin" href="{{route('dashboard')}}">Dashboard</a></li>
            <li class="liadmin"><a class="aadmin" href="{{route('manage.users')}}">Manage Users</a></li>
            <li class="liadmin"><a class="aadmin" href="{{route('logout')}}">Log out</a></li>
        </ul>
        """
    elif user_role == "user":
        return """
        <ul>
            <li class="liuser"><a class="auser" href="{{route('cancel.user')}}">Cancel Order</a></li>
            <li class="liuser"><a class="auser" href="{{route('logout')}}">Log out</a></li>
        </ul>
        """
    else:
        return "<p>Invalid user role</p>"