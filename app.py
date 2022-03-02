from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('gBWrPRQ566OyyBtLOdju/+Z8zLVlcgLQSyscIOK/FpTDHaLwSQEW9eM18NO21W0CayDjdspZG2V1VEPKv1AV13GL+gDnYtnA55RGmKa8tDcfn1275fKVGc9rbDcUjfcuQXWOZrezGDy+wjiCZ2npSgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a8426128cfa59102dd82778ffbd2244c')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if(event.message.text=='pic'):
        message=ImageSendMessage(
        original_content_url='https://2.bp.blogspot.com/-H3JXh2cIKHs/WuwLvnz19cI/AAAAAAAAMXs/-qySdr5zEcc-kcLC4arf5m5H3F_trN7sgCK4BGAYYCw/s1600/kristopher-roller-110203-unsplash-m.jpg',
        preview_image_url='https://2.bp.blogspot.com/-H3JXh2cIKHs/WuwLvnz19cI/AAAAAAAAMXs/-qySdr5zEcc-kcLC4arf5m5H3F_trN7sgCK4BGAYYCw/s1600/kristopher-roller-110203-unsplash-m.jpg'
        )
    elif(event.message.text=='Button'):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://2.bp.blogspot.com/-H3JXh2cIKHs/WuwLvnz19cI/AAAAAAAAMXs/-qySdr5zEcc-kcLC4arf5m5H3F_trN7sgCK4BGAYYCw/s1600/kristopher-roller-110203-unsplash-m.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                ),
                URITemplateAction(
                    label='uri',
                    uri='https://2.bp.blogspot.com/-H3JXh2cIKHs/WuwLvnz19cI/AAAAAAAAMXs/-qySdr5zEcc-kcLC4arf5m5H3F_trN7sgCK4BGAYYCw/s1600/kristopher-roller-110203-unsplash-m.jpg'
                )
            ]
        )
        )
    else:
        message = TextSendMessage(text=event.message.text + " --By Miller")   
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
