import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
import requests

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 &d일 %H시 %M분 입니다.')

Context = ssl._create_unverified_context()

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?ie=UTF-8&sm=whl_nht&query=%EC%A7%84%EC%A3%BC%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
#print(soup)

temp = soup.find('div', 'temperature_text')
#print(temp)

dl_summary = soup.find('dl', 'summary_list')
#print(dl_summary)
print(dl_summary.text.strip())