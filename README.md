# <p align="center">MtProto-ngrok
#### <p align="center">  [راهنما فارسی](FA_README.md)
  
<p align="center"> Expose Your MtProto Proxy to the Internet

![](https://img.shields.io/github/issues/Oct4Pie/MtProto-ngrok) 
![](https://img.shields.io/github/forks/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/github/stars/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/github/license/Oct4Pie/MtProto-ngrok)
![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FOct4Pie%2FMtProto-ngrok)

> You can use this project to expose your Telegram MtProto proxy and don't worry about portability and port forwarding. This project is using [mtprotoproxy](https://github.com/alexbers/mtprotoproxy), written in Python.


## Getting Started

The code has been tested on Windows 10, macOS, and most Linux operating systems with Python 3.5-3.12.
* To get a copy via git: 
```
git clone https://github.com/Oct4Pie/MtProto-ngrok.git
```

### Prerequisites

The proxy may run smoother and faster when the [cryptography](https://pypi.org/project/cryptography/) module is installed.
* It can be installed from pypi via PIP:
```
pip3 install cryptography
```
* `main.py` downloads and runs ngrok
* Ngrok requires an authentication token to route TCP traffic. You can sign up at [here](https://dashboard.ngrok.com/signup) and then obtain your token from [here](https://dashboard.ngrok.com/get-started/your-authtoken).
* Set `AUTHTOKEN` in `config.py` equal to your token.

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
## Running
* To run the proxy server and ngrok tunnel use:
```bash
cd MtProto-ngrok
python3 main.py
```
* The output url can be pasted in your Telegram app
#### Example
```bash
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
https://github.com/Oct4Pie/MtProto-ngrok/assets/65843843/2bd9fd4d-348d-453a-8f8e-06cd6eb76946
<img  src="https://i.imgur.com/EAH4lpc.jpeg"  width="400"  height="800">


## Running on Repl.it
* Sign up or log in to [Replit](https://replit.com).
* On the Replit dashboard, click the "Create" button.
* Choose the "Python" template to set up a new Python environment.
* Give your Repl a name and optionally provide a description.
* You can directly import the GitHub repository by clicking "Import from GitHub" and providing the repository URL: [https://github.com/Oct4Pie/MtProto-ngrok](https://github.com/Oct4Pie/MtProto-ngrok)
* Use the integrated code editor to write your code. Replit's editor supports syntax highlighting, auto-indentation, and other features.
* To manage packages and dependencies, navigate to the "Packages" tab on the left sidebar and install necessary packages.
* Add your environment variables using the Secrets management tool by clicking the "Secrets" icon on the left sidebar.
* Click the green "Run" button at the top of the editor page to execute your code.
* To add collaborators, use the "Invite" button and share your Repl link with others.
* If your project involves a web application, deploy it directly from Replit using the "Share" menu.

<img src="https://i.imgur.com/Uv97mK3.png" width="600"  height="200">
<img src="https://i.imgur.com/WL6kRsn.png" width="600"  height="350">
<img src="https://i.imgur.com/cEJT8yW.png" width="600"  height="400">
<img src="https://i.imgur.com/7SkNLmh.png">


## Advertising Channels

* Refer to the [@MTProxybot](https://t.me/MTProxybot) Telegram bot to obtain a tag
* Set `AD_TAG` in `config.py` equal to your tag


## Acknowledgments

* [Async MTProto Proxy](https://github.com/alexbers/mtprotoproxy)
* [ngrok](https://ngrok.io)

## License
This project is licensed under the MIT License
See [LICENSE](LICENSE) file for more details
