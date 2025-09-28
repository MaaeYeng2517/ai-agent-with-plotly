

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')

print(response.status_code)

print(response.content)


html_text = response.text
encoded_html = html_text.encode(html_text.status_code)
decoded_html = encoded_html.decode(html_text.encoding)

# Remove all the CRLF chars
while '\n' in decoded_html:
     decoded_html = decoded_html.replace('\n','')

# Remove all the extra spaces,
#   you could even replace with ''
while '  ' in decoded_html:
    decoded_html = decoded_html.replace('  ',' ')

# Remove tabs '\t', maybe not.
while '\t' in decoded_html:
    decoded_html = decoded_html.replace('\t','')

print(decoded_html)

soup = BeautifulSoup(html_text.content, 'html.parser')

print(soup.prettify())