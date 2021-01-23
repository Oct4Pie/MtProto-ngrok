import os

os.chdir(os.path.dirname(__file__))

PORT = 4443
USERS = {
    "tg": open("secret", "r").read() if os.path.exists("secret") else "",
}

MODES = {
    "classic": False,
    "secure": False,
    "tls": True,
}

TLS_DOMAIN = "www.telegram.org"
AUTHTOKEN = ""  # set to your ngrok's token
# AD_TAG = ""
