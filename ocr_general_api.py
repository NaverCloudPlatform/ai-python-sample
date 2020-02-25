import hashlib
import hmac
import base64
import time
import requests
import json
from datetime import datetime
import base64

class OCRTestSample:

    # ocr API Gateway url
    ep_path = ''
    # ocr secret key
    secret_key = ''
    # IAM AccessKey
    access_key = ''

    def req_message_send(self):

        timestamp = self.get_timestamp()

        data =self.fileToBase64('./contents/ocr_sample_text.jpg')

        request_body = {

            'version': 'V1',
            'requestId': 'test_ocr_edueman',
            'timestamp': str(timestamp),
            'lang': 'ko',
            'images': [{ 'format': 'jpg', 'data': data,
                         'name':'korea_history'}]
            # 'images': [{ 'format': 'jpg', 'url': 'https://kr.object.ncloudstorage.com/labs/ocr/test_sample_03.jpg',
            #              'name':'korea_history'}]
        }

        ## Request body
        encode_request_body = json.dumps(request_body).encode('UTF-8')

        ## make signature
        signature = self.make_signature(self.secret_key, encode_request_body)

        ## headers
        custom_headers = {
            'Content-Type': 'application/json;UTF-8',
            'x-ncp-apigw-timestamp': str(timestamp),
            'x-ncp-iam-access-key': self.access_key,
            'X-OCR-SECRET': self.secret_key
        }

        print("## Encode Request Body : ", encode_request_body)
        print("## Timestamp : ", timestamp)
        print("## Signature : ", signature)
        print("## headers ", custom_headers)
        print("## request body : ", json.dumps(request_body))

        ## POST Request
        response = requests.post(headers=custom_headers, url=self.ep_path, data=encode_request_body)

        return response

    @staticmethod
    def fileToBase64(filepath):
        fp = open(filepath, "rb")
        data = fp.read()
        fp.close()
        return base64.b64encode(data).decode('utf-8')

    @staticmethod
    def get_timestamp():
        timestamp = int(time.time() * 1000)
        return timestamp

    @staticmethod
    def make_signature(access_key, request_body):

        secret_key_bytes = bytes(access_key, 'UTF-8')

        signing_key = base64.b64encode(hmac.new(secret_key_bytes, request_body, digestmod=hashlib.sha256).digest())

        return signing_key


if __name__ == '__main__':

    start = time.time()
    res = OCRTestSample().req_message_send()

    if(res.status_code == 200):
        data = json.loads(res.text)

        fields = data['images'][0]['fields']
        len = len(fields)

        text = ""
        confidence = 0

        for result in fields:
            inferText = result['inferText']
            text += inferText
            text += ' '
            confidence += result['inferConfidence']

        print("\n## result : " + text)
        print("\n## confidence " + str(confidence / len))

    print("## time :", time.time() - start)