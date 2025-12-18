"""
QUESTION:
Take the'IOI'train

A new railway has been laid in IOI. Trains running on railways in IOI are a combination of several vehicles, and there are two types of vehicles, I and O. Vehicles can only be connected to different types of vehicles. Also, because the train has a driver's seat, the cars at both ends of the train must be of type I. A train is represented by a character string in which characters indicating the type of vehicle are connected in order, and the length of the train is assumed to be the length of the character string. For example, if vehicles are connected in the order of IOIOI, a train with a length of 5 can be formed, and vehicle I is a train with a length of 1 alone. Trains cannot be formed by arranging vehicles in the order of OIOI or IOOI.

Some vehicles are stored in two garages. Vehicles are lined up in a row in each garage. When forming a train, take out the train from the garage and connect it in front of the garage. Only the vehicle closest to the entrance of the garage can be taken out of the garage, but the order of taking out the vehicle from which garage is arbitrary.

Before forming a train, you can take as many cars out of the garage as you like and move them to another waiting rail. Vehicles that have been moved to the standby rails cannot be used to organize trains in the future. Also, once the train formation is started, the vehicle cannot be moved from the garage to the standby rail until the formation is completed.

When organizing a train, it is not necessary to use up all the cars in the garage. That is, after the train formation is completed, unused cars may remain in the garage.

It is believed that there are so many people on the railroad in IOI, so I want to organize the longest possible train.

<image>


Figure: The train is being organized, and the vehicle in the garage cannot be moved to the standby rail at this time. This figure corresponds to I / O example 1.

Task

Create a program to find the maximum length of trains that can be organized given the information of the cars stored in the garage. The row of vehicles stored in each garage is represented by a string consisting of only two types of letters I and O, and the information in the two garages is represented by the string S of length M and the string T of length N, respectively. Given. Each letter represents one vehicle, the letter of which is the same as the type of vehicle. The first letter of the string represents the vehicle closest to the entrance to the garage, and the last letter represents the vehicle closest to the garage.

Limits

* 1 ≤ M ≤ 2000 Length of string S
* 1 ≤ N ≤ 2000 Length of string T



input

Read the following data from standard input.

* In the first line, M and N are written separated by blanks.
* The character string S is written on the second line.
* The character string T is written on the third line.



output

Output an integer representing the maximum train length that can be organized to the standard output on one line. If no train can be organized, output 0.

Input / output example

Input example 1


5 5
OIOOI
OOIOI


Output example 1


7


Let the garage represented by S be the garage S and the garage represented by T be the garage T. At this time, for example, the first vehicle from the garage S, the first two vehicles from the garage T are put out and put on standby, and then the garage S, the garage S, the garage T, the garage S, the garage S, the garage T, and the garage T are placed in this order. If you take out the vehicle, you can form a train IOIOIOI with a length of 7.

In addition, after the first vehicle from garage S and the first two vehicles from garage T are put out and put on standby, the order is garage T, garage T, garage S, garage S, garage T, garage S, and garage S. You can also organize a 7-length train by putting out a vehicle. Since it is not possible to form a train longer than this, 7 is output.




Input example 2


5 9
IIIII
IIIIIIIII


Output example 2


1


Note that train I, which consists of only one car, also meets the conditions for a train.

The question text and the data used for the automatic referee are the question text and the test data for scoring, which are created and published by the Japan Committee for Information Olympics.





Example

Input

5 5
OIOOI
OOIOI


Output

7
"""

def max_train_length(M: int, N: int, S: str, T: str) -> int:
    INF = 10 ** 18
    dp0 = [[0] * (N + 1) for _ in range(M + 1)]
    dp1 = [[-INF] * (N + 1) for _ in range(M + 1)]
    
    for p in range(M + 1):
        for q in range(N + 1):
            v0 = dp0[p][q]
            v1 = dp1[p][q]
            if p < M:
                if S[p] == 'I':
                    dp1[p + 1][q] = max(dp1[p + 1][q], v0 + 1)
                else:
                    dp0[p + 1][q] = max(dp0[p + 1][q], v1 + 1)
            if q < N:
                if T[q] == 'I':
                    dp1[p][q + 1] = max(dp1[p][q + 1], v0 + 1)
                else:
                    dp0[p][q + 1] = max(dp0[p][q + 1], v1 + 1)
    
    ans = max((max(e) for e in dp1))
    return max(ans, 0)