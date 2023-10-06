import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'http://www.k-apt.go.kr/'

# 셀레니엄 초기화
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
services = Service(ChromeDriverManager().install()) #드라이버 자동설치
chrome = webdriver.Chrome(service = services, options = options)

#사이트 이동
chrome.get(url)
time.sleep(1)

# 팝업 닫기 1
chrome.find_element(By.CSS_SELECTOR, '#layerPopup20230609 .layerP_bottom button').click()
time.sleep(1)
chrome.find_element(By.CSS_SELECTOR, '#layerPopup20230320 .layerP_bottom button').click()
time.sleep(1)


# 팝업 닫기 2
chrome.execute_script("closePopupLayer($('#layerPopup20230320'))")
time.sleep(1)
chrome.execute_script("closePopupLayer($('#layerPopup20230609'))")
time.sleep(1)

#우리단지 기본정보로 이동
chrome.find_element(By.CSS_SELECTOR, '#nav li:first-child a').click()
time.sleep(1)

chrome.find_element(By.CSS_SELECTOR, '.wp220 li:first-child a').click()
time.sleep(1)

#우리단지 기본정보로 이동2
chrome.execute_script("goMapView('/kaptinfo/openkaptinfo.do')")
time.sleep(1)

# 검색 할 단지정보 설정
syear = '2023년'
smonth = '07월'
ssido = '서울특별시'
sgugun = '강남구'
sdong = '삼성동'


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

# 아파트 목록 출력
from bs4 import BeautifulSoup

html = BeautifulSoup(chrome.page_source, 'lxml')

# 아파트 이름/주소 출력
for name in html.select('.aptS_rLName'):
    print(name.text)

for addr in html.select('.aptS_rLAdd'):
    print(addr.text)

# 아파트 목록 클릭
# 첫번째 아파트 클릭
chrome.find_element(By.CSS_SELECTOR, '#mCSB_2_container li:nth-child(1) a').click()
time.sleep(1)

# 마지막 아파트 클릭 - 눈에 안보이므로 클릭불가! ( 화면 안에 보이지 않으면 클릭이 불가함)
chrome.find_element(By.CSS_SELECTOR, '#mCSB_2_container li:nth-child(11) a').click()
time.sleep(1)

# 클릭대상 아파트의  idx 확인
aptname = '아이파크삼성동'
idx = 1
for name in html.select('.aptS_rLName'):
   if aptname == name.text: break
   idx += 1

print(idx)

# 클릭대상 아파트 검색 후 클릭

apts = chrome.find_elements(By.CSS_SELECTOR, '.aptS_rLName')
print(len(apts))

for idx, apt in enumerate(apts):                # 목록에서 내가 입력한 아파트 이름에 맞춰 검색 결과가 나올 수 있도록
    webdriver.ActionChains(chrome).move_to_element(apts[idx]).perform()
    #print(idx, apt.text)
    if aptname == apt.text:
        chrome.execute_script("arguments[0].click();", apts[idx])
time.sleep(1)
##### 눈에 안보이는 객체 클릭하기 ######
# ActionChains의 move_to_element 함수를 이용해서
# 목록의 나머지 항목까지 볼 수 있게 마우스 커서를 이동시킬 수 있음 ==> 리스트에서 그 다음 항목으로 하나하나 넘어갈 수 있도록..
# 또한 execute_script 에 매개변수를 이용해서
# 조건에 맞는 특정 객체에 이벤트를 수행 할 수 있음


# 관리시설정보로 이동
chrome.find_element(By.CSS_SELECTOR, '.lnb li:nth-child(3) a').click()
time.sleep(1)

# chrome.find_element(By.XPATH, '//a[@title="관리시설정보"]').click()
#
# //*[@id="container"]/div[2]/div[1]/ul/li[3]/a


# 주차장 대수 출력

chrome.find_element(By.CSS_SELECTOR, '#kaptd_pcnt').text
chrome.find_element(By.CSS_SELECTOR, '#kaptd_pcntu').text

#내가 짠 코드: 글씨도 다 나옴..
plots = chrome.find_element(By.CSS_SELECTOR, '.contTbl tr:nth-child(5)')
print(plots.text)


# 셀레니엄 종료
chrome.quit()



