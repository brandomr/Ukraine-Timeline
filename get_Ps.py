import urllib.request
from bs4 import BeautifulSoup

url = "http://www.bbc.com/news/world-middle-east-26248275"

soup = BeautifulSoup(urllib.request.urlopen(url))

allpars = soup.find_all('p')

for child in allpars.children:
    print(child)



f = open('ctp_output.txt', 'w')


for tag in soup.find_all('p'):
    for i in tag:
        date = str(tag.strong.text.encode('utf-8'))
    text= str(tag.text.encode('utf-8'))
    write_to_file = "Date: " + date + ", " + "Text: " + text + '\n'
    f.write(write_to_file)
