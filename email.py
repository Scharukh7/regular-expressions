import re

email_pattern = r'^[\w\.-]+@[a-zA-Z\.]+\.[a-zA-Z]{2,}$'

emails = ['tomholland@gmail.com', 'cillian_murphy23@live.com', 'christain123-@uk', 'keanue-reeves@gmail.com', 'bale@example.']

for email in emails:
    if re.match(email_pattern, email):
        print(f"{email} is a valid email address")
    else:
        print(f"{email} is not a valid email address")
