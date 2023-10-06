import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.yanolja.com/motel/r-900493?lat=37.50681&lng=127.06624&advert=AREA&topAdvertiseMore=0&sort=133&placeListType=motel&pathDivision=r-900493'

# 웹드라이버 초기화
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
services = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=services, options=options)

# URL 로드
chrome.get(url)

def infinite_scroll(chrome, timeout=2):
    last_height = chrome.execute_script("return document.body.scrollHeight")
    while True:
        chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(timeout)
        new_height = chrome.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# 웹 페이지 끝까지 스크롤하여 모든 내용을 로드합니다.
infinite_scroll(chrome)

# 숙소상세페이지 클릭해서 들어가는 알고리즘
div0 = 'PlaceListBody_listGroup__LddQf'
mname = 'PlaceListTitle_container__qe7XH PlaceListTitle_text_2511B'

try:
    # 모든 숙소 이름 리스트를 가져옵니다.
    motel_names = [element.text for element in chrome.find_elements(By.CSS_SELECTOR, mname)]
    print("All Motel Names:", motel_names)

    # 모든 숙소 리스트 아이템을 가져옵니다.
    items = chrome.find_elements(By.CSS_SELECTOR, f'{div0} div a')

    for item in items:
        item.click()
        time.sleep(1)

        # 추가적인 크롤링 동작을 여기서 수행하면 됩니다.

        # 아이템의 크롤링이 끝나면 뒤로 가서 다음 아이템으로 넘어갑니다.
        chrome.back()
        time.sleep(1)

except Exception as e:
    print(f"Error occurred: {e}")

# 웹드라이버 종료
chrome.quit()




# 숙소명: div. css-t9rim1
# 전화번호: 제외
# 리뷰(친절도, 청결도, 편의성, 비품만족도): nth-child로.......
# 최신순 - 
### 친절도/ 청결도/ 편의성/ 비품만족도 : css-djkjag // 평점: css-1czpws0
# 주소: div. css-o8j33g
# 평점: div. css-nq91ht - div. <strong>

