import requests

client_id = ""
client_secret = ""

text = "네이버 클라우드 플랫폼은 다양한 AI 서비스를 API를 통해 제공 하고 있습니다."
#text = "NAVER CLOUD PLATFORM provides various AI services in API formats, such as Clova and Papago."
#text = "merry christmas is a season"
#text = "ネイバークラウドプラットフォームは、さまざまなAIサービスAPIを介して提供しています。"
#text = "Naver Cloud Platform通過API提供各種AI服務"
#text = "Naver Cloud Platform proporciona varios servicios de inteligencia artificial a través de la API."


# mijin : 한국어, 여성 음색
# jinho : 한국어, 남성 음색
# clara : 영어, 여성 음색
# matt : 영어, 남성 음색
# shinji : 일본어, 남성 음색
# meimei : 중국어, 여성 음색
# liangliang : 중국어, 남성 음색
# jose : 스페인어, 남성 음색
# carmen : 스페인어, 여성 음색


speaker = "jinho"
speed = "0"

val = {
    "speaker": speaker,
    "speed": speed,
    "text": text
}

url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}

response = requests.post(url,  data=val, headers=headers)
rescode = response.status_code

if(rescode == 200):
    print(rescode)
    with open('kr_sample_01.mp3', 'wb') as f:
        f.write(response.content)
else:
    print("Error : " + response.text)