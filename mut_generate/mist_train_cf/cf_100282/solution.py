"""
QUESTION:
Créez une fonction en Python qui calcule la moyenne des salaires des baby-boomers et des jeunes actifs pour les années 2000 à 2021. La fonction doit prendre deux listes de salaires en entrée, une pour les baby-boomers et une pour les jeunes actifs, et retourner les moyennes respectives. Utilisez les listes de salaires suivantes : 

salaire_bb = [45000, 50000, 55000, 60000, 65000, 67000]
salaire_ja = [25000, 30000, 35000, 40000, 45000, 47000]
"""

def moyenne_salaire(salaire_bb, salaire_ja):
    moyenne_bb = sum(salaire_bb)/len(salaire_bb)
    moyenne_ja = sum(salaire_ja)/len(salaire_ja)
    return moyenne_bb, moyenne_ja