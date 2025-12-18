"""
QUESTION:
Implement the Hodgkin-Huxley model using the provided constants and simulate the membrane potential over time in response to a step current input. The model should be governed by the following set of differential equations:

\[C_m \frac{dV}{dt} = I - \bar{g}_{Na}m^3h(V - E_{Na}) - \bar{g}_Kn^4(V - E_K) - \bar{g}_{leak}(V - E_{leak})\]

\[\frac{dx}{dt} = \alpha_x(V)(1 - x) - \beta_x(V)x\]

The function should take the following parameters: 
- Constants: C_m, G_Na, G_K, G_leak, E_Na, E_K, E_leak
- Simulation parameters: dt, t_max, I
- Initial conditions: V_0, m_0, h_0, n_0

The function should return the membrane potential V over time.
"""

def hodgkin_huxley_model(G_Na, G_K, G_leak, E_Na, E_K, E_leak, C_m, dt, t_max, I, V_0, m_0, h_0, n_0):
    """
    Simulate the Hodgkin-Huxley model to calculate the membrane potential over time.

    Parameters:
    G_Na (float): Maximal conductance (Na+) ms/cm2
    G_K (float): Maximal conductance (K+) ms/cm2
    G_leak (float): Maximal conductance (leak) ms/cm2
    E_Na (float): Nernst potential (Na+) mV
    E_K (float): Nernst potential (K+) mV
    E_leak (float): Nernst potential (leak) mV
    C_m (float): Cell capacitance uF/cm2
    dt (float): Time step (ms)
    t_max (float): Maximum simulation time (ms)
    I (numpy array): External current input
    V_0 (float): Initial membrane potential (mV)
    m_0 (float): Initial Na+ activation gating variable
    h_0 (float): Initial Na+ inactivation gating variable
    n_0 (float): Initial K+ activation gating variable

    Returns:
    V (numpy array): Membrane potential over time (mV)
    """

    num_steps = int(t_max / dt)
    V = np.zeros(num_steps)
    m = np.zeros(num_steps)
    h = np.zeros(num_steps)
    n = np.zeros(num_steps)

    V[0] = V_0
    m[0] = m_0
    h[0] = h_0
    n[0] = n_0

    for i in range(1, num_steps):
        alpha_m = 0.1 * (V[i - 1] + 40) / (1 - np.exp(-(V[i - 1] + 40) / 10))
        beta_m = 4 * np.exp(-(V[i - 1] + 65) / 18)
        alpha_h = 0.07 * np.exp(-(V[i - 1] + 65) / 20)
        beta_h = 1 / (1 + np.exp(-(V[i - 1] + 35) / 10))
        alpha_n = 0.01 * (V[i - 1] + 55) / (1 - np.exp(-(V[i - 1] + 55) / 10))
        beta_n = 0.125 * np.exp(-(V[i - 1] + 65) / 80)

        m[i] = m[i - 1] + dt * (alpha_m * (1 - m[i - 1]) - beta_m * m[i - 1])
        h[i] = h[i - 1] + dt * (alpha_h * (1 - h[i - 1]) - beta_h * h[i - 1])
        n[i] = n[i - 1] + dt * (alpha_n * (1 - n[i - 1]) - beta_n * n[i - 1])

        I_Na = G_Na * m[i] ** 3 * h[i] * (V[i - 1] - E_Na)
        I_K = G_K * n[i] ** 4 * (V[i - 1] - E_K)
        I_leak = G_leak * (V[i - 1] - E_leak)
        dVdt = (1 / C_m) * (I[i - 1] - I_Na - I_K - I_leak)
        V[i] = V[i - 1] + dt * dVdt

    return V