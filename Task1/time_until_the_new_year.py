from datetime import date

current_date = date.today()
new_year = date(current_date.year + 1, 1, 1)

print(current_date)
print(new_year)
print(new_year - current_date)
