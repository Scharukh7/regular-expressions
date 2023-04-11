import re

# Regular expression that matches credit card numbers in the format "XXXX-XXXX-XXXX-XXXX",
# where "X" is a digit. The regular expression is broken down as follows:
# ^      : Start of string
# \d{4}  : Match four digits
# -      : Match a hyphen
# \d{4}  : Match four digits
# -      : Match a hyphen
# \d{4}  : Match four digits
# -      : Match a hyphen
# \d{4}  : Match four digits
# $      : End of string
regex = r'^\d{4}-\d{4}-\d{4}-\d{4}$'

# Credit card number to test against the regular expression
card_num = '1515-5959-7777-7979'

# Test the credit card number against the regular expression using the re.match() function
if re.match(regex, card_num):
    print('Match found!')
else:
    print('Match not found.')
