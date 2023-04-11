import re

regex = r'^https?://(?:www\.)?[\w-]+\.\w{2,}(?:/\S*)?$'
url = 'https://example.com/path/to/page.html'

if re.match(regex, url):
    print('Match found!')
else:
    print('Match not found.')