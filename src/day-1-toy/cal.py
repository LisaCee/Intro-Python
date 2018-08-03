# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
#
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.

import sys
import calendar
import datetime

# month = int(input("Enter a month 1 - 12: "))
# year = int(input("Enter a 4 digit year: "))

month = sys.argv[1]
year = sys.argv[2]

# if month == None:
#     month = 8
# if year == None:
#     year = 2018    

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(int(year), int(month))
print(str)

