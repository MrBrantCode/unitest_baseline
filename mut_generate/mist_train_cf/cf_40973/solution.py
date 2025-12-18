"""
QUESTION:
Create a function `calculate_forces` that takes the following parameters: `Rho`, `Thickness`, `Ori_1`, `Ori_2`, `Chord`, `SectionLength`, `Vmin`, `Vmax`, `Vstep`, `AeroFlag`, and `GravFlag`. The function should return a dictionary containing the calculated lift and drag forces for each velocity within the range from `Vmin` to `Vmax` with a step of `Vstep`. The calculation should be based on aerodynamic principles and include factors for aerodynamic and gravitational effects as indicated by `AeroFlag` and `GravFlag`, respectively.
"""

def calculate_forces(Rho, Thickness, Ori_1, Ori_2, Chord, SectionLength, Vmin, Vmax, Vstep, AeroFlag, GravFlag):
    forces = {}
    for velocity in range(Vmin, Vmax + 1, Vstep):
        lift_force = 0.5 * Rho * (velocity ** 2) * Chord * SectionLength * (math.sin(Ori_2) - math.sin(Ori_1))
        drag_force = 0.5 * Rho * (velocity ** 2) * Chord * SectionLength * (math.cos(Ori_2) - math.cos(Ori_1))

        if AeroFlag == 1:
            lift_force *= 1.2  
            drag_force *= 1.1  

        if GravFlag == 1:
            lift_force -= Rho * SectionLength * Chord * 9.81  

        forces[velocity] = {'lift': lift_force, 'drag': drag_force}

    return forces