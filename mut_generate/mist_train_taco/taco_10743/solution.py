"""
QUESTION:
problem

You are in charge of quality control at a machine manufacturing plant. This machine requires a power supply, a motor, and a cable as parts. The manufacturing plant has a power supply, b motors, and c cables, numbered from 1 to a, a + 1 to a + b, and a + b + 1 to a + b + c, respectively. attached. The trouble is that some parts may be out of order. I want to know which parts are out of order and which parts are normal in the factory.

Therefore, the factory inspected the parts by the following method. Bring the power supply, motor, and cable one by one, connect them, and try to operate them. At this time, if all three parts are normal, it operates correctly and is recognized as "passed". If any of the three parts is out of order, it will not operate properly and will be recognized as "failed". (Since the machines made in the factory are so precise, it does not happen that the broken parts are mixed and operate correctly by accident.)

You will be given a list of test results. Each line in the list of test results shows the numbers of the power supply, motor, and cable used for the test, and whether the test passed or failed.

Given a list of inspection results, all parts are either faulty or normal from the inspection results, some are definitely faulty, some are definitely normal. Create a program to classify parts that are not decided.



input

The input consists of multiple datasets. The format of each data set is as follows. The input ends on a line containing three zeros.

Three integers are written on the first line, separated by blanks, and represent the number of power supplies a, the number of motors b, and the number of cables c in order.

One integer is written on the second line, and the number of tests N included in the list of test results is written.

The next N lines represent a list of test results. On each line, four integers i, j, k, r are written with one blank as a delimiter, and the result of inspection by connecting the power supply i, the motor j, and the cable k is "pass" (r = 1). (When) or "Fail" (when r = 0).

a, b, c, N satisfy 1 ≤ a, b, c ≤ 100, 1 ≤ N ≤ 1000.

The number of datasets does not exceed 5.

output

Output in the following format for each data set. The output of each dataset consists of lines a + b + c.

Line i (1 ≤ i ≤ a + b + c):

* If the inspection result shows that the part i is out of order, 0 is output.
* If the inspection result shows that the part i is normal, 1 is output.
* Output 2 if the inspection result does not determine whether part i is defective or normal.

Examples

Input

2 2 2
4
2 4 5 0
2 3 6 0
1 4 5 0
2 3 5 1
0 0 0


Output

2
1
1
0
1
0


Input

None


Output

None
"""

def classify_parts(a, b, c, test_results):
    total_parts = a + b + c
    status = [2] * (total_parts + 1)  # Initialize status list with 2 (undetermined)
    failed_tests = []

    for i, j, k, r in test_results:
        if r == 1:
            status[i] = status[j] = status[k] = 1  # Mark all parts as normal if test passes
        else:
            failed_tests.append((i, j, k))

    for i, j, k in failed_tests:
        if status[j] == 1 and status[k] == 1:
            status[i] = 0  # If motor and cable are normal, power supply must be faulty
        if status[k] == 1 and status[i] == 1:
            status[j] = 0  # If power supply and cable are normal, motor must be faulty
        if status[i] == 1 and status[j] == 1:
            status[k] = 0  # If power supply and motor are normal, cable must be faulty

    return status[1:]  # Return the status list excluding the first element (which is unused)