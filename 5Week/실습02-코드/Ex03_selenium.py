##################################################################
# Selenium을 이용한 웹 브라우저 자동화 - 구글에 접속하여 원하는 내용 검색
##################################################################
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait             # Implicitly wait
from selenium.webdriver.support import expected_conditions as EC    # Explicitly wait
from selenium.webdriver.chrome.options import Options


# 웹 브라우저 옵션 설정
opts = Options()
# opts.add_argument('--headless')               # 숨기기
opts.add_argument('--start-maximized')          # 창크기 최대화
# opts.add_argument('--window-size=1920,1080')  # 창크기 지정

driver = webdriver.Chrome(options=opts)         # 상황에 따라 달라지므로 직접 프로그램을 실행시킨 후 F12로 확인할 것
driver.implicitly_wait(time_to_wait=5)          # 암묵적 대기(초)
# driver.maximize_window()                      # driver.set_window_size(1300, 900)

try:    # name='q' 태그를 찾을 때까지 최대 10초를 기다림
    driver.get('https://google.com')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    for iframe in iframes:
        print(iframe.get_attribute('name'))

    # iframe 스위칭
    driver.switch_to.frame('callout')  # driver.switch_to.frame(0)
    driver.find_element(By.CLASS_NAME, "M6CB1c.rr4y5c").click()  # "건너뛰기" 클릭
    driver.switch_to.default_content()

    elem = driver.find_element(By.NAME, "q")
    # elem = driver.find_element(By.CLASS_NAME, "gLFyf")

    elem.clear()  # 안정성을 위해 입력필드를 지움
    elem.send_keys('파이썬')
    time.sleep(1)
    elem.send_keys(Keys.ENTER)  # elem.submit()

    # driver.find_element_by_class_name("LC20lb").click()       # 첫번째 검색 결과 (구버전)
    # driver.find_element_by_css_selector('.LC20lb').text       # 태그 검색 확인 (구버전)
    elems = driver.find_elements(By.CLASS_NAME, 'LC20lb')       # 모든 결과 결과

    print(elems[1].text, end='')        # 두번째 결과 제목 출력
    elems[1].click()
    time.sleep(5)
    print(driver.current_url)           # URL 출력
    driver.back()       # driver.forward()

except Exception as e:
    print(e)

finally:
    time.sleep(5)
    driver.quit()       # driver.close()
