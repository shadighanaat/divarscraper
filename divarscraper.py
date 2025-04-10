from bidi.algorithm import get_display
import arabic_reshaper
def convert(text):

    reshaped_text=arabic_reshaper.reshape(text)
    converted=get_display(reshaped_text)
    return converted
print(convert("خرید و فروش و قیمت خودرو پژو 206 در استان اصفهان مدل ۱۳۹۵ تا ۱۴۰۲"))

import requests
from bs4 import BeautifulSoup
response=requests.get('https://divar.ir/s/isfahan-province/car/peugeot/206?production-year=1395-1402')
print(response)
soup=BeautifulSoup(response.text,'html.parser')
titles=soup.find_all('div',attrs={'id':'app'})
if (len(titles)==0):
    print('not found')
else:
    items= titles[0].find_all("a")
    for item in items:
         
   
         print(convert(item.getText()))

        

