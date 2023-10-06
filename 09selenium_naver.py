# pip install selenium
# pip install webdriver-manager
# pip install pyperclip

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

options = webdriver.ChromeOptions()
services = Service(ChromeDriverManager().install()) #드라이버 자동설치
chrome = webdriver.Chrome(service = services, options = options)

url = 'https://www.naver.com/'
chrome.get(url)

chrome.maximize_window()     #창 최대로 키우기

# 로그인 하기
# * 셀레니엄에서 특정요소를 css선택자로 제어하려면 find_element라는 함수를 이용
#     + find_element(By.선택자_유형, 선택자)
# * 셀레니엄에서 요소를 클릭하려면 선택자로 요소를 지정한 후 click함수 호출

chrome.find_element(By.CSS_SELECTOR, 'div.MyView-module__my_login___tOTgr a').click()
time.sleep(1)

# 아이디/ 비밀번호에 값 입력하기
# * 셀레니엄에서 특정요소에 값을 입력하려면 send_keys라는 함수 사용

nid = 'letmetalk2'
pyperclip.copy(nid)        # 아이디를 클립보드로 복사
uid =chrome.find_element(By.ID, 'id')
# uid.send_keys('letmetalk2')  # 네이버 로그인 시 실패
uid.send_keys(Keys.CONTROL+'v')  # 클립보드에 복사된 아이디를 붙여넣기 함
time.sleep(1)

npw= ''
pyperclip.copy(npw)        # 아이디를 클립보드로 복사
pwd =chrome.find_element(By.ID, 'pw')

pwd.send_keys(Keys.CONTROL+'v')
# passwd.send_keys('')   # 네이버 로그인 시 실패!
time.sleep(1)

chrome.find_element(By.ID, 'log.login').click()
time.sleep(1)

# 등록여부 지정 - 등록안함 선택
chrome.find_element(By.ID, 'new.dontsave').click()
time.sleep(1)

# 받은 쪽지 확인
memo= chrome.find_element(By.CSS_SELECTOR, 'MyView-module__link_new___lnR1w')
memo= chrome.find_element(By.CSS_SELECTOR, 'div.MyView-module__desc_new___BJQbF a:nth-child(3)')

print(memo.text)

# 로그아웃
chrome.find_element(By.CSS_SELECTOR, 'button.MyView-module__btn_logout___bsTOJ').click()
time.sleep(1)

# 크롬닫기
chrome.close()