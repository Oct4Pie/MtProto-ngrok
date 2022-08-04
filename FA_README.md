
# <p align="center"> MtProto-ngrok
<p align="center"> تلگرام خود را عمومی کنید MtProto پروکسی های

![](https://img.shields.io/github/issues/Oct4Pie/MtProto-ngrok) 
![](https://img.shields.io/github/forks/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/github/stars/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/github/license/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FOct4Pie%2FMtProto-ngrok)


> (MtProto) با استفاده از این پروژه شما میتوانید پروکسی های خود را بدون نیاز به هیچ  گونه وابستگی دیگر عمومی کنید    [mtprotoproxy](https://github.com/alexbers/mtprotoproxy) :خود پروژه از پروکسی به صورت پیش فرض استفاده میکند



## شروع

این کد روی ویندوز ۱۰، مک، و بیشتر ورژن های لینوکس با پایتون ۳.۵ الی ۳.۹ تست شده است

* برای نصب برای روی دستگاه خود توسط گیت:

```
git clone https://github.com/Oct4Pie/MtProto-ngrok.git
```

### پیش نیازها

  

پروکسی ممکن است با نصب ماژول [رمزنگاری](https://pypi.org/project/cryptography/) پرسرعت‌تر و سریعتر اجرا شود.

  

* ماژول رمزنگاری پایتون از پای‌پای توسط ماژول پیپ قابل نصب است:

```
pip3 install cryptography
```

  

* را دانلود کرده و اجرا میکند ngrok `main.py` فایل

* به یک توکن احراز هویت احتیاج دارد ngrok

* [اینجا](https://dashboard.ngrok.com/signup) ثبت نام کنید و سپس رمز خود را از [اینجا](https://dashboard.ngrok.com/auth/your-authtoken) دریافت کنید

  

* را برابر با توکن دریافت شده تنظیم کنید `main.py` داخل فایل `AUTHTOKEN`

  

### اجرا

  

* ngrok برای اجرای پروکسی سرور و تونل:

  

```
cd MtProto-ngrok

python3 main.py
```

  

* آدرس خروجی را می توان در برنامه تلگرام یا مرورگر جای گذاری کرد

  
## repl.it اجرا روی
* دانلود کنید repl.it می توانید مخزن را از طریق
* ثبت نام کنید [https://repl.it/signup ](https://repl.it/signup) در
* روی "+" کلیک کنید "Create" در صفحه اصلی ، در بخش
* آدرس مخزن را وارد کنید: [https://github.com/Oct4Pie/MtProto-ngrok.git]

<img  src="./replit_demo.png"  width="600"  height="350">
<img  src="./replit_demo1.png"  width="600"  height="400">

* پایتون را به عنوان زبان انتخاب کنید
* را ست کنید `run="python3 main.py"`
* کد را اجرا کنید "Run" از طریق 
* `python3 main.py` shell یا از طریق 

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


<img  src="./proxy_demo.gif"  width="350"  height="600">


## تبلیغ کانال

* در تلگرام مراجعه کنید [@MTProxybot](https://t.me/MTProxybot) جهت گرفتن تگ به ربات

* را برابر با تگ خود تنظیم کنید `config.py` داخل `AD_TAG` سپس

## گروه پشتیبانی تلگرام
* [https://t.me/MtProto_ngrok](https://t.me/MtProto_ngrok) به ما بپیوندید


## مجوز

* محفوظ است MIT این پروژه تحت مجوز

* میتوانید کد را با ذکر منبع تغییر داده و منتشر کنید

* همچنین مسئولیت هرگونه ناسازگاری و یا آسیب به دستگاه به عهده کاربر است

* مراجعه کنید [LICENSE](LICENSE) برای جزئیات بیشتر به پرونده

  
  

## تقدیر و تشکر

*  [Async MTProto Proxy پروژه](https://github.com/alexbers/mtprotoproxy)
*  [ngrok](https://ngrok.io)