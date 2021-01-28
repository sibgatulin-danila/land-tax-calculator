
def getInputData():
    # Получение даты установки права собственности
    print('Введите дату установки права собственности')
    print('Дата формата YYYY-mm-dd: ')

    dateStart = input()


    # Получение даты прекращения права собственности
    print()
    print('Введите дату прекращения права собственности')
    print('Дата формата YYYY-mm-dd: ')

    dateFinish = input()


    # Получение кадастровой стоимости
    print()
    print('Введите кадастровую стоимость')
    print('Стоимость в рублях формата р*.кк: ')

    cadastralValue = round(float(input()), 2)


    # Получение назначения
    print()
    print('Введите назначение')
    print('1 - сельскохозяйственное')
    print('2 - жильщный фонд')
    print('3 - личное подсобное хозяйство')
    print('4 - для обеспечения обороны, безопасности и таможенных нужд')
    print('5 - прочее')
    print('назначение: ')

    target = int(input())


    # Площадь участка
    print()
    print('Введите площадь участка')
    print('Площадь участка в формате 1111.11, га: ')

    plotSize = round(float(input()), 2)


    # Доля владения
    print()
    print('Введите долю владения')
    print('Доля владения от 0 до 1:')

    partOfLand = round(float(input()), 3)


    # Коэффициент строительства
    print()
    print('Введите коэффициент строительства')
    print('Коэффициент от 0 до 1')

    buildingRate = round(float(input()), 2)


    # Считать ли льготы
    print()
    print('Льготная земля?')
    print('1 - Да, 0 - нет:')

    isExemption = bool(int(input()))


    return dateStart, dateFinish, cadastralValue, target, plotSize, partOfLand, buildingRate, isExemption 

def getInputDataTest():
    return '2020-11-20', '2021-11-20', 20000.10, 1, 700, 1, 1, 1