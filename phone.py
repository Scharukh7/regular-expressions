import re

regex = r'^\(\d{3}\) \d{3}-\d{4}$'
phone_number = '(122) 007-7777'

if re.match(regex, phone_number):
    print('Match found!')
else:
    print('Match not found.')