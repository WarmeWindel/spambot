#by WarmeWindel https://github.com/WarmeWindel!

from time import sleep
import pyautogui

message = 0
count = 0
delay = 0


message = input("Enter your message:")
count = int(input("Enter how many times you want to type your message:"))
delay = int(input("Enter your delay:"))

print("starting")
print("click where youw want to type! starting in 5seconds")
sleep(5)

while count >= 0:
    pyautogui.write(message)
    sleep(delay)
    pyautogui.press('enter')
    count -1 
else:
    exit()    

exit() 


