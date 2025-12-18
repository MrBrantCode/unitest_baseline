"""
QUESTION:
Saurabh and Pranav play the popular game of Hungry Birds on windows and android phones respectively.

The game goal is to destroy birds in the Hungry Birds Game. A certain number of points is given for destroying each bird depending on the bird type and the current factor value.

There are n types of Hungry Birds. The number of birds of type ai and bird cost ci is known for each bird type. A player gets ci.f points for destroying one bird of type i, where f is the current factor. The factor value can be an integer number from 1 to t + 1, inclusive. At the beginning of the game the factor value is equal to 1. The factor is set to i + 1 after destruction of pi (1 ≤ i ≤ t) birds, so the (pi + 1)-th bird to be destroyed is considered with factor equal to i+1.

Your task is to determine the maximum number of points Saurabh and Pranav can get after they destroy all birds. Take into account that they are so tough that they can destroy birds in any order chosen by them individually on their respective phones. 

Input :
The first line contains the only integer number n (1 ≤ n ≤ 100) — the number of bird types.

Each of the following n lines contains two integer numbers ai and ci (1 ≤ ai ≤ 10^9, 0 ≤ ci ≤ 1000), separated with space — the number of birds of the i-th type and the cost of one i-type bird, correspondingly.

The next line contains the only integer number t (1 ≤ t ≤ 100) — the number that describe the factor's changes.

The next line contains t integer numbers pi (1 ≤ p1 < p2 < ... < pt ≤ 10^12), separated with spaces. 

Output :
Print the only number — the maximum number of points they can get. 

SAMPLE INPUT
2
3 8
5 10
1
20

SAMPLE OUTPUT
74
"""

def calculate_max_points(n, bird_data, t, factors):
    # Sort bird data by cost in ascending order
    bird_data.sort()
    bird_data.append((4000, 0))  # Sentinel value to simplify the loop
    
    # Calculate total number of birds
    total_birds = sum(birds for _, birds in bird_data)
    
    # Append total_birds + 1 to factors to simplify the loop
    factors.append(total_birds + 1)
    
    bird_count = 0
    f_i = 0
    factor = 1
    b_i = 0
    score = 0
    
    while b_i < len(bird_data) and f_i < len(factors) and bird_count < total_birds:
        if bird_count + bird_data[b_i][1] < factors[f_i]:
            bird_count += bird_data[b_i][1]
            score += bird_data[b_i][1] * bird_data[b_i][0] * factor
            b_i += 1
        elif bird_count + bird_data[b_i][1] > factors[f_i]:
            birds_covered = factors[f_i] - bird_count
            score += birds_covered * bird_data[b_i][0] * factor
            bird_data[b_i] = (bird_data[b_i][0], bird_data[b_i][1] - birds_covered)
            bird_count += birds_covered
            f_i += 1
            factor += 1
        else:
            bird_count += bird_data[b_i][1]
            score += bird_data[b_i][1] * bird_data[b_i][0] * factor
            f_i += 1
            factor += 1
            b_i += 1
    
    return score