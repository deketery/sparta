import requests 
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


_url = 'https://motioneffect.tistory.com/'
i=50
while i >=1 :
    total_url =  _url + str(i)
    data = requests.get(total_url ,headers=headers)
    soup = BeautifulSoup(data.text,"html.parser")
    docs = soup.select('#content > div > div > div > div > div.titleWrap.jumbotron > h2 > a')
    i = i-1
    if docs : 
        for doc in docs:
            print(doc.get_text(),total_url)
