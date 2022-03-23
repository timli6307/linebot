from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from mykey import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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
    elif(event.message.text=='邏輯閘'):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/6/64/AND_ANSI.svg',
            title='邏輯閘種類',
            text='你說的是哪種呢?',
            actions=[
                # PostbackTemplateAction(
                #     label='postback',
                #     text='postback text',
                #     data='action=buy&itemid=1'
                # ),
                MessageTemplateAction(
                    label='及閘OR、或閘AND',
                    text='及閘OR、或閘AND'
                ),
                MessageTemplateAction(
                    label='反或閘NOR、反及閘NAND',
                    text='反或閘NOR、反及閘NAND'
                ),
                MessageTemplateAction(
                    label='互斥或XOR、互斥反或XNOR',
                    text='互斥或、互斥反或'
                ),
                
                # URITemplateAction(
                #     label='uri',
                #     uri='https://2.bp.blogspot.com/-H3JXh2cIKHs/WuwLvnz19cI/AAAAAAAAMXs/-qySdr5zEcc-kcLC4arf5m5H3F_trN7sgCK4BGAYYCw/s1600/kristopher-roller-110203-unsplash-m.jpg'
                # )
            ]
        )
        )
    elif(event.message.text=='互斥或、互斥反或'):
        message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
        text='互斥或XOR、互斥反或XNOR',
        actions=[
            # PostbackTemplateAction(
            #     label='postback',
            #     text='postback text',
            #     data='action=buy&itemid=1'
            # ),
            MessageTemplateAction(
                label='互斥或XOR',
                text='1'
            ),
            MessageTemplateAction(
                label='互斥反或XNOR',
                text='2'
            )
        ]
    )
    )
    elif(event.message.text=='及閘OR、或閘AND'):
        message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
        text='及閘OR、或閘AND',
        actions=[
            # PostbackTemplateAction(
            #     label='postback',
            #     text='postback text',
            #     data='action=buy&itemid=1'
            # ),
            MessageTemplateAction(
                label='及閘OR',
                text='message text'
            ),
            MessageTemplateAction(
                label='或閘AND',
                text='message text'
            )
        ]
    )
    )
    elif(event.message.text=='反或閘NOR、反及閘NAND'):
        message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
        text='反或閘NOR、反及閘NAND',
        actions=[
            # PostbackTemplateAction(
            #     label='postback',
            #     text='postback text',
            #     data='action=buy&itemid=1'
            # ),
            MessageTemplateAction(
                label='反或閘NOR',
                text='message text'
            ),
            MessageTemplateAction(
                label='反及閘NAND',
                text='message text'
            )
        ]
    )
    )
    elif(event.message.text=='布林代數'):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Hasse_diagram_of_powerset_of_3.svg/375px-Hasse_diagram_of_powerset_of_3.svg.png',
            title='布林代數種類',
            text='你說的是哪部分呢?',
            actions=[
                # PostbackTemplateAction(
                #     label='postback',
                #     text='postback text',
                #     data='action=buy&itemid=1'
                # ),
                MessageTemplateAction(
                    label='SOP、POS',
                    text='SOP、POS'
                ),
                MessageTemplateAction(
                    label='卡諾化簡',
                    text='卡諾化簡'
                )
            ]
        )
        )
    elif(event.message.text=='數字系統'):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Oudjat.SVG/360px-Oudjat.SVG.png',
            title='數字系統',
            text='數字系統分很多部分哦~',
            actions=[
                MessageTemplateAction(
                    label='各進制',
                    text='各進制'
                ),
                MessageTemplateAction(
                    label='特殊碼',
                    text='特殊碼'
                ),
                MessageTemplateAction(
                    label='補數',
                    text='補數'
                ),
                MessageTemplateAction(
                    label='溢位Overflow',
                    text='溢位Overflow'
                )
            ]
        )
        )
    elif(event.message.text=='第摩根定理'):
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.ytimg.com/vi/Qc_YfFc8iPA/maxresdefault.jpg',
            title='第摩根定理',
            text='分成兩個唷',
            actions=[
                MessageTemplateAction(
                    label='第摩根第一定理',
                    text='第摩根第一定理'
                ),
                MessageTemplateAction(
                    label='第摩根第二定理',
                    text='第摩根第二定理'
                )
            ]
        )
        )
    elif(event.message.text=='組合邏輯電路'):
        message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Half_Adder.svg/220px-Half_Adder.svg.png',
                    title='半加器、半減器',
                    text='半加器、半減器',
                    actions=[
                        MessageTemplateAction(
                            label='半加器',
                            text='半加器'
                        ),
                        MessageTemplateAction(
                            label='半減器',
                            text='半減器'
                        ),
                        URITemplateAction(
                            label='推薦自修網址',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Full-adder_logic_diagram.svg/440px-Full-adder_logic_diagram.svg.png',
                    title='全加器、全減器',
                    text='全加器、全減器',
                    actions=[
                        MessageTemplateAction(
                            label='全加器',
                            text='全加器'
                        ),
                        MessageTemplateAction(
                            label='全減器',
                            text='全減器'
                        ),
                        URITemplateAction(
                            label='推薦自修網址',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/1_bit_Decoder_2-to-4_line_zh_hant.svg/350px-1_bit_Decoder_2-to-4_line_zh_hant.svg.png',
                    title='解碼器、編碼器',
                    text='解碼器、編碼器',
                    actions=[
                        MessageTemplateAction(
                            label='解碼器',
                            text='解碼器'
                        ),
                        MessageTemplateAction(
                            label='編碼器',
                            text='編碼器'
                        ),
                        URITemplateAction(
                            label='推薦自修網址',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Demultiplexer.png/405px-Demultiplexer.png',
                    title='多工器、解多工器',
                    text='多工器、解多工器',
                    actions=[
                        MessageTemplateAction(
                            label='多工器',
                            text='多工器'
                        ),
                        MessageTemplateAction(
                            label='解多工器',
                            text='解多工器'
                        ),
                        URITemplateAction(
                            label='推薦自修網址',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/6/60/Zhdl.jpg',
                    title='比較器、可程式邏輯元件',
                    text='比較器、可程式邏輯元件',
                    actions=[
                        MessageTemplateAction(
                            label='比較器',
                            text='比較器'
                        ),
                        MessageTemplateAction(
                            label='可程式邏輯元件',
                            text='可程式邏輯元件'
                        ),
                        URITemplateAction(
                            label='推薦自修網址',
                            uri='http://example.com/1'
                        )
                    ]
                ),
            ]
        )
    )
    
    else:
        message = TextSendMessage(text=event.message.text + " --has sent")   
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    
