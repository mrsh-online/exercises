import nltk
from bs4 import BeautifulSoup
import pandas as pd
import requests
from nltk.sentiment import SentimentIntensityAnalyzer

# for the nltk
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# we gonna fetch the title from bbc
url= 'https://bbc.com'

response = requests.get(url)

if response.status_code == 200:
    print('page fetch succesfully')
else:
    print('an error happened !')


soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('a')

news_data = []

for headline in headlines:
    if headline.find('h2'):
        title = headline.get_text(strip=True)
        link = headline.get('href')
        sentiment = sia.polarity_scores(title)
        if  not link.startswith('http'):
            link = f'https://bbc.com{link}'
        
        news_data.append({'title':title, 'link': link, 'sentiment' : sentiment})

df = pd.DataFrame(news_data)
df.to_csv('bbc.csv', index=False)
print('Headlines save to csv')


    

#
# sentiment = sia.polarity_scores("Python is the best programming language")

