
def getTaxValue(target):
    if (
        target == 1
        or target == 2
        or target == 3
        or target == 4
    ):
        return 0.3
    else:
        return 1.5


def calculateCadastralValueWithPrevileges(cadastralValue, isExemption, plotSize):
    if (isExemption == False):
        return cadastralValue / 1200
    
    if (plotSize < 600):
        return 0

    return cadastralValue * (plotSize - 600) / plotSize