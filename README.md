# date-calculator

Calculate the number of full days elapsed in between two events. The day of each event is considered a partial day and not counted.

## CLI

quickstart

```
$ python3 days_between.py 01/02/1990 01/03/1990
27
```

help

```
$ python3 days_between.py --help
usage: calculate the number of full days elapsed in between two dates [-h] dateString1 dateString2

positional arguments:
  dateString1  'dd/mm/yyyy (string representing a date)
  dateString2  'dd/mm/yyyy (string representing a date)

optional arguments:
  -h, --help   show this help message and exit
```

leap years

```
$ python3 days_between.py 01/01/2000 01/01/2001
365
```

but not century years

```
$ python3 days_between.py 01/01/1700 01/01/1701
364
$ python3 days_between.py 01/01/1800 01/01/1801
364
$ python3 days_between.py 01/01/1900 01/01/1901
364
```

## Testing

```
$ python3 test_runner.py

Running tests for function "daysBetween":

PASS:    {'arg1': '02/06/1983', 'arg2': '22/06/1983', 'expectedResult': 19}
PASS:    {'arg1': '04/07/1984', 'arg2': '25/12/1984', 'expectedResult': 173}
PASS:    {'arg1': '03/01/1989', 'arg2': '03/08/1983', 'expectedResult': -1979}
PASS:    {'arg1': '11/08/1990', 'arg2': '12/08/1990', 'expectedResult': 0}
PASS:    {'arg1': '11/08/1990', 'arg2': '10/08/1990', 'expectedResult': 0}
PASS:    {'arg1': '11/08/1990', 'arg2': '13/08/1990', 'expectedResult': 1}
PASS:    {'arg1': '11/08/1990', 'arg2': '09/08/1990', 'expectedResult': -1}
PASS:    {'arg1': '11/08/1990', 'arg2': '11/08/1990', 'expectedResult': 0}

FAIL:    {'arg1': 'XXXXXXXXXX', 'arg2': '11/08/1990', 'expectedResult': 'example of failing test - unexpected error'}

expected: example of failing test - unexpected error
received: Invalid dateString: expected 'dd/mm/yyyy'



FAIL:    {'arg1': '11/08/1990', 'arg2': '11/08/1990', 'expectedResult': 'example of failing test - bad result'}

expected: example of failing test - bad result
received: 0


PASS:    {'arg1': '00/01/1000', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': '99/01/1000', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': '-3/01/1000', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': '01/00/1000', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': '01/99/1000', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': '01/-3/1000', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': '11-11-1111', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
PASS:    {'arg1': 'abcdefg', 'arg2': '11/11/1111', 'expectedResult': <class 'Exception'>}
```
