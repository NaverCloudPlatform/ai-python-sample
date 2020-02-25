import requests

client_id = ""
client_secret = ""

text = "네이버 클라우드 플랫폼은 다양한 AI 서비스를 API를 통해 제공 하고 있습니다."

speaker = "nara"
speed = "0"
pitch = "0"
emotion = "0"
format = "mp3"

val = {
    "speaker": speaker,
    "speed": speed,
    "text": text
}

url = "https://naveropenapi.apigw.ntruss.com/voice-premium/v1/tts"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(url,  data=val, headers=headers)
rescode = response.status_code

if(rescode == 200):
    print(rescode)
    with open('cpv_sample.mp3', 'wb') as f:
        f.write(response.content)
else:
    print("Error : " + response.text)