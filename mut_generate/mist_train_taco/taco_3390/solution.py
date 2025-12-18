"""
QUESTION:
In a fictitious city of CODASLAM there were many skyscrapers. The mayor of the city decided to make the city beautiful and for this he decided to arrange the skyscrapers in descending order of their height, and the order must be strictly decreasing but he also didn’t want to waste much money so he decided to get the minimum cuts possible. Your job is to output the minimum value of cut that is possible to arrange the skyscrapers in descending order.

-----Input-----

*First line of input is the number of sky-scrappers in the city
*Second line of input is the height of the respective sky-scrappers


-----Output-----

* Your output should be the minimum value of cut required to arrange these sky-scrappers in descending order.

-----Example-----
Input:
5
1 2 3 4 5

Output:
8

By:
Chintan,Asad,Ashayam,Akanksha
"""

def minimum_cuts_to_descending_order(num_skyscrapers, skyscraper_heights):
    skyscraper_heights.reverse()
    cuts = 0
    change = 0
    t = False
    i = 1
    
    while i < len(skyscraper_heights):
        if skyscraper_heights[i] <= skyscraper_heights[i - 1]:
            for j in range(i - 1, -1, -1):
                if skyscraper_heights[j] <= skyscraper_heights[i] - (i - j):
                    break
                else:
                    change += skyscraper_heights[j] - (skyscraper_heights[i] - (i - j))
                if change >= skyscraper_heights[i]:
                    change = skyscraper_heights[i]
                    t = True
                    break
            cuts += change
            if t:
                del skyscraper_heights[i]
                t = False
                i -= 1
            else:
                for j in range(i - 1, -1, -1):
                    if skyscraper_heights[j] < skyscraper_heights[i] - (i - j):
                        break
                    else:
                        skyscraper_heights[j] = skyscraper_heights[i] - (i - j)
        i += 1
        change = 0
    
    return cuts