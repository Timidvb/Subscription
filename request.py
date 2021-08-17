import requests

link = open("link.txt", "r")

url = "https://pptp.cloud/sub/eff3ccea-d40c-4861-92b8-c0e635ea7b86.html"
r = requests.get(url)

print(url, r.text)

full_page = """
<html><head></head><body>%s</body></html>
"""%(r.text)

with open('sub.html', 'w') as f:
    f.write(full_page)
