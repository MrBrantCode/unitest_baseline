"""
QUESTION:
We have a distribution of probability of a discrete variable (it may have only integer values)
```
x       P(x)
0       0.125
1       0.375
2       0.375
3       0.125
Total = 1.000   # The sum of the probabilities for all the possible values should be one (=1)
```
The mean, ```μ```,  of the values of x is:



For our example
```
μ = 0*0.125 + 1*0.375 + 2*0.375 + 3*0.125 = 1.5
```

The variance, ```σ²``` is:



For our example :
```
σ² = 0.75
```

The standard deviation, ```σ``` is:



Finally, for our example:
```
σ = 0.8660254037844386
```
Make the function ```stats_disc_distr()``` that receives a 2D array. Each internal array will have a pair of values: the first one, the value of the variable ```x``` and the second one its correspondent probability, ```P(x)```.

For the example given above:
```python
stats_disc_distr([[0, 0.125], [1, 0.375], [2, 0.375], [3, 0.125]]) == [1.5, 0.75, 0.8660254037844386]
```
The function should check also if it is a valid distribution.

If the sum of the probabilities is different than ```1```, the function should output an alert.
```python
stats_disc_distr([[0, 0.425], [1, 0.375], [2, 0.375], [3, 0.125]]) == "It's not a valid distribution"
```
If one of the values of ```x``` is not an integer, the function will give a specific alert:
```python
stats_disc_distr([[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]]) == "All the variable values should be integers"
```

If the distribution has both problems will output another specific alert:
```python
stats_disc_distr([[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]]) == "It's not a valid distribution and furthermore, one or more variable value are not integers"
```
But if a value is a float with its decimal part equals to 0 will proceed without inconveniences, (if the sum of probabilities is ```1```:
```python
stats_disc_distr([[0.0, 0.125], [1.0, 0.375], [2.0, 0.375], [3, 0.125]]) == [1.5, 0.75, 0.8660254037844386]
```

The 2Darray will not have any strings.

Enjoy it!!
"""

def stats_disc_distr(distrib):
    def check_errors(distrib):
        errors = 0
        if not isclose(sum((x[1] for x in distrib)), 1):
            errors += 1
        if not all((isinstance(x[0], int) or (isinstance(x[0], float) and x[0].is_integer()) for x in distrib)):
            errors += 2
        if errors > 0:
            return {
                1: "It's not a valid distribution",
                2: "All the variable values should be integers",
                3: "It's not a valid distribution and furthermore, one or more variable value are not integers"
            }[errors]
        return None

    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

    err = check_errors(distrib)
    if err:
        return err

    mean = sum((x[0] * x[1] for x in distrib))
    var = sum(((x[0] - mean) ** 2 * x[1] for x in distrib))
    std_dev = var ** 0.5

    return [mean, var, std_dev]