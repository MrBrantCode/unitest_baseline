"""
QUESTION:
Create a class called MyClass with a class attribute "var" having a default value "value". The class should have a method called is_palindrome to check if "var" is a palindrome. The class should be inheritable, allowing subclasses to override the "var" attribute. Create a subclass of MyClass called MyChildClass that overrides the "var" attribute and provides a different implementation for the is_palindrome method. The is_palindrome method in MyChildClass should be case-insensitive.
"""

def entrance(var):
    class MyClass:
        def __init__(self, var=var):
            self.var = var

        def is_palindrome(self):
            return self.var == self.var[::-1]

    class MyChildClass(MyClass):
        def __init__(self, var=var):
            super().__init__(var)

        def is_palindrome(self):
            return self.var.lower() == self.var[::-1].lower()

    return MyChildClass(var)

# The function entrance returns the class instance of MyChildClass.
# You can use it like this:
# my_instance = entrance("racecar")
# print(my_instance.is_palindrome())