def isLeapYear(year):
    "(year: int) => bool"
    # https://simple.wikipedia.org/wiki/Century_leap_year
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

def daysInMonth(month, year):
    "(month: int, year: int) => int"
    daysInFeb = 29 if isLeapYear(year) else 28
    return [31, daysInFeb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1]

def parseDateString(dateString):
    "(dateString: any) => {day: int, month: int, year: int}"
    ERROR_MESSAGE = "Invalid dateString: expected 'dd/mm/yyyy'"
    try:
        dayMonthYear = dateString.split("/")
        day = int(dayMonthYear[0])
        month = int(dayMonthYear[1])
        year = int(dayMonthYear[2])
        if (0 < day <= daysInMonth(month, year)) and (0 < month <= 12):
            return {
                "day": day,
                "month": month,
                "year": year,
            }
        else:
            raise ValueError(ERROR_MESSAGE)
    except Exception:
        raise ValueError(ERROR_MESSAGE)

def daysFromEpoch(dateString):
    "(dateString: 'dd/mm/yyyy') => int"
    date = parseDateString(dateString)
    totalDays = date["day"] - 1
    for year in range(date["year"] + 1):
        if year == date["year"]:
            for month in range(1, date["month"] + 1):
                if month != date["month"]:
                    totalDays += daysInMonth(month, year)
        else:
            for month in range(1, 12 + 1):
                totalDays += daysInMonth(month, year)
    return totalDays

def daysBetween(dateString1, dateString2):
    "(dateString1: 'dd/mm/yyyy', dateString2: 'dd/mm/yyyy) => int"
    delta = daysFromEpoch(dateString2) - daysFromEpoch(dateString1)
    # The first and the last day are considered partial days and never counted
    return delta - 1 if delta > 0 else delta + 1 if delta < 0 else delta
