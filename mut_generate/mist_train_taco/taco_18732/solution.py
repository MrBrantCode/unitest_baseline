"""
QUESTION:
The mean and standard deviation of a sample of data can be thrown off if the sample contains one or many outlier(s) :


(image source)

For this reason, it is usually a good idea to check for and remove outliers before computing the mean or the standard deviation of a sample. To this aim, your function will receive a list of numbers representing a sample of data. Your function must remove any outliers and return the mean of the sample, rounded to two decimal places (round only at the end).

Since there is no objective definition of "outlier" in statistics, your function will also receive a cutoff, in standard deviation units. So for example if the cutoff is 3, then any value that is more than 3 standard deviations above or below the mean must be removed. Notice that, once outlying values are removed in a first "sweep", other less extreme values may then "become" outliers, that you'll have to remove as well!
Example :
```python
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
clean_mean(sample, cutoff) → 5.5
```

Formula for the mean :

(where n is the sample size)

Formula for the standard deviation :

(where N is the sample size, xi is observation i and x̄ is the sample mean)

Note : since we are not computing the sample standard deviation for inferential purposes, the denominator is n, not n - 1.
"""

def calculate_clean_mean(sample, cutoff):
    def mean(data):
        return sum(data) / len(data)
    
    def std_dev(data, mean_val):
        return (sum((num - mean_val) ** 2 for num in data) / len(data)) ** 0.5
    
    sample_mean = mean(sample)
    sample_std_dev = std_dev(sample, sample_mean)
    
    cleaned = [num for num in sample if abs(num - sample_mean) <= cutoff * sample_std_dev]
    
    if len(cleaned) == len(sample):
        return round(sample_mean, 2)
    else:
        return calculate_clean_mean(cleaned, cutoff)