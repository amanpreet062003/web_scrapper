import requests
from bs4 import BeautifulSoup

URL = "https://shop.bbc.com/collections/apparel"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
content_title = soup.body.find_all(attrs={'class':"bc-sf-filter-product-item-title"})
content_price = soup.body.find_all(attrs={'class':"bc-sf-filter-product-item-price"})

for title, price in zip(content_title, content_price):
    price_value = price.text.strip().split()[0]
    print(f"The title of the product: {title.text.strip()}, The price of the product: {price_value}")
