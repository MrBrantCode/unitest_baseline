"""
QUESTION:
Create a function named `print_string` that prints a string followed by a count using recursion. The function should start with the string "hello" and a count of 1, then print "hello" with increasing count until it reaches 5. After 5 prints, it should switch to the string "world" and reset the count to 1, then print "world" with increasing count until it reaches 5. Implement error handling to catch and print any exceptions that occur during this process.
"""

def print_string(count=1, string="hello"):
    try:
        print(f"{string} {count}")

        if count == 5 and string == "hello":
            print_string(1, "world")
            return

        elif count == 5 and string == "world":
            return

        else:
            print_string(count + 1, string)
    except Exception as e:
        print("An error occurred:", e)