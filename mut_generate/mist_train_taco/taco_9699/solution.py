"""
QUESTION:
Cosmic market, commonly known as Kozumike, is the largest coterie spot sale in the universe. Doujin lovers of all genres gather at Kozumike. In recent years, the number of visitors to Kozumike has been increasing. If everyone can enter from the beginning, it will be very crowded and dangerous, so admission is restricted immediately after the opening. Only a certain number of people can enter at the same time as the opening. Others have to wait for a while before entering.

However, if you decide to enter the venue on a first-come, first-served basis, some people will line up all night from the day before. Many of Kozumike's participants are minors, and there are security issues, so it is not very good to decide on a first-come, first-served basis. For that reason, Kozumike can play some kind of game among the participants, and the person who survives the game gets the right to enter first. To be fair, we use highly random games every year.

I plan to participate in Kozumike again this time. I have a douujinshi that I really want to get at this Kozumike. A doujinshi distributed by a popular circle, which deals with the magical girl anime that became a hot topic this spring. However, this circle is very popular and its distribution ends immediately every time. It would be almost impossible to get it if you couldn't enter at the same time as the opening. Of course, there is no doubt that it will be available at douujin shops at a later date. But I can't put up with it until then. I have to get it on the day of Kozumike with any hand. Unfortunately, I've never been the first to enter Kozumike.

According to Kozumike's catalog, this time we will select the first person to enter in the following games. First, the first r × c of the participants sit in any of the seats arranged like the r × c grid. You can choose the location on a first-come, first-served basis, so there are many options if you go early. The game starts when r × c people sit down. In this game, all people in a seat in a row (row) are instructed to sit or stand a certain number of times. If a person who is already seated is instructed to sit down, just wait. The same is true for those who are standing up. The column (row) to which this instruction is issued and the content of the instruction are randomly determined by roulette. Only those who stand up after a certain number of instructions will be able to enter the venue first. Participants are not informed of the number of instructions, so they do not know when the game will end. So at some point neither standing nor sitting knows if they can enter first. That's why the catalog emphasizes that you can enjoy the thrill.

At 1:00 pm the day before Kozumike, I got all the data about this year's game. According to the information I got, the number of times this instruction, q, has already been decided. On the contrary, all the instructions for q times have already been decided. It is said that it has a high degree of randomness, but that was a lie. I don't know why it was decided in advance. But this information seems to me a godsend.

If the game is played according to this data, you will know all the seating locations where you can enter first. In the worst case, let's say all the participants except me had this information. Even in such a case, you should know the number of arrivals at the latest to enter the venue first. However, it seems impossible to analyze this instruction by hand from now on because it is too much. No matter how hard I try, I can't make it in time for Kozumike.

So I decided to leave this calculation to you. You often participate in programming contests and you should be good at writing math programs like this. Of course I wouldn't ask you to do it for free. According to the catalog, this year's Kozumike will be attended by a circle that publishes a doujinshi about programming contests. If I can enter at the same time as the opening, I will get the douujinshi as a reward and give it to you. Well, I'll take a nap for about 5 hours from now on. In the meantime, I believe you will give me an answer.



Input

The input consists of multiple cases. Each case is given in the following format.


r c q
A0 B0 order0
A1 B1 order1
..
..
..
Aq-1 Bq-1 orderq-1


When Ai = 0, the orderi instruction is executed for the Bi line.
When Ai = 1, the orderi instruction is executed for the Bi column.
When orderi = 0, all people in the specified row or column are seated.
When orderi = 1, make everyone stand in the specified row or column.


The end of the input is given by r = 0 c = 0 q = 0.

The input value satisfies the following conditions.
1 ≤ r ≤ 50,000
1 ≤ c ≤ 50,000
1 ≤ q ≤ 50,000
orderi = 0 or 1
When Ai = 0
0 ≤ Bi <r
When Ai = 1
0 ≤ Bi <c


The number of test cases does not exceed 100

Output

In the worst case, print out in one line how many times you should arrive to get the right to enter the venue first.

Example

Input

5 5 5
0 0 1
0 0 0
0 2 0
1 2 1
0 0 0
5 5 5
1 4 0
0 1 1
0 4 1
1 3 0
0 3 1
5 5 5
1 0 0
0 3 0
1 2 1
0 4 0
0 1 1
0 0 0


Output

4
13
8
"""

def calculate_arrival_time(r, c, q, instructions):
    # Reverse the instructions to process them in reverse order
    instructions.reverse()
    
    # Initialize tracking arrays for rows and columns
    r_used = [False] * r
    c_used = [False] * c
    
    # Initialize counters for unused rows and columns
    r_cnt = c
    c_cnt = r
    
    # Initialize the answer
    ans = 0
    
    # Process each instruction
    for (a, b, o) in instructions:
        if a == 0:
            if not r_used[b]:
                r_used[b] = True
                c_cnt -= 1
                if o:
                    ans += r_cnt
        else:
            if not c_used[b]:
                c_used[b] = True
                r_cnt -= 1
                if o:
                    ans += c_cnt
    
    return ans