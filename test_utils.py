def printPass(testCase):
    print(f'PASS:\t {testCase}')

def printFail(testCase, result):
    print(f'\nFAIL:\t {testCase}\n')
    print(f'expected: {testCase["expectedResult"]}')
    print(f'received: {result}')
    print("\n")

def runTests(testCases, testFunction):
    print(f'\nRunning tests for function "{testFunction.__name__}":\n')
    for testCase in testCases:
        try:
            result = testFunction(testCase["arg1"], testCase["arg2"])
            if result == testCase["expectedResult"]:
                printPass(testCase)
            else:
                printFail(testCase, result)
        except Exception as e:
            if testCase["expectedResult"] == Exception:
                printPass(testCase) 
            else:
                printFail(testCase, e)
