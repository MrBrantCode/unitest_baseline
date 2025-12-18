"""
QUESTION:
Animation is one of methods for making movies and in Japan, it is popular to broadcast as a television program or perform as a movie. Many people, especially the young, love one. And here is an anime lover called Jack. We say he is an mysterious guy with uncertain age. He likes anime which are broadcasted in midnight and early morning especially.

In his room, there is a huge piece of paper on the wall. He writes a timetable of TV anime on it. In his house, he can watch all Japanese TV anime programs that are broadcasted in Japan using a secret and countrywide live system. However he can not watch all anime and must give up to watch some programs because they are "broadcasted at the same time" in a season. Here, programs are "broadcasted at the same time" means that two or more programs have one or more common minutes in broadcasting time. Increasing the number of anime programs in recent makes him nervous. Actually, some people buy DVDs after the program series ends or visit a web site called vhefoo. Anyway, he loves to watch programs on his live system. Of course, he is not able to watch two or more programs at the same time. However, as described above, he must give up some programs broadcasted at the same time. Therefore, he has a set of programs F and he watches programs in a set F absolutely.

Your task is to write a program that reads a timetable and outputs the maximum number of watchable programs, keeping that Jack watches all programs in the set F. Of course, there are multiple choices of programs, so we want the number of programs he can watch. If two or more programs in a set F are broadcasted at the same time, you must give Jack an unfortunate announcement. In this case, your program outputs -1. In addition, each anime program is a program of 30 minutes.

Hint

Second dataset: He can watch program E after watching B. Then he can choose a program either I or J after watching H. Therefore he can watch maximum 4 programs.

Constraints

The number of datasets is less than or equal to 400.
1≤N≤500

Input

Input consists of multiple datasets.
A dataset is given in a following format.


N
PROGRAM1
PROGRAM2
...
PROGRAMN
P
FAV1
FAV2
...
FAVP


N is the number of programs in a season.
PROGRAMi(1≤i≤N)is a string which has the following format.


name weekday start


* name is a program name. This is a a string having between 1 and 32 characters and these names do not overlap each other program. A name consists of alphanumeric characters and '_'(underscore).
* weekday is a broadcasting weekday about the corresponding program. This is an integer. 0 means Sunday and 1 is Monday and so on (2:Tuesday, 3:Wednesday, 4:Thursday, 5:Friday, 6:Saturday).
* start is a starting time of the program broadcasting. This is an integer between 600 and 2929. First one or two digits represent hour and the last two digits represent minute. If the hour has one digit it will be a representation "900" for example. Note: a program may have an integer more than or equal to 2400 as start, if the program begins the next day. For example, a program begins from 2500 on Monday should be interpreted as a program begins from 0100 on Tuesday. There are no input the minute of start exceeds 59. And when the hour of start is equal to 29, there are no input the minute of start exceeds 29.



P is an integer and represents the number of elements in the set F. And FAVi(1≤i≤P≤N) is a string for a program name which Jack watches absolutely. You can assume names which are not given in program descriptions will not appear in the set F.
The last line contains a single 0 which represents the end of input.

Output

For each dataset, output an integer S that represents maximum number of programs Jack can watch in the following format.


S


Example

Input

1
galaxy_angel 0 600
1
galaxy_angel
11
A 0 600
B 0 610
C 0 610
D 0 610
E 0 640
EE 0 700
F 0 710
G 0 710
H 0 710
I 0 740
J 0 750
2
B
H
42
nchj 6 2620
anhnnnmewbktthsrn 4 2515
gntmdsh 1 1800
achnnl 4 2540
hnskirh 0 2200
aonexrcst 0 1700
dgdys 6 2330
hdnnara 4 2525
dnpaonntssotk 4 2555
ddmnwndrlnd 6 2500
C 4 2445
astrttnomch 0 2330
seknnqasr 1 2630
sftnt 4 2630
stnsgt 2 2605
drrnenmknmrmr 4 2610
hnzm 6 2713
yndmsoazzlsn 6 2658
mrahlcalv 4 2615
hshzrhkkrhs 1 900
ortchntsbshni 0 2430
kmnmzshrski 1 2530
sktdnc 4 1800
gykkybrkjhkirkhn 2 2459
trk 0 900
30zzsinhkntiik 3 2700
sngkotmmmirprdx 1 2600
yran 2 2529
tntissygntinybu 1 2614
skiichhtki 5 2505
tgrbnny 6 2558
dnbrsnki 3 1927
yugozxl 1 1930
frbllchrmn 1 1928
fjrg 1 1955
shwmngtr 0 2200
xmn 5 2200
rngnkkrskitikihn 0 2100
szysz 0 1254
prttyrythmaulrdrm 6 1000
sckiesfrntrqst 5 1820
mshdr 1 2255
1
mrahlcalv
0


Output

1
4
31
"""

def max_watchable_programs(n, programs, favorites):
    if n == 0:
        return 0

    dic = {}
    tbl = []

    for i in range(n):
        nm, w, s = programs[i]
        w, s = int(w), int(s)
        h, m = s // 100, s % 100
        s = (1440 * w + h * 60 + m) % 10080
        e = s + 30
        tbl.append([s, e, 0, nm])
        dic[nm] = i

    for fav in favorites:
        tbl[dic[fav]][2] = 1

    if n == 1:
        return 1

    tbl.sort(key=lambda x: (x[0], x[2]))

    for i in range(len(tbl)):
        if tbl[i][2]:
            k = i
            break

    ans, i, j = 1, k, k

    while True:
        j += 1
        if i >= n:
            i = 0
        if j >= n:
            j = 0
        if j == k:
            break
        e = tbl[i][1] - 10080 if tbl[i][1] >= 10080 else 0
        if tbl[i][0] <= tbl[j][0] and tbl[j][0] < tbl[i][1] or tbl[j][0] < e:
            if tbl[j][2] and tbl[i][2]:
                return -1
            elif tbl[j][2]:
                i = j
        elif tbl[j][0] <= tbl[k][0] and tbl[k][0] < tbl[j][1]:
            pass
        else:
            ans += 1
            i = j

    return ans