"""
QUESTION:
Problem Statement

Mr. Takatsuki, who is planning to participate in the Aizu training camp, has a poor house and does not have much money. Therefore, he is trying to save money by using the Seishun 18 Ticket. With only one 18 ticket, you can ride a local train all day long, and you can enter and exit the ticket gates freely (detailed usage rules are omitted).

The attraction of the 18 Ticket is that you can use your spare time to see local souvenirs at the station where you change trains. She wants to visit various stations during her trip because it is a great opportunity. However, since I don't want to miss the next train, I decided to look around the station only when the time between the time I arrived at the transfer station and the time I left the transfer station was T minutes or more.

You will be given a transfer plan using Mr. Takatsuki's 18 ticket, so output the name and time of the station you can look around. Please note that the station that departs first and the station that arrives last are not candidates for exploration.

Constraints

* 1 <= N <= 10
* 1 <= T <= 180
* st_timei, ar_timei
* Represented by "HH: MM", HH is 00 or more and 23 or less, and MM is 00 or more and 59 or less. HH is hours and MM is minutes.
* 00:00 <= st_time1 <ar_time1 <st_time2 <ar_time2 <... <st_timeN <ar_timeN <= 23:59
* st_namei, ar_namei
* A character string represented by uppercase and lowercase letters.
* 1 <= string length <= 50
* The names of the i-th arrival station ar_namei and the i + 1th departure station st_namei + 1 match.
* The names of st_name1, ar_nameN, and the transfer station are different character strings.

Input

Each data set is input in the following format.


N T
st_time1 st_name1 ar_time1 ar_name1
st_time2 st_name2 ar_time2 ar_name2
...
st_timeN st_nameN ar_timeN ar_nameN


N is an integer representing the number of times the train is boarded, and T is an integer representing the permissible time (minutes) to see the transfer station. Subsequently, train departure and arrival pairs are given over N lines. The input of each line means that the train that Mr. Takatsuki rides departs from the station of st_namei at the time of st_timei, and that the train that Mr. Takatsuki rides arrives at the station of ar_namei at the time of ar_timei.

Output

Output in the following format for each data set.


M
stay_name1 stay_time1
stay_name2 stay_time2
...
stay_nameM stay_timeM


M (0 <= M <= N -1) is an integer that represents the number of stations you can look around. Then, over M lines, a list of stations that can be visited is output in ascending order of time. Each line means that you can walk around the station of stay_namei for stay_timei minutes.

Examples

Input

N T
st_time1 st_name1 ar_time1 ar_name1
st_time2 st_name2 ar_time2 ar_name2
...
st_timeN st_nameN ar_timeN ar_nameN


Output

2
Kanazawa 55
Niitsu 24


Input

8 24
05:30 Kyoto 06:37 Maibara
06:50 Maibara 07:36 Tsuruga
07:42 Tsuruga 10:03 Kanazawa
10:58 Kanazawa 12:07 Toyama
12:15 Toyama 14:12 Naoetsu
14:29 Naoetsu 15:57 Nagaoka
16:11 Nagaoka 17:14 Niitsu
17:38 Niitsu 20:06 AizuWakamatsu


Output

2
Kanazawa 55
Niitsu 24


Input

1 180
10:44 Koriyama 11:52 AizuWakamatsu


Output

0
"""

def find_explorable_stations(N, T, schedule):
    def time_to_minutes(time_str):
        """Convert time string 'HH:MM' to total minutes."""
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    explorable_stations = []
    current_time = time_to_minutes(schedule[0][2])  # Initial arrival time

    for i in range(1, N):
        next_departure_time = time_to_minutes(schedule[i][0])
        if next_departure_time - current_time >= T:
            explorable_stations.append((schedule[i-1][3], next_departure_time - current_time))
        current_time = time_to_minutes(schedule[i][2])

    return len(explorable_stations), explorable_stations