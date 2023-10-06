from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://movie.daum.net/main'
chrome = webdriver.Chrome()

chrome.get(url)
time.sleep(3)

html = BeautifulSoup(chrome.page_source, 'lxml')
time.sleep(1)

chrome.close()

print(html.select('div.poster_movie span.rank_num')[0].text)
print(html.select('div.poster_movie span.txt_append')[0].text)
print(html.select('div.poster_info dl:nth-child(1)')[0].text.strip().replace('\n',''))
print(html.select('div.poster_info dl:nth-child(2)')[0].text.strip().replace('\n',''))
print(html.select('div.poster_info dl:nth-child(3)')[0].text.strip().replace('\n',''))
print(html.select('div.poster_info dl:nth-child(4)')[0].text.strip().replace('\n',' '))
print(html.select('div.poster_info dl:nth-child(5)')[0].text.strip().replace('\n',' '))
# print(html.select('table.poll-table td:nth-child(3)')[0].text)
# print(html.select('table.poll-table td:nth-child(4) div:first-child')[0]['title'])
# print(html.select('table.poll-table td:nth-child(4) div:nth-child(2)')[0]['title'])
# print(html.select('table.poll-table td:nth-child(4) div:nth-child(3)')[0]['title'])