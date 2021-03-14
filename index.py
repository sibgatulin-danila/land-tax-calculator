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

print()
print("Месяцев владения:")
print(firstQuarterMonths,
secondQuarterMonths,
thirdQuarterMonths,
fourthQuarterMonths)

firstTaxPayment = round(1/3 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * firstQuarterMonths * 0.25, 2) 
secondTaxPayment = round(1/3 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * secondQuarterMonths * 0.25, 2)
thirdTaxPayment = round(1/3 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * thirdQuarterMonths * 0.25, 2)
fourthTaxPayment = round(1/3 * tax / 100 * partOfLand * buildingRate * cadastralValueWithPriveleges * fourthQuarterMonths * 0.25, 2)

print("Авансовые платежи за каждый квартал:")
print(firstTaxPayment, secondTaxPayment, thirdTaxPayment, fourthTaxPayment)

print("Сумма авансовых платежей:")
print(round(firstTaxPayment + secondTaxPayment + thirdTaxPayment + fourthTaxPayment, 2))
