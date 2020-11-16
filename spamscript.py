import pyautogui, time
time.sleep(4)
text = "hey :heart:"
while(True):
	Waiting_time =5 
	time.sleep(Waiting_time)
	print("waiting " + str(Waiting_time) + " secs...")
	pyautogui.typewrite(text)
	pyautogui.press("enter")
