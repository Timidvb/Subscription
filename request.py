import requests

link = open("link.txt", "r")

link.readline().replace("\n", "")
r = requests.get(url)

print(url, r.text)

full_page = "%s"%(r.text)

with open('sub.html', 'w') as f:
    f.write(full_page)
