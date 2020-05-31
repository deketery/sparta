# 지니뮤직의 1~50위 곡을 스크래핑 해보세요.
#https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text,"html.parser")
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
#순위 / 곡 제목 / 가수이름
for song in songs:
    rank = song.select_one('td.number').text[:2].strip()
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank,title,"-",singer)
