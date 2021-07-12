# Implements a proleptic Gregorian calendar date as a Julian day number.
class Date:
    # Creates an object instance for the specified Gregorian date.
    def __init__(self, year, month, day):
        self._julianDay = 0
        assert self._isValidGregorian(year, month, day), \
            "Invalid Gregorian date."

        # The first line of the equation, T = (M - 14) / 12, has to be changed
        # since Python's implementation of integer division is not the same
        # as the mathematical definition.
        tmp = 0
        if month < 3:
            tmp -= 1
        self._julianDay = day - 32075 + \
                (1461 * (year + 4800 + tmp) // 4) + \
                (367 * (month - 2 - tmp * 12) // 12) - \
                (3 * ((year + 4900 + tmp) // 100) // 4)

    # Extracts the appropriate Gregorian date component.
    def year(self):
        return (self._toGregorian())[0] # returning y from (y, M, d)

    def month(self):
        return (self._toGregorian())[1] # returning M from (y, M, d)

    def day(self):
        return (self._toGregorian())[2] # returning d from (y, M, d)

    # Returns day of the week as an int between 0 (Mon) and 6(Sun).
    def dayOfWeek(self):
        year, month, day = self._toGregorian()
        if month < 3:
            month += 12
            year -= 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    # Returns the date as a string in Gregorian format.
    def __str__(self):
        year, month, day = self._toGregorian()
        return "%04d/%02d/%02d" % (year, month, day)

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    # The remaining methods are to be included at this point.
    # TODO : Returns the Gregorian month number of this date.
    def monthName(self):
        return self.month()

    # TODO : Returns the number of days as a positive integer
    # between this date and the otherDate
    def numDays(self, otherDate):
        pass

    # TODO : Determines if this date falls in a leap year and
    # Returns the appropriate boolean value.
    def isLeapYear(self):
        pass

    # TODO : Advances the date by the given number of days.
    # The date is incremented if days is positive and
    # decremented if the days is negative.
    # The date is capped to November 24, 4714 BC, if necessary.
    def advanceBy(self, days):
        pass

    # Returns the Gregorian date as a tuple: (year, month, day).
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return year, month, day

    # TODO : Determine if the three components
    # of the given Gregorian date are valid.
    def _isValidGregorian(self, year, month, day):
        return_code = True
        if year == None or month == None or day == None:
            return_code = False
        if month > 12 or day > 31:
            return_code = False
        if month < 0 or day < 0:
            return_code = False
        return return_code

firstDay = Date(2006, 9, 1)
print(firstDay)
