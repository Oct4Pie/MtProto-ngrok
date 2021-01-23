import os
import json
import urllib.request
import zipfile
import io
import sys
import gzip
import platform
import time
import threading
import subprocess
import secrets
from config import PORT, TLS_DOMAIN, AUTHTOKEN
from http.server import HTTPServer, BaseHTTPRequestHandler


class GETHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(tls_link.encode("utf-8"))


def stay_alive():
    server_address = ("0.0.0.0", 8080)
    http_server = HTTPServer(server_address, GETHandler)
    http_server_thread = threading.Thread(target=http_server.serve_forever)
    http_server_thread.start()


def get_ngrok():

    os.system(
        "killall ngrok > /dev/null 2>&1"
    ) if uname.system != "Windows" else os.system("taskkill /f /im ngrok.exe 2> nul")

    ngrok_file = open(
        "ngrok.exe" if uname.system == "Windows" else "ngrok",
        "wb",
    )
    link = ""

    if uname.system == "Windows":
        if uname.machine == "x86_64" or uname.machine == "AMD64":
            link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip"

    elif uname.system == "Linux":
        if uname.machine == "aarch64" or uname.machine == "arm64":
            link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz"

        if uname.machine == "x86_64":
            link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"

        if "armv" in uname.machine:
            link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip"

    elif uname.system == "Darwin":
        if uname.machine == "x86_64":
            link = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip"

        elif uname.machine == "arm64":
            pass
            # ios or m1

        else:
            sys.stderr.write("Machine not supported")
            sys.exit()

    elif uname.system == "FreeBSD":
        pass

    else:
        sys.stderr.write("Machine not supported")
        sys.exit()

    if link:
        ngrok = urllib.request.urlopen(link).read()

        if link.endswith(".tgz"):
            tar_file = io.BytesIO(ngrok)
            binary = gzip.GzipFile(fileobj=tar_file)
            ngrok_file.write(binary.read())

        if link.endswith(".zip"):
            with zipfile.ZipFile(io.BytesIO(ngrok)) as zipped:
                for zipinfo in zipped.infolist():
                    with zipped.open(zipinfo) as binary:
                        ngrok_file.write(binary.read())

    ngrok_file.close()
    os.system("chmod +x ngrok") if uname.system != "Windows" else None


def expose_server():
    token_cmd = f"./ngrok authtoken {AUTHTOKEN} > /dev/null"
    ngrok_cmd = f"./ngrok tcp {PORT} --log=stdout > ngrok.log &"

    if uname.system == "Windows":
        ngrok_path = os.path.join(os.getcwd(), "ngrok.exe")
        token_cmd = f'"{ngrok_path}" authtoken {AUTHTOKEN} > nul'
        ngrok_cmd = f'"{ngrok_path}" tcp {PORT} --log=stdout > ngrok.log &'

    tries = 5
    os.system(token_cmd)
    ngrok_thread = threading.Thread(target=os.system, args=[ngrok_cmd])
    ngrok_thread.start()

    while tries != 0:
        try:
            url = json.loads(
                urllib.request.urlopen("http://localhost:4040/api/tunnels")
                .read()
                .decode("utf-8")
            )["tunnels"][0]["public_url"]
            url = url.replace("tcp://", "")
            return url.split(":")[0], url.split(":")[1]

        except Exception:
            time.sleep(1)
            tries -= 1

    raise Exception("Timeout")


if __name__ == "__main__":
    uname = platform.uname()
    python_exec = sys.executable

    if platform.system() == "Windows":
        pass

    file_dir = os.path.dirname(__file__)
    os.chdir(file_dir if file_dir != '' else '.')

    if not os.path.exists("ngrok"):
        get_ngrok()

    url, port = expose_server()
    secret = secrets.token_hex(nbytes=16)
    open("secret", "w").write(secret)
    tls_secret = "ee" + secret + TLS_DOMAIN.encode().hex()
    params = {"server": url, "port": port, "secret": tls_secret}
    params_encodeded = urllib.parse.urlencode(params, safe=":")
    tls_link = "tg://proxy?{}".format(params_encodeded)
    print(tls_link)

    if os.getenv("REPL_ID") or os.getenv("RUN_HTTP"):
        stay_alive()

    os.system(
        f"{sys.executable} mtprotoproxy.py > /dev/null 2>&1"
    ) if uname.system != "Windows" else subprocess.run(f"\"{python_exec}\" \"{file_dir+'/'+'mtprotoproxy.py'}\" > nul 2>&1", shell=True)
