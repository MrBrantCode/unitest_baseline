"""
QUESTION:
Anton likes to listen to fairy tales, especially when Danik, Anton's best friend, tells them. Right now Danik tells Anton a fairy tale:

"Once upon a time, there lived an emperor. He was very rich and had much grain. One day he ordered to build a huge barn to put there all his grain. Best builders were building that barn for three days and three nights. But they overlooked and there remained a little hole in the barn, from which every day sparrows came through. Here flew a sparrow, took a grain and flew away..."

More formally, the following takes place in the fairy tale. At the beginning of the first day the barn with the capacity of n grains was full. Then, every day (starting with the first day) the following happens:  m grains are brought to the barn. If m grains doesn't fit to the barn, the barn becomes full and the grains that doesn't fit are brought back (in this problem we can assume that the grains that doesn't fit to the barn are not taken into account).  Sparrows come and eat grain. In the i-th day i sparrows come, that is on the first day one sparrow come, on the second day two sparrows come and so on. Every sparrow eats one grain. If the barn is empty, a sparrow eats nothing. 

Anton is tired of listening how Danik describes every sparrow that eats grain from the barn. Anton doesn't know when the fairy tale ends, so he asked you to determine, by the end of which day the barn will become empty for the first time. Help Anton and write a program that will determine the number of that day!


-----Input-----

The only line of the input contains two integers n and m (1 ≤ n, m ≤ 10^18) — the capacity of the barn and the number of grains that are brought every day.


-----Output-----

Output one integer — the number of the day when the barn will become empty for the first time. Days are numbered starting with one.


-----Examples-----
Input
5 2

Output
4

Input
8 1

Output
5



-----Note-----

In the first sample the capacity of the barn is five grains and two grains are brought every day. The following happens:  At the beginning of the first day grain is brought to the barn. It's full, so nothing happens.  At the end of the first day one sparrow comes and eats one grain, so 5 - 1 = 4 grains remain.  At the beginning of the second day two grains are brought. The barn becomes full and one grain doesn't fit to it.  At the end of the second day two sparrows come. 5 - 2 = 3 grains remain.  At the beginning of the third day two grains are brought. The barn becomes full again.  At the end of the third day three sparrows come and eat grain. 5 - 3 = 2 grains remain.  At the beginning of the fourth day grain is brought again. 2 + 2 = 4 grains remain.  At the end of the fourth day four sparrows come and eat grain. 4 - 4 = 0 grains remain. The barn is empty. 

So the answer is 4, because by the end of the fourth day the barn becomes empty.
"""

def find_empty_day(n, m):
    def get_empty_before_birds(m, i):
        if i <= m + 1:
            return 0
        t = i - (m + 1)
        return t * (t + 1) // 2

    def get_total_empty_after_birds(m, i):
        return get_empty_before_birds(m, i) + i

    (low, high) = (1, n)
    while True:
        i = (low + high) // 2
        if get_total_empty_after_birds(m, i) < n:
            low = i + 1
        elif get_total_empty_after_birds(m, i - 1) < n <= get_total_empty_after_birds(m, i + 1):
            return i
        else:
            high = i - 1