import requests

link = open("link.txt", "r")

url = link.readline()
r = requests.get(url)

print(url, r.text)

full_page = """
<html><head></head><body>%s</body></html>
"""%(r.text)

with open('sub.html', 'w') as f:
    f.write(full_page)
