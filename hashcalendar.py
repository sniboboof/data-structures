
class make_month():
    def __init__(self, year, month):
        #i used the gregorian calendar from timeanddate.com for initial values
        #oddly enough its year 1 seems off by 5 days and I can't figure out why
        if year < 1:
            #Anno Domini only
            raise KeyError

        monthlens = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

        leapYear = False
        #is this a leap year?
        if year % 400 == 0:
            leapYear = True
        elif year % 100 != 0 and year % 4 == 0:
            leapYear = True

        #need to set the length of the month
        #and the starting day of the week
        self.len = monthlens[month-1]
        if month == 2:
            if leapYear:
                self.len += 1

        self.start = 0  # time started on a sunday
                        # well, year one did
        yearspassed = year-1
        self.start = (self.start + 365*yearspassed) % 7
        leapdays = yearspassed//4 - yearspassed//100 + yearspassed//400
        self.start = (self.start+leapdays) % 7

        dayspassed = sum(monthlens[:month-1])
        if month > 2 and leapYear:
            dayspassed += 1

        self.start = (self.start+dayspassed) % 7

    def __len__(self):
        return self.len

    def __call__(self, day):
        weekdays = ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', )
        if 0 < day <= len(self):
            return weekdays[(self.start+day-1) % 7]
        else:
            raise KeyError
