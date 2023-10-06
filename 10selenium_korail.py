import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.letskorail.com/'
uid = '1262955471'
pwd = 'tjsanswkd08*'

deptst = '서울'
arrvst = '부산'
dpyear = '2023'
dpmonth = '9'
dpday = '16'
dphour = '10 (오전10)'


# 셀레니엄 초기화
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
services = Service(ChromeDriverManager().install()) #드라이버 자동설치
chrome = webdriver.Chrome(service = services, options = options)

#코레일 메인페이지 방문
chrome.get(url)
time.sleep(1)

# 팝업창 닫기
# 다른 창으로 제어를 넘기고 싶다면 : switch_to.window(핸들러)
print(chrome.window_handles)
print(chrome.window_handles[0]) # 메인창
print(chrome.window_handles[1]) # 팝업창

chrome.switch_to.window( chrome.window_handles[1])  # 팝업창으로 제어 넘김
chrome.close()

chrome.switch_to.window( chrome.window_handles[0])   # 부모창으로 제어넘김

#로그인 페이지로 이동
chrome.find_element(By.CSS_SELECTOR, 'ul.gnb_list li:nth-child(2) a').click()
time.sleep(1)


# 멤버십 번호 입력
uid =chrome.find_element(By.ID, 'txtMember')
uid.send_keys('1262955471')
time.sleep(1)

# 멤버십 비번 입력
pw =chrome.find_element(By.ID, 'txtPwd')
pw.send_keys('tjsanswkd08*')
time.sleep(1)

# 로그인 버튼 클릭
chrome.find_element(By.CSS_SELECTOR, '.btn_login a').click()
time.sleep(1)

# 메인페이지 팝업창 닫기
chrome.switch_to.window( chrome.window_handles[1])  # 팝업창으로 제어 넘김
chrome.close()

chrome.switch_to.window( chrome.window_handles[0])
time.sleep(1)

# 열차예매 페이지로 이동
chrome.find_element(By.CSS_SELECTOR, '.lnb_m01 a').click()
time.sleep(1)


# 종별 선택

chrome.find_element(By.ID, 'selGoTrainRa00').click()
time.sleep(1)

# 좌석종류선택
# seat = Select(chrome.find_element(By.CSS_SELECTOR, 'div.box_ck03__label'))
# seat.select_by_visible_text(seat)
# time.sleep(1)
#
# sway = Select(chrome.find_element(By.CSS_SELECTOR, ''))
# seat.select_by_visible_text(seat)
# time.sleep(1)

# 출발/도착역 설정
start = chrome.find_element(By.ID, 'start')
start.clear()
start.send_keys(deptst)
time.sleep(1)

get = chrome.find_element(By.ID, 'get')
get.clear()
get.send_keys(arrvst)
time.sleep(1)




# 출발일/시간 설정
# select 요소를 선택하려면 select_by_visible_text 함수 사용
syear = Select(chrome.find_element(By.ID, 's_year'))
syear.select_by_visible_text(dpyear)                    # 옵션 선택에서 글자로 선택한다
time.sleep(1)

smonth = Select(chrome.find_element(By.ID, 's_month'))
smonth.select_by_visible_text(dpmonth)                    # 옵션 선택에서 글자로 선택한다
time.sleep(1)

sday = Select(chrome.find_element(By.ID, 's_day'))
sday.select_by_visible_text(dpday)
time.sleep(1)

shour = Select(chrome.find_element(By.ID, 's_hour'))
shour.select_by_visible_text(dphour)
time.sleep(1)

#조회하기 버튼 클릭
chrome.find_element(By.CSS_SELECTOR, '.btn_inq a').click()
time.sleep(1)

#예약 버튼 클릭

# 브라우저의 특정 액션은 자바스크립트를 이용해서 처리
# 셀레니엄에서 자바스크립스를 실행하려면 execute_script 함수 사용

# 화면 스크롤
chrome.execute_script('window.scrollTo(0, 1080);')    # 스크롤 끝까지 내리도록
time.sleep(1)


# 예매하기 버튼 클릭


# 경고창 닫기
# 셀레니엄에서 경고창을 닫으려면 switch_to.alert.accept 함수 사용
chrome.switch_to.alert.accept()      # 20분 내 결제해야한다는 알림창
time.sleep(1)

chrome.switch_to.alert.accept()        # 뭐 그다음 알림창
time.sleep(1)

# 결제


# 결제유형 선택


# 신용카드 정보 입력

# 발권



chrome.close()
