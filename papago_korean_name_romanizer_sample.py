
import requests

client_id = ""
client_secret = ""

url = "https://naveropenapi.apigw.ntruss.com/krdict/v1/romanization?query=" + '허창현'

headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret
}

response = requests.get(url, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error : " + response.text)