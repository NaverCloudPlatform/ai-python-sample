import requests
client_id = ""
client_secret = ""

url = "https://naveropenapi.apigw.ntruss.com/vision-pose/v1/estimate"

files = {
    'image': open('./contents/golf_form.jpg', 'rb')
    #'image': open('./contents/iu.jpg', 'rb')
}

headers = {
    'X-NCP-APIGW-API-KEY-ID': client_id,
    'X-NCP-APIGW-API-KEY': client_secret
}

response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print("Error Code:" + rescode)