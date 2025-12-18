"""
QUESTION:
Nearly each project of the F company has a whole team of developers working on it. They often are in different rooms of the office in different cities and even countries. To keep in touch and track the results of the project, the F company conducts shared online meetings in a Spyke chat.

One day the director of the F company got hold of the records of a part of an online meeting of one successful team. The director watched the record and wanted to talk to the team leader. But how can he tell who the leader is? The director logically supposed that the leader is the person who is present at any conversation during a chat meeting. In other words, if at some moment of time at least one person is present on the meeting, then the leader is present on the meeting.

You are the assistant director. Given the 'user logged on'/'user logged off' messages of the meeting in the chronological order, help the director determine who can be the leader. Note that the director has the record of only a continuous part of the meeting (probably, it's not the whole meeting).

Input

The first line contains integers n and m (1 ≤ n, m ≤ 105) — the number of team participants and the number of messages. Each of the next m lines contains a message in the format:

  * '+ id': the record means that the person with number id (1 ≤ id ≤ n) has logged on to the meeting. 
  * '- id': the record means that the person with number id (1 ≤ id ≤ n) has logged off from the meeting. 



Assume that all the people of the team are numbered from 1 to n and the messages are given in the chronological order. It is guaranteed that the given sequence is the correct record of a continuous part of the meeting. It is guaranteed that no two log on/log off events occurred simultaneously.

Output

In the first line print integer k (0 ≤ k ≤ n) — how many people can be leaders. In the next line, print k integers in the increasing order — the numbers of the people who can be leaders.

If the data is such that no member of the team can be a leader, print a single number 0.

Examples

Input

5 4
+ 1
+ 2
- 2
- 1


Output

4
1 3 4 5 

Input

3 2
+ 1
- 2


Output

1
3 

Input

2 4
+ 1
- 1
+ 2
- 2


Output

0


Input

5 6
+ 1
- 1
- 3
+ 3
+ 4
- 4


Output

3
2 3 5 

Input

2 4
+ 1
- 2
+ 2
- 1


Output

0
"""

def find_possible_leaders(n, m, messages):
    posibles_jefes = set(range(1, n + 1))
    anteriores = set()
    posteriores = set()
    continuos = [True] * (n + 1)
    mencionados = set()
    posibles_jefes_mencionados = set()
    ultimo_en_salir = [True] * (n + 1)
    ultima_salida_inesperada = None
    
    for i in range(m):
        (op, num) = messages[i]
        cont = False
        if op == '+':
            cont = not i or (messages[i - 1][0] == '-' and messages[i - 1][1] == num)
            posteriores.add(num)
        if op == '-':
            cont = i == m - 1 or (messages[i + 1][0] == '+' and messages[i + 1][1] == num)
            if num not in mencionados:
                anteriores.add(num)
                ultima_salida_inesperada = num
            posteriores.discard(num)
            ultimo_en_salir[num] &= not posteriores
        continuos[num] &= cont
        mencionados.add(num)
    
    if not anteriores and not posteriores:
        if messages[0][0] == '+' and messages[-1][0] == '-' and (messages[0][1] == messages[-1][1]) and continuos[messages[0][1]] and ultimo_en_salir[messages[0][1]]:
            posibles_jefes_mencionados.add(messages[0][1])
    elif not posteriores:
        posibles_jefes_filtrados = list(filter(lambda x: continuos[x] and ultimo_en_salir[x] and (ultima_salida_inesperada == x), anteriores))
        if posibles_jefes_filtrados:
            posibles_jefes_mencionados.add(messages[-1][1])
    elif not anteriores:
        posibles_jefes_filtrados = list(filter(lambda x: continuos[x] and ultimo_en_salir[x], posteriores))
        if posibles_jefes_filtrados:
            posibles_jefes_mencionados.add(messages[0][1])
    else:
        posibles_jefes_mencionados = set(filter(lambda x: ultimo_en_salir[x] and continuos[x] and (ultima_salida_inesperada == x), anteriores & posteriores))
    
    posibles_jefes -= mencionados - posibles_jefes_mencionados
    
    return len(posibles_jefes), sorted(posibles_jefes)