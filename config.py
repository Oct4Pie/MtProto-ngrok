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
