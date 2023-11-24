# main.py on feature_branch
from messaging import send_group_sms

if __name__ == "__main__":
    message = "New feature added in the feature_branch!"
    recipients = ["+1111111111", "+2222222222"]
    send_group_sms(message, recipients)