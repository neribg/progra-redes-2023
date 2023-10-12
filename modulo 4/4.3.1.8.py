'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 4.3.1.8
'''
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    days_by_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year < 1 or month < 1 or month > 12:
        return None
    if is_year_leap(year) and month == 2:
        return 29
    else:
        return days_by_month[month]

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return None

    days = day

    for m in range(1, month):
        month_days = days_in_month(year, m)
        if month_days is None:
            return None
        days += month_days

    if day > days_in_month(year, month):
        return None

    return days

print(day_of_year(2000, 12, 31))
