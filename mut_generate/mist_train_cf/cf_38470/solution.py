"""
QUESTION:
Implement the `simulate_network` function, which simulates the dynamics of a neural network model with two populations of neurons: excitatory (E) and inhibitory (I). The function should take in a dictionary `pars` containing the following parameters:

- `wEE`, `wEI`, `wIE`, `wII`: Synaptic weights
- `I_ext_E`, `I_ext_I`: External inputs
- `a_E`, `a_I`: Parameters for the activation function
- `theta_E`, `theta_I`: Parameters for the activation function
- `tau_E`, `tau_I`: Time constants

The function should also take in the `duration` of the simulation and the time step `dt`. It should return the membrane potential dynamics of the E and I populations over time.

The membrane potential dynamics are given by the equations:

\[ \frac{dE}{dt} = \frac{-E + F(w_{EE}E - w_{EI}I + I_{ext\_E}, a_E, \theta_E)}{\tau_E} \]
\[ \frac{dI}{dt} = \frac{-I + F(w_{IE}E - w_{II}I + I_{ext\_I}, a_I, \theta_I)}{\tau_I} \]

Where:

- \( F(x, a, \theta) = \frac{1}{1 + e^{-a(x-\theta)}} \)

The function should use a numerical integration method (such as Euler's method) to update the membrane potentials over time.
"""

import numpy as np

def F(x, a, theta):
    return 1 / (1 + np.exp(-a * (x - theta)))

def simulate_network(pars, duration, dt):
    wEE, wEI = pars['wEE'], pars['wEI']
    wIE, wII = pars['wIE'], pars['wII']
    I_ext_E, I_ext_I = pars['I_ext_E'], pars['I_ext_I']
    a_E, a_I = pars['a_E'], pars['a_I']
    theta_E, theta_I = pars['theta_E'], pars['theta_I']
    tau_E, tau_I = pars['tau_E'], pars['tau_I']

    num_steps = int(duration / dt)
    time = np.arange(0, duration, dt)
    E = np.zeros(num_steps)
    I = np.zeros(num_steps)

    for t in range(1, num_steps):
        dEdt = (-E[t-1] + F(wEE*E[t-1] - wEI*I[t-1] + I_ext_E, a_E, theta_E)) / tau_E
        dIdt = (-I[t-1] + F(wIE*E[t-1] - wII*I[t-1] + I_ext_I, a_I, theta_I)) / tau_I
        E[t] = E[t-1] + dt * dEdt
        I[t] = I[t-1] + dt * dIdt

    return time, E, I