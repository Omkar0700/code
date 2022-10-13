import requests
from bs4 import BeautifulSoup
import json


cmc = requests.get('https://coinmarketcap.com')
soup = BeautifulSoup(cmc.content, 'html.parser')
data = soup.find('script', id='__NEXT_DATA__', type='application/json')
coin_data = json.loads(data.contents[0])
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
