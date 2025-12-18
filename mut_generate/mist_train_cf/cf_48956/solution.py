"""
QUESTION:
Calculate the probability that Semir arrives at school punctually on any given day. Given probabilities are: 15% chance of being late with a big breakfast and 6% chance of being late with a light breakfast. Assume a 50% chance of having a light breakfast and a 50% chance of having a heavy breakfast.

Implement a function `calculate_prob` that takes the probabilities of having a light breakfast (`p_light_breakfast`), having a heavy breakfast (`p_heavy_breakfast`), being late with a light breakfast (`p_late_light`), and being late with a heavy breakfast (`p_late_heavy`) as parameters. The function should return the overall probability of Semir being on time. Use default values of 0.5 for `p_light_breakfast` and `p_heavy_breakfast`, and 0.06 for `p_late_light` and 0.15 for `p_late_heavy`.
"""

def calculate_prob(p_light_breakfast=0.5, p_heavy_breakfast=0.5, p_late_light=0.06, p_late_heavy=0.15):
  """
  Calculate the overall probability of Semir being on time.

  Parameters:
  p_light_breakfast (float): The probability of having a light breakfast. Defaults to 0.5.
  p_heavy_breakfast (float): The probability of having a heavy breakfast. Defaults to 0.5.
  p_late_light (float): The probability of being late with a light breakfast. Defaults to 0.06.
  p_late_heavy (float): The probability of being late with a heavy breakfast. Defaults to 0.15.

  Returns:
  float: The overall probability of Semir being on time.
  """
  p_ontime_light = 1 - p_late_light
  p_ontime_heavy = 1 - p_late_heavy

  p_ontime = p_light_breakfast * p_ontime_light + p_heavy_breakfast * p_ontime_heavy

  return p_ontime