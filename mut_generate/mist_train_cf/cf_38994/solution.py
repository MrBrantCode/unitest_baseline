"""
QUESTION:
Implement a function `update_pin(users: dict)` that updates a user's PIN in a given user database. The function should prompt the user to enter their previous PIN and a new PIN. If the previous PIN is different from the new PIN, it should check if the previous PIN exists in the database. If it does, the function should update the user's PIN and display the updated database along with a success message. If the previous PIN does not exist in the database, it should display an "Invalid PIN" message. If the previous PIN is the same as the new PIN, it should display a "Card is necessary" message. The function should return the updated user database.
"""

def update_pin(users: dict):
    previous_pin_inp = int(input('Please Enter previous PIN: '))
    new_pin_inp = int(input('Please Enter new PIN: '))

    if previous_pin_inp != new_pin_inp:
        if previous_pin_inp in users:
            users[int(new_pin_inp)] = users.pop(int(previous_pin_inp))
            print(users)
            print('Dear user, your PIN has been updated successfully..!')
        else:
            print('Invalid PIN')
    else:
        print('Card is necessary')

    return users