from test_utils import runTests
from date_utils import daysBetween

TEST_CASES = [
    {"arg1": "02/06/1983", "arg2": "22/06/1983", "expectedResult": 20},
    {"arg1": "04/07/1984", "arg2": "25/12/1984", "expectedResult": 174},
    {"arg1": "03/01/1989", "arg2": "03/08/1983", "expectedResult": -1980},
    {"arg1": "11/08/1990", "arg2": "11/08/1990", "expectedResult": 0},
    {"arg1": "11/08/1990", "arg2": "12/08/1990", "expectedResult": 1},
    {"arg1": "11/08/1990", "arg2": "10/08/1990", "expectedResult": -1},
    {"arg1": "11/08/1990", "arg2": "10/08/1990", "expectedResult": -1},
    {"arg1": "XXXXXXXXXX", "arg2": "11/08/1990", "expectedResult": "example of failing test - unexpected error"},
    {"arg1": "11/08/1990", "arg2": "11/08/1990", "expectedResult": "example of failing test - bad result"},
    {"arg1": "00/01/1000", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "99/01/1000", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "-3/01/1000", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "01/00/1000", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "01/99/1000", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "01/-3/1000", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "11-11-1111", "arg2": "11/11/1111", "expectedResult": Exception},
    {"arg1": "abcdefg", "arg2": "11/11/1111", "expectedResult": Exception},
]

if __name__ == "__main__":
    runTests(TEST_CASES, daysBetween)
