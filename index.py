from functions.getInputData import getInputData, getInputDataTest
from functions.getTaxValue import getTaxValue


# exit if file imported!
if (__name__ != '__main__'):
    print('The file can not be imported!')
    exit()

# dateStart, dateFinish, cadastralValue, target, partOfLand, buildingRate, isExemption = getInputData()
dateStart, dateFinish, cadastralValue, target, plotSize, partOfLand, buildingRate, isExemption = getInputDataTest()

tax = getTaxValue(target)
