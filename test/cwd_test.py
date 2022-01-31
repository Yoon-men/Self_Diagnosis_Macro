import os
import keyboard

print("[system] Current Working Directory : ", os.getcwd(), "\n")      # cwd = Current Working Directory
print("[system] ESC키를 입력하면 프로그램을 종료합니다.")
while True : 
    if keyboard.is_pressed('esc') : 
        break
