import requests
import random
import string
import time

# کلید رفرال WARP+ خودت رو اینجا بزار
REFERRAL_CODE = "UjZJq"

# تعداد رفرال‌هایی که می‌خوای بزنی
REFERRAL_COUNT = 10

def gen_rand_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=22))

def send_referral():
    install_id = gen_rand_id()
    payload = {
        "key": "{}=".format(gen_rand_id() + "="),
        "install_id": install_id,
        "fcm_token": f"{install_id}:APA91b{gen_rand_id()}",
        "referrer": REFERRAL_CODE,
        "warp_enabled": False,
        "tos": "2023-11-01T07:35:00.000+00:00",
        "type": "Android",
        "locale": "en_US"
    }

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'okhttp/3.12.1'
    }

    response = requests.post("https://api.cloudflareclient.com/v0a745/reg", json=payload, headers=headers)

    return response.status_code

# اجرای برنامه
for i in range(1, REFERRAL_COUNT + 1):
    status = send_referral()
    if status == 200:
        print(f"[✓] رفرال {i} موفق")
    elif status == 403:
        print(f"[✗] رفرال {i} بلاک شد! آی‌پی رو عوض کن.")
        break
    else:
        print(f"[!] رفرال {i} ناموفق - وضعیت: {status}")
    
    # تأخیر تصادفی بین هر درخواست (3 تا 7 ثانیه)
    time.sleep(random.uniform(3, 7))
