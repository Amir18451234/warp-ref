import requests
import random
import string
import time

def random_string(length=22):
    return ''.join(random.choices(string.ascii_letters + string.digits + '_-', k=length))

def send_warp_referral(referral_code, count=100):
    url = "https://api.cloudflareclient.com/v0a745/reg"
    headers = {
        "User-Agent": "okhttp/3.12.1",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept-Encoding": "gzip",
        "Connection": "Keep-Alive",
        "Host": "api.cloudflareclient.com"
    }
    for i in range(count):
        install_id = random_string()
        fcm_token = f"{install_id}:APA91b{random_string(134)}"
        key = random_string(43) + "="

        payload = {
            "key": key,
            "install_id": install_id,
            "fcm_token": fcm_token,
            "referrer": referral_code,
            "warp_enabled": False,
            "tos": int(time.time()),
            "type": "Android",
            "locale": "en_US"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"رفرال شماره {i+1} ارسال شد!")
        else:
            print(f"خطا در ارسال رفرال شماره {i+1} - کد وضعیت: {response.status_code} - پاسخ: {response.text}")

        time.sleep(3)

if __name__ == "__main__":
    referral_code = "UjZJq"
    send_warp_referral(referral_code, 10)  # اول 10 بار تست کن
