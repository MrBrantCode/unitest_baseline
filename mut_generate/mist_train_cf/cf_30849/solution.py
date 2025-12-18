"""
QUESTION:
Implement a function named `get_cavg` that computes the Cavg (average cost) for a given set of language recognition pairs. The Cavg is calculated using several threshold bins within a specified score range.

The function should take the following parameters: `pairs` (a list of language recognition pairs where each pair contains the probability of correctly recognizing the language and the language label), `lang_num` (the number of languages being recognized), `min_score` (the minimum score for language recognition), `max_score` (the maximum score for language recognition), `bins` (the number of threshold bins to use within the score range, default value is 20), and `p_target` (the target probability for correctly recognizing the language, default value is 0.5).

The function should calculate the Cavg for each language within the specified threshold bins using the formula: Cavg = p_target * p_miss + sum(p_nontarget * p_fa), where p_miss is the probability of missing the target language, p_nontarget is the probability of recognizing a non-target language, and p_fa is the probability of false acceptance. The results should be stored in a list.
"""

def get_cavg(pairs, lang_num, min_score, max_score, bins=20, p_target=0.5):
    ''' Compute Cavg, using several threshold bins in [min_score, max_score].
    '''
    cavgs = [0.0] * (bins + 1)
    precision = (max_score - min_score) / bins
    for section in range(bins + 1):
        threshold = min_score + section * precision
        # Cavg for each lang: p_target * p_miss + sum(p_nontarget*p_fa)
        target_cavg = [0.0] * lang_num
        for lang in range(lang_num):
            p_miss = sum(p for p, l in pairs if l == lang and p < threshold) / sum(1 for p, l in pairs if l == lang)
            p_fa = sum(1 for p, l in pairs if l != lang and p >= threshold) / sum(1 for p, l in pairs if l != lang)
            p_nontarget = 1 - p_miss
            target_cavg[lang] = p_target * p_miss + p_nontarget * p_fa
        cavgs[section] = sum(target_cavg) / lang_num
    return cavgs