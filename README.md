# Self_Diagnosis_Macro
![image](https://user-images.githubusercontent.com/64591335/143431001-33b1b53e-34bf-40ee-95ae-c51667289c9f.png)
> 느슨해진 자가진단에 긴장감을 주는 프로그램
---
## What the fuck is this?
가상 키패드를 찢어발기는 자가진단 매크로 프로그램이오.<br><br> 
자가진단 사이트가 업데이트를 계속하는 한, 창과 방패의 싸움은 계속될 것임을 약속하오.<br><br>
허나, 이 처절한 전투의 본 목적을 잊어버려서는 안되는 법.<br><br>
**부디 그대의 건강에 이상이 없을 때만 이용해주기를 바랄 뿐이오.**<br><br>

## Get ready for the next battle
```
chrome_place = '(Chrome.exe가 있는 곳)'
```
.py 내에서 파일 경로를 맞게 고쳐주기를 바라네. ***(v1.1 ~ v1.2)***<br><br>
```
f = open(r'(user.csv가 있는 곳)', 'r', encoding = 'utf-8')
```
이 역시 파일 경로를 맞게 고쳐주기를 바라네. ***(v1.1 ~ )***<br><br>
```
ToastNotifier().show_toast('자가진단 매크로', '자가진단이 완료되었습니다.', duration=60, icon_path=r'(diagnosis.ico가 있는 곳)')
```
자가진단이 완료되고 나서 나오는 알림의 아이콘을 바꾸고 싶다면 여기서도 역시 파일 경로에 맞게 고쳐주게나. ***(v1.3 ~ )***<br><br>
## Update History
◇ 2021.11.25.목 02:38 // v1.0
- v1.0 개발

◇ 2021.11.25.목 16:54 // v1.1
- CSV 읽기 기능 추가

◇ 2021.11.26.금 ??:?? // v1.2
- 입력 시간 제한으로 인한 멈춤 방지 기능 추가

◇ 2021.11.29.월 23:40 // v1.3
- 사용자 상태 확인 기능 추가(Online = headless 옵션 추가 / Offline = 작업 후 pc 종료)

◇ 2021.12.5.일 00:51 // v1.4
- StaleElementReferenceException 방지 기능 추가

◇ 2021.12.6.월 09:40 // v1.5
- 사용자 동작 감지 방식 변경
