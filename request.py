import requests

link = open("link.txt", "r")

url = link.readline().replace('\r','').replace('\n','').replace('\t','')
r = requests.get(url)

full_page = "%s"%(r.text)

with open('sub.html', 'w') as f:
    f.write(full_page)
