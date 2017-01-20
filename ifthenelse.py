# n the Gregorian calendar three criteria must be taken into account to identify leap years:
#
# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source
#
#

import re

shape = input().split()

N = int(shape[0])
M = int(shape[1])

rows = list()

for row in range(N):
    rows.append(list(input()))

mystr = ""
for col in range(M):
    for row in range(N):
        mystr += rows[row][col]

p = re.compile('([A-Za-z0-9]+)([^A-Za-z0-9]+)([A-Za-z0-9])')

print(p.sub('\g<1> \g<3>', mystr))
# final_str = ""
# for i in range(len(mystr)):
#
#
# print(final_str)
