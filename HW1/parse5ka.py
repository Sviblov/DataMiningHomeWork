import requests

url ='https://magnit.ru/promo/?geo=moskva'

response = requests.get(url)

with  open('5ka.html', 'w', engoding ='UTF-8') as file:
    file.write(response.text)