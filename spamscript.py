import pyautogui, time

print("what do you want to type?:")
text = input()
print("i will type: ", text)
print("how many seconds should i wait each time? (only numbers, please. be gentle.)")
Waiting_time = int(input())
sleep_time = 4
print("i will give you ",sleep_time," seconds to get ready :)")
time.sleep(4)
print("let's fucking do it!\nkill me with ctrl+c")

while(True):
	time.sleep(Waiting_time)
	print("waiting " + str(Waiting_time) + " secs...")
	pyautogui.typewrite(text)
	pyautogui.press("enter")
