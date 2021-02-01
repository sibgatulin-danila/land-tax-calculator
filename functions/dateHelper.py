from datetime import datetime

def getOwnershipYears(dateStart, dateFinish):
    start = datetime.strptime(dateStart, "%Y-%m-%d")
    finish = datetime.strptime(dateFinish, "%Y-%m-%d")

    return finish.year - start.year


def isLowerThenHalfOfMonth(date):
    day = datetime.strptime(date, "%Y-%m-%d").day
    
    return day <= 15


def getMonthInQuarter(quarter, dateStart, dateFinish):
    result = 0
    lastMonthOfQuarter = 3
    firstMonthOfQuarter = 1

    startMonth = datetime.strptime(dateStart, "%Y-%m-%d").month
    finishMonth = datetime.strptime(dateFinish, "%Y-%m-%d").month

    if (quarter == 2):
        lastMonthOfQuarter = 6
        firstMonthOfQuarter = 4
    elif (quarter == 3): 
        lastMonthOfQuarter = 9
        firstMonthOfQuarter = 7
    elif (quarter == 4):
        lastMonthOfQuarter = 12
        firstMonthOfQuarter = 10

    for x in range(firstMonthOfQuarter, lastMonthOfQuarter + 1):
        if (x < startMonth or x > finishMonth):
            continue
        if (x == startMonth):
            result += int(isLowerThenHalfOfMonth(dateStart))
        elif (x == finishMonth):
            result += 0 if isLowerThenHalfOfMonth(dateFinish) else 1
        else:
            result += 1
    
    return result
