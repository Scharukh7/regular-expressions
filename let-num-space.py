import re
# [a-zA-Z\d ]{5,50} : Match any combination of uppercase and lowercase letters and digits between 5 and 50 times
# $                : End of string
''''''
regex = r'^[a-zA-Z\d ]{5,50}$'

# String to test against the regular expression
word = 'reGex 1s Fascinat1nG'

# Test the string against the regular expression using the re.match() function
if re.match(regex, word):
    print('Match found!')
else:
    print('Match not found.')