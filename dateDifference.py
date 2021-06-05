def isLeapYear(year):
    "(year: int) => bool"
    # https://simple.wikipedia.org/wiki/Century_leap_year
    return year % 4 == 0 & (year % 400 == 0 | year % 100 != 0)

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
        if (0 < day <= daysInMonth(month, year)) & (0 < month <= 12):
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
    return daysFromEpoch(dateString2) - daysFromEpoch(dateString1)

if __name__ == "__main__":
    TEST_CASES = [
        {"arg1": "02/06/1983", "arg2": "22/06/1983", "expectedResult": 19+1},
        {"arg1": "04/07/1984", "arg2": "25/12/1984", "expectedResult": 173+1},
        {"arg1": "03/01/1989", "arg2": "03/08/1983", "expectedResult": -1979-1},
        {"arg1": "11/08/1990", "arg2": "11/08/1990", "expectedResult": "example of failing test"},
        {"arg1": "11/08/1990", "arg2": "11/08/1990", "expectedResult": 0},
        {"arg1": "11/08/1990", "arg2": "12/08/1990", "expectedResult": 1},
        {"arg1": "11/08/1990", "arg2": "10/08/1990", "expectedResult": -1},
        {"arg1": "00/01/1000", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "99/01/1000", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "-3/01/1000", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "01/00/1000", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "01/99/1000", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "01/-3/1000", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "11-11-1111", "arg2": "11/11/1111", "expectedResult": Exception},
        {"arg1": "abcdefg", "arg2": "11/11/1111", "expectedResult": Exception},
    ]

    def printPass(testCase):
        print(f'PASS:\t {testCase}')

    def printFail(testCase, result):
        print(f'\nFAIL:\t {testCase}\n')
        print(f'expected: {testCase["expectedResult"]}')
        print(f'received: {result}')
        print("\n")

    for testCase in TEST_CASES:
        try:
            result = daysBetween(testCase["arg1"], testCase["arg2"])
            if result == testCase["expectedResult"]:
                printPass(testCase)
            else:
                printFail(testCase, result)
        except Exception as e:
            if testCase["expectedResult"] == Exception:
               printPass(testCase) 
            else:
                printFail(testCase, Exception)