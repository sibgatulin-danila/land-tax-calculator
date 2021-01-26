from functions.getInputData import getInputData, getInputDataTest
from functions.getTaxValue import getTaxValue


# exit if file imported!
if (__name__ != '__main__'):
    print('The file can not be imported!')
    exit()

# dateStart, dateFinish, cadastralValue, target = getInputData()
dateStart, dateFinish, cadastralValue, target, plotSize = getInputDataTest()

tax = getTaxValue(target)

