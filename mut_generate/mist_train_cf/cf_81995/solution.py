"""
QUESTION:
Write a test case to verify if the `setTitle` function is successfully called when invoking `functionUnderTest` using the MockK library. 

The `functionUnderTest` function creates an `AlertDialog.Builder` instance and calls `setTitle` on it. The `AlertDialog.Builder` class is final and cannot be mocked directly. 

The function `functionUnderTest` should be refactored to accept an instance of `AlertDialog.Builder` as a parameter to facilitate mocking.
"""

def setTitle(builder):
    builder.setTitle("MyTitle")
    builder.create()
    return builder