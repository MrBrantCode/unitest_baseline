"""
QUESTION:
Write a function to determine if a given CAPTCHA solution is secure, with a score indicating the probability of a user being a bot.
"""

def is_captcha_secure(score):
    """
    Determine if a given CAPTCHA solution is secure based on the score.

    Args:
        score (float): The score indicating the probability of a user being a bot.

    Returns:
        bool: True if the CAPTCHA solution is secure, False otherwise.
    """
    # Google's reCaptcha v3 uses a score of 0.5 as the threshold
    # You can adjust this value according to your specific requirements
    threshold = 0.5
    return score >= threshold