import json

import requests
url ='pass your meta url'


header = {
"Content-Type": "application/json",
'Authorization': <"Perment token">
}



def media(mobile_number):
    k = {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": mobile_number,
  "type": "template",
  "template": {
    "name": "lifeeazy_product_update",
    "language": {
      "code": "en"
    },
    "components": [

      {
        "type": "header",
        "parameters": [
          {
            "type": "image",
            "image": {
              "link": "https://media.licdn.com/dms/image/C5116AQHZAvAWQwNpSQ/profile-displaybackgroundimage-shrink_200_800/0/1517374088629?e=2147483647&v=beta&t=KYlVZJQ3ft7cITQfq4pSArpxxhZ4CQh2hv2jviJ61rM"
            }
          }
        ]
      },
    ]
  }
}
    x = requests.post(url=url,headers=header,json=k)
    print(x.json())
    return x.json()