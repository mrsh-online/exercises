from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.bbc.com"
response = requests.get(url)

if response.status_code == 200:
    print('Page fetch successfully !')
else:
    print('an error happenned')

soup = BeautifulSoup(response.text, 'html.parser' )



headlines = soup.find_all("a")

news_data =[]


for headline in headlines:
    if headline.find('h2'):
        title = headline.get_text(strip=True)
        link = headline.get('href')
        if  not link.startswith('http'):
            link = f'https://bbc.com{link}'
        news_data.append({'title':title, 'link': link})

df = pd.DataFrame(news_data)
df.to_csv('bbc.csv', index=False)
print('Headlines save to csv')

