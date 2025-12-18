"""
QUESTION:
Consider a system of n water taps all pouring water into the same container. The i-th water tap can be set to deliver any amount of water from 0 to a_{i} ml per second (this amount may be a real number). The water delivered by i-th tap has temperature t_{i}.

If for every $i \in [ 1, n ]$ you set i-th tap to deliver exactly x_{i} ml of water per second, then the resulting temperature of water will be $\frac{\sum_{i = 1}^{n} x_{i} t_{i}}{\sum_{i = 1}^{n} x_{i}}$ (if $\sum_{i = 1}^{n} x_{i} = 0$, then to avoid division by zero we state that the resulting water temperature is 0).

You have to set all the water taps in such a way that the resulting temperature is exactly T. What is the maximum amount of water you may get per second if its temperature has to be T?


-----Input-----

The first line contains two integers n and T (1 ≤ n ≤ 200000, 1 ≤ T ≤ 10^6) — the number of water taps and the desired temperature of water, respectively.

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^6) where a_{i} is the maximum amount of water i-th tap can deliver per second.

The third line contains n integers t_1, t_2, ..., t_{n} (1 ≤ t_{i} ≤ 10^6) — the temperature of water each tap delivers.


-----Output-----

Print the maximum possible amount of water with temperature exactly T you can get per second (if it is impossible to obtain water with such temperature, then the answer is considered to be 0).

Your answer is considered correct if its absolute or relative error doesn't exceed 10^{ - 6}.


-----Examples-----
Input
2 100
3 10
50 150

Output
6.000000000000000

Input
3 9
5 5 30
6 6 10

Output
40.000000000000000

Input
2 12
1 3
10 15

Output
1.666666666666667
"""

def calculate_max_water_volume(n, T, a, t):
    max_volume = 0.0
    temp = 0
    higher_sources = []
    lower_sources = []
    
    for i in range(n):
        volume = a[i]
        temperature = t[i]
        delta_temp = temperature - T
        if delta_temp > 0:
            higher_sources.append((volume, delta_temp))
        elif delta_temp < 0:
            lower_sources.append((volume, delta_temp))
        max_volume += volume
        temp += volume * delta_temp
    
    higher_sources.sort(key=lambda v: v[1])
    lower_sources.sort(key=lambda v: -v[1])
    
    while abs(temp / max_volume) >= 1e-06 and (len(lower_sources) > 0 or temp >= 0) and (len(higher_sources) > 0 or temp <= 0):
        if temp < 0:
            (volume, delta_temp) = lower_sources.pop()
            if temp - delta_temp * volume >= 0:
                required_volume = temp / delta_temp
                return max_volume - required_volume
            temp -= delta_temp * volume
            max_volume -= volume
        else:
            (volume, delta_temp) = higher_sources.pop()
            if temp - delta_temp * volume <= 0:
                required_volume = temp / delta_temp
                return max_volume - required_volume
            temp -= delta_temp * volume
            max_volume -= volume
    
    if abs(temp / max_volume) < 1e-06:
        return max_volume
    
    return 0.0