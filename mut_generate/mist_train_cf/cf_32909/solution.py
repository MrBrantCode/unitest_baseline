"""
QUESTION:
Create a function called `add` that takes a new stock price `v` as input and updates the Percentage Price Oscillator (PPO) calculation. The function should return the current PPO value. The PPO is calculated using three exponential moving averages (EMAs): a short-term EMA, a long-term EMA, and a signal EMA. The PPO is then calculated as the difference between the short-term and long-term EMAs, divided by the long-term EMA, and multiplied by 100. The result is then used to update the signal EMA. The function should correctly handle the initial values of the EMAs and the PPO calculation.
"""

def add(self, v, short_alpha, long_alpha, signal_alpha, 
        short_ema=None, long_ema=None, signal_ema=None, 
        short=None, long=None, ppo=None):
    if short_ema is None:
        short_ema = {'value': None}
    if long_ema is None:
        long_ema = {'value': None}
    if signal_ema is None:
        signal_ema = {'value': None}

    alpha_short = short_alpha if short is None else (1 - short_alpha)
    alpha_long = long_alpha if long is None else (1 - long_alpha)

    if short is None:
        short = v
    else:
        short = short_alpha * v + alpha_short * short

    if long is None:
        long = v
    else:
        long = long_alpha * v + alpha_long * long

    if ppo is None:
        ppo = 0
    else:
        ppo = 0 if long == 0 else ((short - long) / long) * 100

    signal_alpha_new = signal_alpha
    alpha_signal = 1 - signal_alpha if signal_ema['value'] is None else signal_alpha

    if signal_ema['value'] is None:
        signal_ema['value'] = ppo
    else:
        signal_ema['value'] = signal_alpha_new * ppo + alpha_signal * signal_ema['value']

    short_ema['value'] = short
    long_ema['value'] = long

    return signal_ema['value'], short_ema, long_ema, signal_ema, short, long, ppo