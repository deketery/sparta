import json
import os
import sys
import urllib.request
import pprint
import re
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime, timedelta, timezone
from time import time, gmtime
import requests
import signaturehelper

from bs4 import BeautifulSoup

from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.keyword


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def keyword_amount():
    keyword = request.args.get('keyword_give')  # 키워드 입력받아오기

    keyword_amount_info = get_keyword_search_count(keyword)  # 검색량
    docs_amount_info = docs_count(keyword)  # 문서량
    blog_PC10_info = blog_pc_10(keyword)  # pC상위 10개
    datalab_info = datalab_api(keyword)
    taporder_info = taporder_api(keyword)
    return jsonify({
        'result': 'success',
        'keyword_amount': keyword_amount_info,
        'docs_amount': docs_amount_info,
        'blog_pc_10': blog_PC10_info,
        'datalab_30': datalab_info,
        'tap_order':taporder_info
    })

##################################################


def get_header(method, uri, api_key, secret_key, customer_id):
    # 검색광고api 검색량 조회세트1
    API_KEY = '0100000000f68beb16c9173bdd48d1357128e81935b1c17a82686a9739f1547b69b68d8a07'
    SECRET_KEY = 'AQAAAAD2i+sWyRc73UjRNXEo6Bk1AXyUkvf32XciCkWSmwvxNQ=='
    CUSTOMER_ID = '1930049'

    timestamp = str(round(time() * 1000))
    signature = signaturehelper.Signature.generate(timestamp, method, uri,
                                                   SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8',
            'X-Timestamp': timestamp,
            'X-API-KEY': API_KEY,
            'X-Customer': str(CUSTOMER_ID),
            'X-Signature': signature}


def get_keyword_search_count(keyword):
    # 검색광고api 검색량 조회세트2
    striped_keyword = keyword.replace(" ", "")
    BASE_URL = 'https://api.naver.com'
    API_KEY = '0100000000f68beb16c9173bdd48d1357128e81935b1c17a82686a9739f1547b69b68d8a07'
    SECRET_KEY = 'AQAAAAD2i+sWyRc73UjRNXEo6Bk1AXyUkvf32XciCkWSmwvxNQ=='
    CUSTOMER_ID = '1930049'

    uri = '/keywordstool'
    method = 'GET'
    params = {'hintKeywords': striped_keyword}
    r = requests.get(BASE_URL + uri,
                     params=params,
                     headers=get_header(
                         method, uri,
                         API_KEY, SECRET_KEY,
                         CUSTOMER_ID)
                     )

    # pprint.pprint("response status_code = {}".format(r.status_code))
    keyword_search_amount = (r.json()['keywordList'][0])
    return keyword_search_amount


def docs_count(keyword):
    # 네이버 검색 api_2 문서량
    client_id = "ypBiU96rLqtStddxGQTZ"
    client_secret = "RqqvUoPprT"
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        dicts = json.loads(response_body.decode('utf-8'))
        total_doc = {"totaldoc": dicts["total"]}
    return total_doc


def blog_pc_10(keyword):
    # 네이버 검색 api_2 블로그 정보.
    client_id = "ypBiU96rLqtStddxGQTZ"
    client_secret = "RqqvUoPprT"
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        dicts = json.loads(response_body.decode('utf-8'))
        blog_list = dicts["items"]
        blog_infolist = []
        for blog in blog_list:

            link_data = blog["link"]

            title_data = blog["title"]
            title_data = re.sub('<.+?>', '', title_data, 0).strip()

            date_data = blog["postdate"]
            date = datetime.strptime(date_data, '%Y%m%d').strftime('%Y-%m-%d')
            blog_info = {"블로그링크": link_data,
                         "블로그제목": title_data,
                         "발행날짜": date}
            blog_infolist.append(blog_info)
        return blog_infolist
    else:
        return "Error Code:" + rescode


def datalab_api(keyword):
    # 데이터랩 API 최근 30일간 조회비율
    client_id = "4F5CQkZ_TVFe9HrLCCY5"
    client_secret = "NWFWkw6E0u"
    url = "https://openapi.naver.com/v1/datalab/search"
    month_ago_date = datetime.now() - timedelta(days=30)
    yesterday_date = datetime.now() - timedelta(days=1)
    body = {
        "startDate": month_ago_date.strftime("%Y-%m-%d"),
        "endDate": yesterday_date.strftime("%Y-%m-%d"),
        "timeUnit": "date",
        "keywordGroups": [
            {"groupName": str(keyword), "keywords": [str(keyword)]}
        ],
    }
    body = json.dumps(body)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    json_obj = json.loads(response.read().decode('utf-8'))

    return json_obj

    # URL을 읽어서 HTML를 받아오고,

def taporder_api(keyword):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    _url = "https://search.naver.com/search.naver?query="

    keyword_url = _url + keyword

    data = requests.get(keyword_url, headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    tap_order = soup.select('#lnb > div > div.lnb_menu > ul >li >a >span')
    tap_order_list = []
    # tap_names = soup.find_all('a',class_="tab") soup전체에서a중 클래스 탭을 싹가져옴.
    for tap_name in tap_order:
        tap_order_list.append(tap_name.text.strip())
    if "실시간검색" in tap_order_list:
        tap_order_list.insert(0,"실시간검색 있음")
    else:
        tap_order_list.insert(0,"실시간검색 없음")
    return tap_order_list


    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
