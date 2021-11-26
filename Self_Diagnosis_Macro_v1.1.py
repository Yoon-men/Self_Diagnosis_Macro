'''
====================================================================================================
<Self_Diagnosis_Macro_v1.1>
* Made by Yoonmen *
- CSV 읽기 기능 추가
====================================================================================================
'''

from xml.etree.ElementTree import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import pyautogui
pyautogui.PAUSE = 0.5
import time
import csv
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

chrome_place = '(Chrome.exe가 있는 곳)'



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



try:
    shutil.rmtree(f"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

subprocess.Popen(f'{chrome_place} --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.maximize_window()
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.maximize_window()

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
