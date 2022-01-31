'''
<Self_Diagnosis_Macro_v1.6> - 22.1.31. (MON) 19:22
* Made by Yoonmen *

[update]
1. 자동으로 유저 데이터를 읽는 기능 추가
2. StaleElementReferenceException 방지 기능 추가 (2차)
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, StaleElementReferenceException
import time
import csv
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from win10toast import ToastNotifier
import os
import pyautogui

# <Default setting>
user_status = 0                             # 0 == Offline / 1 == Online
option = Options()
option.add_argument('start-maximized')

fixed_3_2 = [0, 1, 2, 3]
fixed_3_3 = [4, 5, 6, 7, 8]



# <시작 전 사용자 동작 감지>
a, b = pyautogui.position()
detection_end = time.time() + 30
while time.time() <= detection_end :        # 30초 이내로 사용자 동작(마우스 이동) 감지되면 headless 옵션 추가
    c, d = pyautogui.position()
    if (a, b) != (c, d) : 
        option.add_argument('headless')
        user_status = 1
        break


# <CSV 파일 읽기>
f = open("./DB/user.csv", "r", encoding = "utf-8")
user_csv = csv.reader(f)
user_info = []
user_num = 0

for row in user_csv : 
    user_info.append(row)
    user_num += 1
del user_info[0]            # 맨 윗줄 무시 작업 (1)
user_num -= 1               # 맨 윗줄 무시 작업 (2)



# <chromedriver ON>
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(1)      # 페이지 로딩 20초 기다려준다. 20초 후에는 얄짤없다.



# <Start self-diagnosis>
driver.get('https://hcs.eduro.go.kr/#/loginHome')

for i in range(user_num) : 
    # (시작 ~ 사용자 정보 입력)
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


    # (설정 비밀번호 입력 ~ 로그인)
    def PW_input() : 
        user_pw = list(user_info[i][5])
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]').click()                     # 비밀번호 입력란 클릭
        time.sleep(1)

        for j in range(4) : 
            if user_pw[j] in fixed_3_2 : 
                driver.find_element_by_class_name(f"transkey_div_3_2[aria-label=\"{user_pw[j]}\"]").click()
            
            elif user_pw[j] in fixed_3_3 : 
                driver.find_element_by_class_name(f"transkey_div_3_3[aria-label=\"{user_pw[j]}\"]").click()
            
            else : 
                try : 
                    driver.find_element_by_class_name(f"transkey_div_3_2[aria-label=\"{user_pw[j]}\"]").click()
                except NoSuchElementException : 
                    driver.find_element_by_class_name(f"transkey_div_3_3[aria-label=\"{user_pw[j]}\"]").click()

            time.sleep(0.2)

        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()       # '확인' 버튼 클릭

    try :                                                                   # 입력 시간 제한으로 인한 작동 멈춤 방지
        while True : 
            PW_input()
            time.sleep(0.2)
            driver.switch_to_alert
            time.sleep(0.2)
            Alert(driver).accept()

    except NoAlertPresentException :
        pass



    # <자가진단 항목 체크>
    time.sleep(1)

    try : 
        driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/span[1]').click()      # 참여자 목록 클릭
    except StaleElementReferenceException : 
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



    # <게정 전환>
    driver.find_element_by_xpath('//*[@id="topMenuBtn"]').click()                                           # '메뉴 보기' 버튼 클릭
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="topMenuWrap"]/ul/li[4]/button').click()                          # '로그아웃' 버튼 클릭
    driver.switch_to_alert
    Alert(driver).accept()                                                                                  # 로그아웃 허용
    time.sleep(0.5)

    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div/button').click()                       # '다른계정 로그인' 버튼 클릭
    driver.switch_to_alert
    Alert(driver).accept()                                                                                  # 계정 전환 허용



# <자가진단 완료 후 창 닫기>
driver.close()



# <자가진단 완료 알림>
if user_status == 0 :       # 사용자가 오프라인 상태일 경우 - 종료 알림 후 30초 뒤에 pc 종료
    ToastNotifier().show_toast('자가진단 매크로', '자가진단이 완료되었습니다.\n곧 pc를 종료합니다.', duration=60, icon_path="./img/diagnosis.ico")
    os.system('shutdown -f -s -t 30')
elif user_status == 1 :         # 사용자가 온라인 상태일 경우
    ToastNotifier().show_toast('자가진단 매크로', '자가진단이 완료되었습니다.', duration=60, icon_path="./img/diagnosis.ico")