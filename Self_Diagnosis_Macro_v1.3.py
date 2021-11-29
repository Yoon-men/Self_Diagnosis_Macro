'''
====================================================================================================
<Self_Diagnosis_Macro_v1.3>
* Made by Yoonmen *
- pc 사용 여부 확인(30초간 사용자 동작 감지) → If 동작 감지 O) headless 상태로 작업, If 동작 감지 X) 작업 후 pc 종료
====================================================================================================
'''

from xml.etree.ElementTree import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, NoAlertPresentException
import time
import csv
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from win10toast import ToastNotifier
import mouse
import os

user_status = 0                             # 0 == Offline / 1 == Online
option = Options()
option.add_argument('start-maximized')



# ----------------------------------------------------------------------------------------------------
"""사용자 동작 감지"""
detection_end = time.time() + 30
while time.time() <= detection_end :        # 30초 이내로 사용자 동작 감지되면 headless 옵션 추가
    if mouse.is_pressed('left') : 
        option.add_argument('headless')
        user_status = 1
        break               
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
"""CSV 읽기"""
f = open(r'(user.csv가 있는 곳)', 'r', encoding = 'utf-8')
user_csv = csv.reader(f)
user_info = []
user_num = 0

for row in user_csv : 
    user_info.append(row)
    user_num += 1
del user_info[0]            # 맨 윗줄은 안 봐요
user_num -= 1               # 맨 윗줄은 사람 취급도 안해요
# ----------------------------------------------------------------------------------------------------



chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(10)      # 페이지 로딩 10초 기다려준다. 10초 후에는 얄짤없다.

# ====================================================================================================

driver.get('https://hcs.eduro.go.kr/#/loginHome')

for i in range(0, user_num) : 
    # ----------------------------------------------------------------------------------------------------
    """(시작 ~ 사용자 정보 입력)"""
    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()                                                          # '자기진단 참여하기' 버튼
    driver.find_element_by_xpath('//*[@id="schul_name_input"]').click()                                                     # 학교 선택란
    Select(driver.find_element_by_id('sidolabel')).select_by_visible_text(f'{user_info[i][1]}')                             # 지역 선택
    Select(driver.find_element_by_id('crseScCode')).select_by_visible_text(f'{user_info[i][2]}')                            # 학교급 선택
    driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(f'{user_info[i][3]}')                                      # 학교명 입력
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()      # '검색' 버튼
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click()                             # 맨 위에 있는 학교 선택
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()                               # '학교 선택' 버튼 클릭
    driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(f'{user_info[i][0]}')                              # 사용자 이름 입력
    driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(f'{user_info[i][4]}')                               # 사용자 생년월일 입력
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()                                                           # '확인' 버튼 클릭
    # ----------------------------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------------------------
    """(설정 비밀번호 입력 ~ 로그인)"""
    def PW_input() : 
        user_pw = list(user_info[i][5])
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').click()                     # 비밀번호 입력란 클릭
        time.sleep(1)

        try : 
            driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{user_pw[0]}\"]').click()
        except NoSuchElementException : 
            driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{user_pw[0]}\"]').click()
        time.sleep(0.2)
        try : 
            driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{user_pw[1]}\"]').click()
        except NoSuchElementException : 
            driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{user_pw[1]}\"]').click()
        time.sleep(0.2)
        try : 
            driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{user_pw[2]}\"]').click()
        except NoSuchElementException : 
            driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{user_pw[2]}\"]').click()
        time.sleep(0.2)
        try : 
            driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{user_pw[3]}\"]').click()
        except NoSuchElementException : 
            driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{user_pw[3]}\"]').click()
        time.sleep(0.2)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()       # '확인' 버튼 클릭

    try :                                                                   # 입력 시간 제한으로 인한 작동 멈춤 방지
        while True : 
            PW_input()
            time.sleep(0.2)
            driver.switch_to_alert
            Alert(driver).accept()

    except NoAlertPresentException :
        pass
    # ----------------------------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------------------------
    """자가진단"""
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()      # 참여자 목록 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()                                          # 1번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()                                          # 2번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()                                          # 3번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q4a1"]').click()                                          # 4번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()                                           # '제출' 버튼 클릭
    time.sleep(0.5)
    # ----------------------------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------------------------
    """계정 전환"""
    driver.find_element_by_xpath('//*[@id="topMenuBtn"]').click()                                           # '메뉴 보기' 버튼 클릭
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="topMenuWrap"]/ul/li[4]/button').click()                          # '로그아웃' 버튼 클릭
    driver.switch_to_alert
    Alert(driver).accept()                                                                                  # 로그아웃 허용
    time.sleep(0.5)

    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/button').click()                       # '다른계정 로그인' 버튼 클릭
    driver.switch_to_alert
    Alert(driver).accept()                                                                                  # 계정 전환 허용
    # ----------------------------------------------------------------------------------------------------



driver.close()



# ----------------------------------------------------------------------------------------------------
"""각 상태별 결과"""
if user_status == 0 :       # 사용자가 오프라인 상태일 경우
    ToastNotifier().show_toast('자가진단 매크로', '자가진단이 완료되었습니다.\n곧 pc를 종료합니다.', duration=60, icon_path=r'(diagnosis.ico가 있는 곳)')
    os.system('shutdown -f -s -t 0')
elif user_status == 1 :         # 사용자가 온라인 상태일 경우
    ToastNotifier().show_toast('자가진단 매크로', '자가진단이 완료되었습니다.', duration=60, icon_path=r'(diagnosis.ico가 있는 곳)')
# ----------------------------------------------------------------------------------------------------
