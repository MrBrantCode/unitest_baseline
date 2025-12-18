"""
QUESTION:
A: Isono, let's do that! --Sendame -

story

Nakajima "Isono ~, let's do that!"

Isono "What is that, Nakajima"

Nakajima "Look, that's that. It's hard to explain because I have to express it in letters for some reason."

Isono "No, it seems that you can put in figures and photos, right?"

<image>

Nakajima "It's true!"

Isono "So what are you going to do?"

Nakajima "Look, the guy who rhythmically clapping his hands twice and then poses for defense, accumulation, and attack."

Isono "Hmm, I don't know ..."

Nakajima "After clapping hands twice, for example, if it was defense"

<image>

Nakajima "And if it was a reservoir"

<image>

Nakajima "If it was an attack"

<image>

Nakajima "Do you know who you are?"

Isono "Oh! It's dramatically easier to understand when a photo is included!"

Nakajima "This is the progress of civilization!"

(It's been a long time since then)

Hanazawa "Iso's" "I'm" "I'm"

Two people "(cracking ... crackling ... crackling ...)"

Hanazawa "You guys are doing that while sleeping ...!?"

Hanazawa: "You've won the game right now ... Isono-kun, have you won now?"

Isono "... Mr. Hanazawa was here ... Nakajima I'll do it again ... zzz"

Nakajima "(Kokuri)"

Two people "(cracking ... crackling ...)"

Hanazawa "Already ... I'll leave that winning / losing judgment robot here ..."

Then Mr. Hanazawa left.

Please write that winning / losing judgment program.

problem

"That" is a game played by two people. According to the rhythm, the two people repeat the pose of defense, accumulation, or attack at the same time. Here, the timing at which two people pose is referred to as "times". In this game, when there is a victory or defeat in a certain time and there is no victory or defeat in the previous times, the victory or defeat is the victory or defeat of the game.

Each of the two has a parameter called "attack power", and the attack power is 0 at the start of the game.

When the attack pose is taken, it becomes as follows according to the attack power at that time.

* If you pose for an attack when the attack power is 0, you will lose the foul. However, if the opponent also poses for an attack with an attack power of 0, he cannot win or lose at that time.
* If you pose for an attack when your attack power is 1 or more, you will attack your opponent. Also, if the opponent also poses for an attack at that time, the player with the higher attack power wins. However, if both players pose for an attack with the same attack power, they cannot win or lose at that time.



Also, at the end of the attack pose, your attack power becomes 0.

Taking a puddle pose increases the player's attack power by 1. However, if the attack power is 5, the attack power remains at 5 even if the player poses in the pool. If the opponent attacks in the time when you take the pose of the pool, the opponent wins. In addition, if the opponent takes a pose other than the attack in the time when the pose of the pool is taken, the victory or defeat cannot be determined.

If the opponent makes an attack with an attack power of 5 each time he takes a defensive pose, the opponent wins. On the other hand, if the opponent makes an attack with an attack power of 4 or less in the defense pose, or if the opponent poses for accumulation or defense, the victory or defeat cannot be achieved at that time. Even if you take a defensive pose, the attack power of that player does not change.

Since the poses of both players are given in order, output the victory or defeat. Both players may continue to pose after the victory or defeat is decided, but the pose after the victory or defeat is decided is ignored.

Input format

The input is given in the following format.


K
I_1_1
...
I_K
N_1_1
...
N_K


The first line of input is given an integer K (1 ≤ K ≤ 100). The pose I_i (1 ≤ i ≤ K) taken by Isono is given to the K lines from the second line in order. Immediately after that, the pose N_i (1 ≤ i ≤ K) taken by Nakajima is given to the K line in order. I_i and N_i are one of “mamoru”, “tameru”, and “kougekida”. These strings, in order, represent defense, pool, and attack poses.

Output format

Output “Isono-kun” if Isono wins, “Nakajima-kun” if Nakajima wins, and “Hikiwake-kun” if you cannot win or lose in K times.

Input example 1


3
tameru
tameru
tameru
tameru
kougekida
tameru


Output example 1


Nakajima-kun

In the second time, Isono is in the pose of the pool, while Nakajima is attacking with an attack power of 1, so Nakajima wins.

Input example 2


3
mamoru
mamoru
mamoru
tameru
tameru
tameru


Output example 2


Hikiwake-kun

Neither attacked, so I couldn't win or lose.

Input example 3


Five
tameru
tameru
mamoru
mamoru
kougekida
tameru
tameru
kougekida
tameru
kougekida


Output example 3


Isono-kun

There is no victory or defeat from the 1st to the 4th. In the 5th time, both players are posing for attack, but Isono's attack power is 2, while Nakajima's attack power is 1, so Isono wins.

Input example 4


3
kougekida
kougekida
tameru
kougekida
mamoru
kougekida


Output example 4


Nakajima-kun

In the first time, both players are posing for attack with 0 attack power, so there is no victory or defeat. In the second time, only Isono poses for an attack with an attack power of 0, so Nakajima wins.

Input example 5


8
tameru
mamoru
tameru
tameru
tameru
tameru
tameru
kougekida
tameru
kougekida
mamoru
mamoru
mamoru
mamoru
mamoru
mamoru


Output example 5


Isono-kun

In the second time, Nakajima poses for attack with an attack power of 1, but Isono poses for defense, so there is no victory or defeat. In the 7th time, Isono poses with an attack power of 5, so Isono's attack power remains at 5. In the 8th time, Isono poses for attack with an attack power of 5, and Nakajima poses for defense, so Isono wins.





Example

Input

3
tameru
tameru
tameru
tameru
kougekida
tameru


Output

Nakajima-kun
"""

def determine_winner(K, Is, Ns):
    atk_I = 0
    atk_N = 0
    
    for i, n in zip(Is, Ns):
        i_n = [i, n]
        
        if i_n.count('mamoru') == 2:
            pass
        elif i_n.count('mamoru') == 1:
            if i_n.count('tameru') == 1:
                if i[0] == 't':
                    atk_I += 1
                    if atk_I > 5:
                        atk_I = 5
                else:
                    atk_N += 1
                    if atk_N > 5:
                        atk_N = 5
            elif i[0] == 'k':
                if atk_I == 5:
                    return 'Isono-kun'
                elif atk_I == 0:
                    return 'Nakajima-kun'
                else:
                    atk_I = 0
            elif n[0] == 'k':
                if atk_N == 5:
                    return 'Nakajima-kun'
                elif atk_N == 0:
                    return 'Isono-kun'
                else:
                    atk_N = 0
        elif i_n.count('kougekida') == 2:
            if atk_I > atk_N:
                return 'Isono-kun'
            elif atk_I == atk_N:
                atk_I = 0
                atk_N = 0
            else:
                return 'Nakajima-kun'
        elif i_n.count('kougekida') == 1:
            if i[0] == 'k':
                if atk_I == 0:
                    return 'Nakajima-kun'
                else:
                    return 'Isono-kun'
            elif atk_N == 0:
                return 'Isono-kun'
            else:
                return 'Nakajima-kun'
        else:
            atk_I += 1 if atk_I != 5 else 0
            atk_N += 1 if atk_N != 5 else 0
    
    return 'Hikiwake-kun'