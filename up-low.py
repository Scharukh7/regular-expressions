import re
''''''
# ^                : Start of string
# (?=.*\d)         : Positive lookahead assertion to match at least one digit
# (?=.*[a-z])      : Positive lookahead assertion to match at least one lowercase letter
# (?=.*[A-Z])      : Positive lookahead assertion to match at least one uppercase letter
# [a-zA-Z\d]{8,20} : Match any combination of uppercase and lowercase letters and digits between 8 and 20 times
# $                : End of string
''''''
regex = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{5,50}$'

# String to test against the regular expression
word = 'reGex1sFascinat1nG'

# Test the string against the regular expression using the re.match() function
if re.match(regex, word):
    print('Match found!')
else:
    print('Match not found.')
