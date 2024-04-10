import time

proxies = {
    "proxy1": "http://username1:password1@proxy1:port",
    "proxy2": "http://username2:password2@proxy2:port",
}


def start_time():
    start_time = time.time()
    return start_time


def end_time():
    end_time = time.time()
    return end_time
