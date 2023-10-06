from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'http://poll-mbc.co.kr/'
chrome = webdriver.Chrome()

chrome.get(url)
time.sleep(3)

html = BeautifulSoup(chrome.page_source, 'lxml')
time.sleep(1)

chrome.close()

print(html.select('table.poll-table td:nth-child(2)')[0].text)
print(html.select('table.poll-table td:nth-child(3)')[0].text)
print(html.select('table.poll-table td:nth-child(4) div:first-child')[0]['title'])
print(html.select('table.poll-table td:nth-child(4) div:nth-child(2)')[0]['title'])
print(html.select('table.poll-table td:nth-child(4) div:nth-child(3)')[0]['title'])