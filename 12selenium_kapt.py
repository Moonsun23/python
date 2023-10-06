import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# url 설정
base = 'http://www.k-apt.go.kr/'
url1 = base + 'cmmn/bjd/getBjdList.do' # 주소
url2 = base + 'kaptinfo/getKaptList.do' # 아파트
url3 = base + 'kaptinfo/getKaptInfo_detail.do' # 관리시설

# 검색 할 단지정보 설정
syear = '2023년'
smonth = '07월'
ssido = '서울특별시'
sgugun = '강남구'
sdong = '삼성동'

# 셀레니엄 초기화
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
services = Service(ChromeDriverManager().install()) #드라이버 자동설치
chrome = webdriver.Chrome(service = services, options = options)

chrome.get(base)
time.sleep(1)

chrome.execute_script("closePopupLayer($('#layerPopup20230609'))")
time.sleep(1)

chrome.execute_script("closePopupLayer($('#layerPopup20230320'))")
time.sleep(1)

chrome.execute_script("goMapView('/kaptinfo/openkaptinfo.do')")
time.sleep(1)

year = Select(chrome.find_element(By.NAME, 'searchYYYY'))
year.select_by_visible_text(syear)
time.sleep(1)

month = Select(chrome.find_element(By.NAME, 'searchMM'))
month.select_by_visible_text(smonth)
time.sleep(1)

sido= Select(chrome.find_element(By.NAME, 'combo_SIDO'))
sido.select_by_visible_text(ssido)
time.sleep(1)

gugun= Select(chrome.find_element(By.NAME, 'combo_SGG'))
gugun.select_by_visible_text(sgugun)
time.sleep(1)

dong= Select(chrome.find_element(By.NAME, 'combo_EMD'))
dong.select_by_visible_text(sdong)
time.sleep(1)

# 선택한 시군동에 대한 전체코드 출력 : bjdcode


# 선택한 아파트에 대한 전체코드 출력 : data-kaptcode
# 속성값 불러오기 : find_element(선택자).get_attribute(속성명)
# 아파트명, kapcode 출력

# 내코드
from bs4 import BeautifulSoup

html = BeautifulSoup(chrome.page_source, 'lxml')

for name in html.select('.aptS_rLName'):
    print(name.text)

for kcode in html.select('li[data-kaptcode]'):
    print(kcode['data-kaptcode'])

# 선생님 코드
apts = chrome.find_elements(By.CSS_SELECTOR, '#mCSB_2_container li')
for i in range(1, len(apts)+1):
    apt= chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container li:nth-child({i})')
    name= chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container li:nth-child({i}) .aptS_rLName')
  #  print(name.text, apt.get_attribute('data-kaptcode'))
    print(apt.get_attribute('onclick'))

# 기본정보 출력
apt= chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container li:nth-child(16)')
js = apt.get_attribute('onclick')
chrome.execute_script(js)

# 아파트 명칭, 주소 출력
from bs4 import BeautifulSoup

html = BeautifulSoup(chrome.page_source, 'lxml')
print(html.select('.contTbl tr:nth-child(1) td')[0].text)

print(html.select('.contTbl tr:nth-child(2) td')[0].text)

# 관리시설 정보 조회
apt= chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container li:nth-child(16)')
aptcode = apt.get_attribute('data-kaptcode')
print(aptcode)

url3 = url3 + f'?kapt_code={aptcode}'
chrome.get(url3)
#print(chrome.page_source)

html = BeautifulSoup(chrome.page_source, 'lxml')
print(html.find('body'))

import json

aptjson = json.loads(html.find('body').text)
aptjson

print(aptjson.get('resultMap_kapt').get('KAPTD_PCNT'))
print(aptjson.get('resultMap_kapt').get('KAPTD_PCNTU'))

# requests 를 이용해서 단지정보 검색
import requests

res = requests.get(url3)
html = BeautifulSoup(res.text, 'lxml')
aptjson2 = json.loads(html.find('body').text)

print(aptjson2.get('resultMap_kapt').get('KAPTD_PCNT'))
print(aptjson2.get('resultMap_kapt').get('KAPTD_PCNTU'))

chrome.quit()