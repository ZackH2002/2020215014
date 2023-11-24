# main.py
from messaging import send_sms

if __name__ == "__main__":
    message = "Hello, this is a test message!"
    send_sms(message)
# new function