"""
QUESTION:
To get on the Shinkansen, you need two tickets, a "ticket" and a "limited express ticket". These are separate tickets because some of the routes may not use the Shinkansen, but for routes that use only the Shinkansen, one ticket can be used as both a ticket and a limited express ticket. It may also be issued.

Automatic ticket gates must read these tickets and open the gate only when the correct ticket is inserted. Create a program that determines whether one "ticket" and one "limited express ticket" or both, or one "boarding / limited express ticket" has been inserted, and determines whether the door of the automatic ticket gate is open or closed. please do it.



input

The input is given in the following format.


b1 b2 b3


The input consists of one line and contains three integers separated by one space. b1 indicates the state in which the "ticket" is inserted, b2 indicates the state in which the "limited express ticket" is inserted, and b3 indicates the state in which the "boarding / limited express ticket" is inserted. The turned-in state is represented by 0 or 1, where 0 indicates a non-charged state, and 1 indicates a loaded state. However, the combination of expected input states is limited to the following cases.

Input | Input state | Door operation for input
--- | --- | ---
1 0 0 | Insert only "ticket" | Close
0 1 0 | Only "Limited Express Ticket" is introduced | Close
1 1 0 | Introducing "tickets" and "express tickets" | Open
0 0 1 | Introducing "Boarding / Limited Express Tickets" | Open
0 0 0 | No input | Close


output

Outputs Open or Close, which indicates the opening and closing of the automatic ticket gate, on one line.

Example

Input

0 0 1


Output

Open
"""

def check_ticket_gate_status(b1: int, b2: int, b3: int) -> str:
    if b1 == 1 and b2 == 1:
        return 'Open'
    elif b3 == 1:
        return 'Open'
    else:
        return 'Close'