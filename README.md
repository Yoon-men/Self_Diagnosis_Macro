![title](img/SDM_header.jpg)
> 느슨해진 자가진단에 긴장감을 주는 프로그램
---
# What the fuck is this?
가상 키패드를 찢어발기는 자가진단 매크로 프로그램입니다.

**건강에 이상이 있을 때는 자가진단을 직접 해주세요.**

<br>

# Get ready for the next battle
```
chrome_place = '(Chrome.exe가 있는 곳)'
```
***(v1.1 ~ v1.2)*** .py 내에서 파일 경로를 맞게 고쳐주세요 <br><br>
```
f = open(r'(user.csv가 있는 곳)', 'r', encoding = 'utf-8')
```
***(v1.1 ~ )*** 이 역시 파일 경로를 맞게 고쳐주기를 바래요. <br><br>
```
ToastNotifier().show_toast('자가진단 매크로', '자가진단이 완료되었습니다.', duration=60, icon_path=r'(diagnosis.ico가 있는 곳)')
```
***(v1.3 ~ )*** 자가진단이 완료되고 나서 나오는 알림의 아이콘을 바꾸고 싶다면 여기서도 역시 파일 경로에 맞게 고쳐주세요. <br><br>

<br>

# Update History
◇ 2021.11.25. (THU) 02:38 // v1.0
- v1.0 개발

◇ 2021.11.25. (THU) 16:54 // v1.1
- CSV 읽기 기능 추가

◇ 2021.11.26. (FRI) ??:?? // v1.2
- 입력 시간 제한으로 인한 멈춤 방지 기능 추가

◇ 2021.11.29. (MON) 23:40 // v1.3
- 사용자 상태 확인 기능 추가(Online = headless 옵션 추가 / Offline = 작업 후 pc 종료)

◇ 2021.12.5. (SUN) 00:51 // v1.4
- StaleElementReferenceException 방지 기능 추가

◇ 2021.12.6. (MON) 09:40 // v1.5
- 사용자 동작 감지 방식 변경

◇ 2022.1.31. (MON) ??:?? // v1.6 (Will)
- 자동으로 유저 데이터를 읽는 기능 추가
- StaleElementReferenceException 방지 기능 추가 (1)
