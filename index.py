from functions.getInputData import getInputData, getInputDataTest
from functions.getTaxValue import getTaxValue, calculateCadastralValueWithPrevileges
from functions.dateHelper import getMonthInQuarter


# exit if file imported!
if (__name__ != '__main__'):
    print('The file can not be imported!')
    exit()

# dateStart, dateFinish, cadastralValue, target, plotSize, partOfLand, buildingRate, isExemption = getInputData()
dateStart, dateFinish, cadastralValue, target, plotSize, partOfLand, buildingRate, isExemption = getInputDataTest()

tax = getTaxValue(target)

cadastralValueWithPriveleges = calculateCadastralValueWithPrevileges(cadastralValue, isExemption, plotSize)

firstQuarterMonths = getMonthInQuarter(1, dateStart, dateFinish)
secondQuarterMonths = getMonthInQuarter(2, dateStart, dateFinish)
thirdQuarterMonths = getMonthInQuarter(3, dateStart, dateFinish)
fourthQuarterMonths = getMonthInQuarter(4, dateStart, dateFinish)

firstTaxPayment = round(1/4 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * firstQuarterMonths, 2) 
secondTaxPayment = round(1/4 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * secondQuarterMonths, 2)
thirdTaxPayment = round(1/4 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * thirdQuarterMonths, 2)
fourthTaxPayment = round(1/4 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * fourthQuarterMonths, 2)

print(firstTaxPayment, secondTaxPayment, thirdTaxPayment, fourthTaxPayment)