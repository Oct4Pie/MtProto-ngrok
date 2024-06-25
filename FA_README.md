
# <p align="center">MtProto-ngrok
#### <p align="center">  [راهنما فارسی](FA_README.md)
  
<p align="center"> پروکسی های MtProto تلگرام خود را عمومی کنید 

![](https://img.shields.io/github/issues/Oct4Pie/MtProto-ngrok) 
![](https://img.shields.io/github/forks/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/github/stars/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/github/license/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FOct4Pie%2FMtProto-ngrok)


> (MtProto) با استفاده از این پروژه شما میتوانید پروکسی های تلگرام خود را بدون نیاز به هیچ گونه وابستگی دیگر عمومی کنید.  

## شروع

این کد روی ویندوز ۱۰، مک، و بیشتر ورژن های لینوکس با پایتون ۳.۵ الی ۳.۱۲ تست شده است.

* برای نصب از طریق گیت:
```
git clone https://github.com/Oct4Pie/MtProto-ngrok.git
```

### پیش نیازها

پروکسی ممکن است با نصب ماژول [رمزنگاری](https://pypi.org/project/cryptography/) پرسرعت‌تر و سریع‌تر اجرا شود.

* ماژول رمزنگاری پایتون از پای‌پای توسط ماژول پیپ قابل نصب است:
```
pip3 install cryptography
```

* `main.py` فایل ngrok را دانلود کرده و اجرا می‌کند.
* ngrok به یک توکن احراز هویت نیاز دارد تا ترافیک TCP را مسیریابی کند. شما می‌توانید از [اینجا](https://dashboard.ngrok.com/signup) ثبت نام کنید و سپس توکن خود را از [اینجا](https://dashboard.ngrok.com/get-started/your-authtoken) دریافت کنید.
* `AUTHTOKEN` را در فایل `config.py` برابر با توکن خود تنظیم کنید.
```python
# config.py
import os
import random

os.chdir(os.path.dirname(__file__))

PORT = 4443
USERS = {
    "tg": open("secret", "r").read() if os.path.exists("secret") else "",
}
MODES = {
    "classic": False,
    "secure": True,
    "tls": True,
}
TLS_DOMAIN = random.choice(
    [
        "www.ngrok.com",

    ]
)
AUTHTOKEN = ""  # set to your ngrok's token
# AD_TAG = "" # set to your ad tag
```

## اجرا
* برای اجرای پروکسی سرور و تونل ngrok از دستور زیر استفاده کنید:
```
cd MtProto-ngrok
python3 main.py
```
* آدرس خروجی را می‌توان در برنامه تلگرام یا مرورگر جای گذاری کرد.
#### مثال
```
$ python3 main.py
TLS: 
in-app: tg://proxy?server=6.tcp.ngrok.io&port=19977&secret=eed22691fe775a6bfefd0bd56c63afd8257777772e6e67726f6b2e636f6d
external: https://t.me/proxy?server=6.tcp.ngrok.io&port=19977&secret=eed22691fe775a6bfefd0bd56c63afd8257777772e6e67726f6b2e636f6d 

Secure: 
in-app: tg://proxy?server=6.tcp.ngrok.io&port=19977&secret=ddd22691fe775a6bfefd0bd56c63afd825
external: https://t.me/proxy?server=6.tcp.ngrok.io&port=19977&secret=ddd22691fe775a6bfefd0bd56c63afd825 

host:port -> 6.tcp.ngrok.io:19977
secret -> d22691fe775a6bfefd0bd56c63afd825
```
<img  src="https://i.imgur.com/EAH4lpc.jpeg"  width="400"  height="800">

## اجرای روی Repl.it
* ثبت نام یا ورود به [Replit](https://replit.com).
* در داشبورد Replit، روی دکمه "Create" کلیک کنید.
* الگوی "Python" را انتخاب کنید تا یک محیط جدید پایتون ایجاد شود.
* به پروژه خود نام بدهید و به صورت اختیاری توضیحاتی اضافه کنید.
* شما می‌توانید مخزن GitHub را مستقیماً با کلیک روی "Import from GitHub" و وارد کردن آدرس مخزن: [https://github.com/Oct4Pie/MtProto-ngrok](https://github.com/Oct4Pie/MtProto-ngrok) وارد کنید.
* از ویرایشگر کد یکپارچه استفاده کنید تا کد خود را بنویسید. ویرایشگر Replit از ویژگی‌های هایلایت کردن سینتکس، فرمت اتوماتیک و ویژگی‌های دیگر پشتیبانی می‌کند.
* برای اجرای کد خود روی دکمه سبز "Run" در بالای صفحه ویرایشگر کلیک کنید.

<img src="https://i.imgur.com/Uv97mK3.png" width="600" height="200">
<img src="https://i.imgur.com/WL6kRsn.png" width="600" height="350">
<img src="https://i.imgur.com/cEJT8yW.png" width="600" height="400">
<img src="https://i.imgur.com/7SkNLmh.png">

## تبلیغ کانال‌ها

* به ربات تلگرام [@MTProxybot](https://t.me/MTProxybot) مراجعه کنید تا یک تگ دریافت کنید.
* `AD_TAG` را در فایل `config.py` برابر با تگ خود تنظیم کنید.

## تقدیر و تشکر

* [Async MTProto Proxy](https://github.com/alexbers/mtprotoproxy)
* [ngrok](https://ngrok.io)

## مجوز
این پروژه تحت مجوز MIT قرار دارد.
برای جزئیات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.
