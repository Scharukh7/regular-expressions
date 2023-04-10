import re

date_pattern = r'^\d{2}/\d{2}/\d{4}$'

dates = ['04/10/2023', '12/25/2022', '01/01/2021', '13/20/2020', '2020/12/25']

for date in dates:
    if re.match(date_pattern, date):
        print(f"{date} is a valid date")
    else:
        print(f"{date} is not a valid date")
