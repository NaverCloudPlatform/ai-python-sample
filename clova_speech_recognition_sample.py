import requests

client_id = "svcbyxyvfj"
client_secret = "DRcDAbaYNwi0jqBACwm8E1xl9LsHLHLsIGtuVynA"
lang = "Kor"    # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

data = open('./contents/hi.m4a', 'rb')
#data = open('./contents/news.mp3', 'rb')
#data = open('./contents/kr_book.mp3', 'rb')

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}

response = requests.post(url,  data=data, headers=headers)

rescode = response.status_code

if(rescode == 200):
    print(response.text)
else:
    print("Error : " + response.text)