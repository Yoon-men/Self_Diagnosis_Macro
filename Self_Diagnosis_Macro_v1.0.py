'''
====================================================================================================
<Self_Diagnosis_Macro_v1.0>
* Made by Yoonmen *
====================================================================================================
'''

from xml.etree.ElementTree import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import keyboard
import sys
import time

try:
    shutil.rmtree(f"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

print('===========================================================')
print('\n<Self_Diagnosis_Macro_v1.0>')
print('\n- Made by Yoonmen -')
print('\n===========================================================')


# ----------------------------------------------------------------------------------------------------
'''사용자 입력 저장'''
chrome_place = input('\n[system] 크롬이 있는 곳을 입력하세요 : ')

School_Name = input('\n[system] 다니는 학교의 이름을 입력하세요(Example> 킹북고등학교) : ')
User_Name = input('\n[system] 사용자의 이름을 입력하세요 : ')
User_Birth = input('\n[system] 사용자의 생년월일을 입력하세요(Example> 030101) : ')
User_PW = str(input('\n[system] 사용자의 비밀번호를 입력하세요(Example> 1234) : '))
User_PW_List = list(User_PW)
# ----------------------------------------------------------------------------------------------------


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


def start() : 
    # ----------------------------------------------------------------------------------------------------
    '''(시작 ~ 사용자 정보 입력)'''
    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()                  # '자기진단 참여하기' 버튼
    driver.find_element_by_xpath('//*[@id="schul_name_input"]').click()             # 학교 선택란
    driver.find_element_by_xpath('//*[@id="sidolabel"]/option[4]').click()          # 대구광역시 선택
    driver.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()         # 고등학교 선택
    driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(School_Name)       # 학교명 입력
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()      # '검색' 버튼
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click()                             # 맨 위에 있는 학교 선택
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()       # '학교 선택' 버튼 클릭
    driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(User_Name)     # 사용자 이름 입력
    driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(User_Birth)     # 사용자 생년월일 입력
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()                       # '확인' 버튼 클릭
    # ----------------------------------------------------------------------------------------------------


def pw() : 
    # ----------------------------------------------------------------------------------------------------
    '''(설정 비밀번호 입력 ~ 확인)'''
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password"]').click()                     # 비밀번호 입력란 클릭
    time.sleep(1)
    try : 
        driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{User_PW_List[0]}\"]').click()
    except NoSuchElementException : 
        driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{User_PW_List[0]}\"]').click()
    time.sleep(0.2)
    try : 
        driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{User_PW_List[1]}\"]').click()
    except NoSuchElementException : 
        driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{User_PW_List[1]}\"]').click()
    time.sleep(0.2)
    try : 
        driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{User_PW_List[2]}\"]').click()
    except NoSuchElementException : 
        driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{User_PW_List[2]}\"]').click()
    time.sleep(0.2)
    try : 
        driver.find_element_by_class_name(f'transkey_div_3_2[aria-label=\"{User_PW_List[3]}\"]').click()
    except NoSuchElementException : 
        driver.find_element_by_class_name(f'transkey_div_3_3[aria-label=\"{User_PW_List[3]}\"]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()       # '확인' 버튼 클릭
    # ----------------------------------------------------------------------------------------------------


def diagnosis() : 
    # ----------------------------------------------------------------------------------------------------
    '''자가진단'''
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()      # 참여자 목록 클릭
    driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()                                  # 1번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()                                  # 2번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()                                  # 3번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="survey_q4a1"]').click()                                  # 4번 아니요 클릭
    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()                                   # '제출' 버튼 클릭
    print('\n[system] 자가진단이 완료되었습니다.')
    # ----------------------------------------------------------------------------------------------------


def end() : 
    driver.close()

start()
pw()
diagnosis()
end()
