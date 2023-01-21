import requests
import time

# Replace YOUR_BOT_TOKEN with the actual token of your bot
bot_token = "YOUR_BOT_TOKEN"

# Replace YOUR_CHAT_ID with the actual chat ID of the group you want to send the message to
group_chat_id = "YOUR_CHAT_ID"

def send_message(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": group_chat_id, "text": text}
    requests.post(url, json=payload)

def job():
    # Replace this with the text of the message you want to send
    text = "Hello World!"
    send_message(text)

while True:
    job()
    time.sleep(10)
