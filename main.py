def start_project():
    print("شروع پروژه WARP+ رفرال")

def send_referral(referral_code, count):
    for i in range(count):
        # اینجا کد ارسال رفرال رو می‌نویسی
        print(f"رفرال شماره {i+1} با کد {referral_code} ارسال شد.")
        # می‌تونی اینجا تاخیر بذاری مثلا time.sleep(1)

if __name__ == "__main__":
    start_project()
    referral_code = "UjZJq"
    count = 100  # تعداد دفعاتی که می‌خوای رفرال بزنه
    send_referral(referral_code, count)
