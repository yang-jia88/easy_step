import os, sys
import json
from flask import Flask, request
from pymessenger import bot
#https://github.com/davidchua/pymessenger
app = Flask(__name__)
PAGE_ACCESS_TOKEN = "EAAN4Y7IBpgEBADV6QbT64HGFmDgZBnJuaZAevORymsRujpU9ZB3wuGSZBJ9TrPABDw1oMFBb5pM2Ecvg9eUWUgx0A8fDph00kGM9RjrTPLJuanzEVYMDgsizKpmmX1fZChHbt8gT9B96QvCdgShjpMDL6twZBlQrkKFGrgZC6jnSQnW1AvjRlRO"
num1={"A":"營業時間","B":"連絡電話","C":"營業地址"}
str1="可以輸入以下代碼查詢資料A:營業時間,B:連絡電話,C:營業地址"

@app.route('/', methods=['GET'])
def verify():
 # Webhook verification
    print(request.args)
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "1227":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(data)
    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']
                if 'message' in messaging_event:
                     # Extracting text message
                    if 'text' in messaging_event['message']:
                        text=messaging_event['message']['text']
                        print("ID:%s,Text:%s"%(messaging_event['sender']['id'],text))
                        if text=="A" or text=="B" or text=="C":
                            bot.send_text_message(sender_id,num1[text])
                        else:
                            bot.send_text_message(sender_id,"測試")
                return "ok", 200
def log(message):
    print(message)
    sys.stdout.flush()
if __name__ == "__main__":
    app.run(debug = 0, port = 2000)