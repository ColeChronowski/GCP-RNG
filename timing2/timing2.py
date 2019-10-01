import requests
import time
import socket 

MAX_NUMBER = 1000000
MIN_NUMBER = 1

# Verify if the string is an integer or not
def verify_number(s):
    try:
        num = int(s)
        if num >= 1 & num <= 1000000:
            return s
    except ValueError:
        return "An error has ocurred"

def test_timing():
    with open(r'urls.txt') as file:
        for line in file:
            if not line.strip():
                continue
            flag = ""
            boy = line.split('@')[1].strip()
            if boy[0] != "h":
                boy = "http://"+boy #extremely hardy url correction. super futureproof
            start = time.time()
            try:
                r = requests.get(boy)
            except:
                flag = "bogus"
            end = time.time()
            print(socket.gethostbyname(socket.gethostname())+": "+line.strip(), str(end-start), verify_number(r.text + flag))
test_timing()
