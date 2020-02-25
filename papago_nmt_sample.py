import requests

client_id = ""
client_secret = ""

url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"

text = "네이버 클라우드 플랫폼에서는 Clova, papago 등 네이버의 다양한 인공지능 서비스를 API 형태로 제공합니다. 고객은 네이버의 인공지능 서비스를 활용하여, " \
       "최신 기술 기반의 AI 서비스를 구축하고 안정적으로 운영할 수 있습니다.."

# ko : 한국어
# en : 영어
# zh-CN : 중국어 간체
# zh-TW : 중국어 번체
# es: 스페인어
# fr: 프랑스어
# vi: 베트남어
# th: 태국어
# id: 인도네시아어


val = {
    "source": 'ko',
    "target": 'zh-CN',
    "text": text
}

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}

response = requests.post(url,  data=val, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error : " + response.text)