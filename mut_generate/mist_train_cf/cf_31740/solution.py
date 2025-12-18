"""
QUESTION:
Implement a function `calculate_differences(baseAUCs, swapAUCs, svTypes)` that takes in three parameters:
- `baseAUCs`: A list of base AUC values for each svType.
- `swapAUCs`: A dictionary where the keys are swap folders and the values are lists of swap AUC values for each svType.
- `svTypes`: A list of svTypes.

The function should return a list containing the differences calculated for each svType. The difference for each svType is calculated by summing the difference between the swap AUC and base AUC for each swap folder, skipping cases where the swap AUC is 0.
"""

def calculate_differences(baseAUCs, swapAUCs, svTypes):
    allDifferences = []
    for svTypeInd in range(len(svTypes)):
        differenceFromBase = 0
        for swapFolder, aucs in swapAUCs.items():
            baseAUC = baseAUCs[svTypeInd]
            swapAUC = aucs[svTypeInd]
            if swapAUC == 0:
                continue
            differenceFromBase += (swapAUC - baseAUC)
        allDifferences.append(differenceFromBase)
    return allDifferences