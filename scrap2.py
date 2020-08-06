import requests
from bs4 import BeautifulSoup


recurship = requests.get("http://recurship.com/") 
print(recurship.text)

soup = BeautifulSoup(recurship.text,'lxml')

for link in soup.findAll('a', attrs={'href': requests.compile("^http://")}):
    print(link.get('href'))


for title in soup.find_all('a', class_='entry-title'):
	print(title.get_text())

images = soup.findAll('img')
for image in images:
    print(image['http://54.179.166.158/wp-content/uploads/2018/07/acuqui3-300x153.png'])



with open('E/:read.txt', 'w') as f:
   for line in soup.prettify('utf-8', 'minimal'):
      f.write(str(line))    	
