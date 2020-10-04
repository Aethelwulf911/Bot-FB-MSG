import time
import pyautogui as rh

class coordinate:
	emptyMessage = (173,700)

def click():
	rh.click(coordinate.emptyMessage())

def typechat():
	rh.typewrite("this is an auto message")
	rh.typewrite("\n")
	time.sleep(0.5)

def send():
	print("text send")

while True:
	coordinate()
	click()
	typechat()
	time.sleep(5)