"""
QUESTION:
Écrivez une fonction Python `calculer_moyennes_salaire` qui prend en entrée deux listes de salaires `salaire_bb` et `salaire_ja` représentant les salaires moyens annuels des baby-boomers et des jeunes actifs pour les années 2000 à 2021. La fonction doit retourner les moyennes de salaire pour les deux groupes.

Exemple d'entrée :

`annees = [2000, 2005, 2010, 2015, 2020, 2021]`
`salaire_bb = [45000, 50000, 55000, 60000, 65000, 67000]`
`salaire_ja = [25000, 30000, 35000, 40000, 45000, 47000]`
"""

def calculer_moyennes_salaire(salaire_bb, salaire_ja):
    """
    Calcul les moyennes de salaire pour les baby-boomers et les jeunes actifs.

    Args:
        salaire_bb (list): Liste des salaires moyens annuels des baby-boomers.
        salaire_ja (list): Liste des salaires moyens annuels des jeunes actifs.

    Returns:
        tuple: Une tuple contenant les moyennes de salaire pour les baby-boomers et les jeunes actifs.
    """
    moyenne_bb = sum(salaire_bb) / len(salaire_bb)
    moyenne_ja = sum(salaire_ja) / len(salaire_ja)
    return moyenne_bb, moyenne_ja