import pyautogui
import keyboard
import threading
import time
import random


clicking = False
exit_program = False

#you can change from here how much time delay do you want
MIN_DELAY = 0.08
MAX_DELAY = 0.35

def clicker():

    global clicking, exit_program

    while not exit_program: #works till you exit
        if clicking:
            pyautogui.click()

            # random wait like a person
            delay = random.uniform(MIN_DELAY, MAX_DELAY)
            time.sleep(delay)
        else:
            time.sleep(0.1)  

def toggle_clicking():

    global clicking
    clicking = not clicking
    print("Clicking aktif mi?:", clicking)

def stop_program():

    global exit_program
    exit_program = True
    print("Program kapatılıyor...")

#you can change from here which key you want
keyboard.add_hotkey("F8", toggle_clicking)
keyboard.add_hotkey("F9", stop_program)

# so keyboard keep working
thread = threading.Thread(target=clicker)
thread.start()

print("Hazır!")
print("F8 : Başlat / Durdur")
print("F9 : Çıkış")

thread.join()
