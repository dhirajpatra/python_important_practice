import sys
sys.path.append('/usr/bin/python')
import html2text
import requests

url = "https://dotai.tech"
res = requests.get(url)
html = res.text
text = html2text.html2text(html)
print(text)