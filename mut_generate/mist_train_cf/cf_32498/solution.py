"""
QUESTION:
Implement the `throttle_controller_step` function, which calculates and returns the throttle and brake commands for an autonomous vehicle based on the provided inputs. The function takes the cross-track error (`cte`) and sample time as inputs. The throttle and brake commands are determined based on the vehicle's linear velocity, current velocity, deceleration limit, vehicle mass, and wheel radius. The function should follow the specified rules:
- If the linear velocity is 0 and the current velocity is less than 0.1, set the throttle to 0 and the brake to 400.
- If the throttle is less than 0.1 and the cross-track error is negative, set the throttle to 0 and calculate the brake based on the maximum value between the cross-track error and the deceleration limit, multiplied by the vehicle's mass and wheel radius. 

The function has access to the following variables and constants: `linear_velocity`, `current_velocity`, `self.decel_limit`, `self.vehicle_mass`, and `self.wheel_radius`.
"""

def throttle_controller_step(cte, sample_time, linear_velocity, current_velocity, decel_limit, vehicle_mass, wheel_radius):
    throttle = 0
    brake = 0
    
    if linear_velocity == 0 and current_velocity < 0.1:
        throttle = 0
        brake = 400
    elif throttle < 0.1 and cte < 0:
        throttle = 0
        decel = max(cte, decel_limit)
        brake = abs(decel) * vehicle_mass * wheel_radius
    
    return throttle, brake