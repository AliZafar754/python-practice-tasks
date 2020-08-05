import requests
from bs4 import BeautifulSoup
import csv

mainContent = requests.get("https://www.nytimes.com/") 
print(mainContent.text)

soup = BeautifulSoup(mainContent.text,'lxml')

articlell = soup.find_all('h2', class_='css-1vvhd4r e1voiwgp0')
print(articlell.prettify())

article_list =[]
for item in articlell: 
   individualtitle = item.get_text() 
   article_list.append(individualtitle) 
print(article_list.prettify())

with open('pythonscraper.csv','w') as csvfile: 
     writer = csv.writer(csvfile)
     for item in article_list: 
        writer.writerow([item])