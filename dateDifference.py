def isLeapYear(year):
    "(year: int) => bool"
    # https://simple.wikipedia.org/wiki/Century_leap_year
    return year % 4 == 0 & (year % 400 == 0 | year % 100 != 0)

def daysInMonth(month, year):
    "(month: int, year: int) => int"
    daysInFeb = 29 if isLeapYear(year) else 28
    return [31, daysInFeb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1]

def isValidDateString(date):
    "(date: any) => bool"
    if (type(date) != str or len(date.split("/")) != 3):
        return False
    dayMonthYear = date.split("/")
    day = dayMonthYear[0]
    month = dayMonthYear[1]
    year = dayMonthYear[2]
    yearIsValid = type(year) == int
    monthIsValid = type(month) == int & 0 <= month <= 12
    dayIsValid = type(month) == int & 0 <= day <= daysInMonth(month, year)
    return yearIsValid & monthIsValid & dayIsValid

def parseDateString(dateString):
    "(dateString: any) => {day: int, month: int, year: int}"
    if not isValidDateString(dateString):
        raise ValueError("Invalid dateString: expected 'dd/mm/yyyy'")
    dayMonthYear = dateString.split("/")
    return {
        "day": int(dayMonthYear[0]),
        "month": int(dayMonthYear[1]),
        "year": int(dayMonthYear[2]),
    }

def daysFromEpoch(dateString):
    date = parseDateString(dateString)
    totalDays = date["day"] - 1
    for year in range(date["year"] + 1):
        if year == date["year"]:
            for month in range(1, date["month"] + 1):
                if month != date["month"]:
                    totalDays += daysInMonth(month, year)
                    # print(f'Y: {year},\tM: {month},\tD: {daysInMonth(month, year)},\t D_total: {totalDays}')
        else:
            for month in range(1, 12 + 1):
                totalDays += daysInMonth(month, year)
                # print(f'Y: {year},\tM: {month},\tD: {daysInMonth(month, year)},\t D_total: {totalDays}')
    return totalDays

def daysBetween(dateString1, dateString2):
    return daysFromEpoch(dateString2) - daysFromEpoch(dateString1)
