# Function for determining if year is a leap year
def is_leap_year (yr):
    if yr % 4 == 0: 
        if yr % 100 == 0:
            if yr % 400 == 0:
                return (True)
            else:
                return (False)
        else:
            return (True)
    else:
        return (False)

# Function for determining how many days in a month
def days_in_month (year, month):
    if month == 1 or month == 3 or month == 5 or  month == 7 or month == 8  or month == 10 or month == 12:
        return (31)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return (30)
    elif is_leap_year(year):
        return (29)
    else:
        return (28)
    