days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total_sundays = 0
days_in_year = 0
for year in range(1901, 2001):
    for days in days_in_month:
        if days == 28 and year % 100 != 0 and year % 4 == 0:
            days += 1
        days_in_year += days
        if days_in_year % 7 == 0:
            total_sundays += 1

print(total_sundays)
