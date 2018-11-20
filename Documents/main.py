ReplyEndpoint ='https://api.line.me/v2/bot/message/reply'


def reply_text(reply_token,text):
       header={
                "Content-Type": "application/json",
                "Authorization": "Bearer{ENTER_ACCESS_TOKEN}"      
        }
       payload = {
           "replyToken":reply_token,
           "message":[
               {
                        "type": "text"
                        "text": text
                }

               ]

        }
       requests.post(ReplyEndpoint,headers=header,data=jason.dumps(payload))
