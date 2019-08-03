###########################################################################  3번 문제
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def testPalindrome(caseStr):
    if str(caseStr) == (str(caseStr))[::-1]:
        return 'YES'
    else:
        return 'NO'


tc = 3
caseStr = []
for i in range(1, tc + 1):
    caseStr.append(input())
for i in range(0, tc):
    print(testPalindrome(caseStr[i]))
