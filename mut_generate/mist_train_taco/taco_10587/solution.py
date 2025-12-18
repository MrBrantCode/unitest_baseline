"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Vietnamese], and [Bengali] as well.

You are given the height $H$ (in metres) and mass $M$ (in kilograms) of Chef. The Body Mass Index (BMI) of a person is computed as $\frac{M}{H^{2}}$.

Report the category into which Chef falls, based on his BMI:

Category 1: Underweight if BMI $≤ 18$
Category 2: Normal weight if BMI $\in \{19$, $20$,$\ldots$, $24\}$
Category 3: Overweight if BMI $\in \{25$, $26$,$\ldots$, $29\}$
Category 4: Obesity if BMI $≥ 30$

------ Input: ------

The first line of input will contain an integer, $T$, which denotes the number of testcases. Then the testcases follow. 
Each testcase contains a single line of input, with two space separated integers, $M, H$, which denote the mass and height of Chef respectively. 

------ Output: ------
For each testcase, output in a single line, $1, 2, 3$ or $4$, based on the category in which Chef falls.

------ Constraints  ------
$1 ≤ T ≤ 2*10^{4}$
$1 ≤ M ≤ 10^{4}$
$1 ≤ H ≤ 10^{2}$
Its guaranteed that $H^{2}$ divides $M$.

----- Sample Input 1 ------ 
3
72 2
80 2
120 2
----- Sample Output 1 ------ 
1
2
4
----- explanation 1 ------ 
Case 1: Since $\frac{M}{H^{2}} = \frac{72}{2^{2}} = 18$, therefore person falls in category $1$.

Case 2: Since $\frac{M}{H^{2}} = \frac{80}{2^{2}} = 20$, therefore person falls in category $2$.

Case 3: Since $\frac{M}{H^{2}} = \frac{120}{2^{2}} = 30$, therefore person falls in category $4$.
"""

def calculate_bmi_category(mass: int, height: int) -> int:
    """
    Calculate the BMI category based on the given mass and height.

    :param mass: The mass of Chef in kilograms.
    :param height: The height of Chef in meters.
    :return: An integer representing the BMI category (1, 2, 3, or 4).
    """
    BMI = mass // (height ** 2)
    
    if BMI <= 18:
        return 1
    elif 19 <= BMI <= 24:
        return 2
    elif 25 <= BMI <= 29:
        return 3
    else:
        return 4