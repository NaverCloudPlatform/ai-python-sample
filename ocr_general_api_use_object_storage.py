import base64
import configparser
import json
import time

import boto3
import requests


class OCRTestSample:
    # 설정파일 읽기
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

    def req_message_send(self, idx, data, filename, fileformat):
        # ocr API Gateway url
        ep_path = self.config['OCR_GEN_API_CONFIG']['ep_path']
        # ocr secret key
        secret_key = self.config['OCR_GEN_API_CONFIG']['secret_key']

        timestamp = self.get_timestamp()
        request_body = {
            'version': 'V1',
            'requestId': 'test_ocr_for_obj_storage' + str(idx),
            'timestamp': str(timestamp),
            'lang': 'ko',
            'images': [{'format': fileformat, 'data': data, 'name': filename}]
        }

        ## Request body
        encode_request_body = json.dumps(request_body).encode('UTF-8')

        ## headers
        custom_headers = {
            'Content-Type': 'application/json;UTF-8',
            'X-OCR-SECRET': secret_key
        }

        #print("## Encode Request Body : ", encode_request_body)
        #print("## Timestamp : ", timestamp)
        #print("## headers ", custom_headers)
        #print("## request body : ", json.dumps(request_body))

        ## POST Request
        response = requests.post(headers=custom_headers, url=ep_path, data=encode_request_body)

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

    @property
    def get_file_list(self):
        # for connect object storage
        service_name = self.config['S3_CONFIG']['service_name']
        endpoint_url = self.config['S3_CONFIG']['endpoint_url']
        access_key = self.config['ACCOUNT_KEY_CONFIG']['access_key']
        secret_key = self.config['ACCOUNT_KEY_CONFIG']['secret_key']
        bucket_name = self.config['S3_CONFIG']['bucket_name']
        prefix = self.config['S3_CONFIG']['prefix']
        download_path = self.config['LOCAL_CONFIG']['download_path']

        # 1. s3 connect
        s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key)

        # 2. 대상 object storage에 접근
        # prefix는 object storage하위 폴더
        delimiter = '/'
        max_keys = 300
        response = s3.list_objects(Bucket=bucket_name, MaxKeys=max_keys, Prefix=prefix)

        file_list = []
        if not response.get('Contents'):
            return file_list

        # 3. 대상 파일 접근하여 local path에 download
        # local path의 파일 data를 API로 넘기기 위해 base64encoding
        # 파일정보를 담아 return
        file_list = []
        while True:
            print('IsTruncated=%r' % response.get('IsTruncated'))
            print('Marker=%s' % response.get('Marker'))
            print('NextMarker=%s' % response.get('NextMarker'))

            for content in response.get('Contents'):
                image_data = []
                if content.get('Size') > 0:
                    print(' Name=%s, Size=%d, Owner=%s' % \
                          (content.get('Key'), content.get('Size'), content.get('Owner').get('ID')))

                    if '/' not in content.get('Key'):
                        file_name = content.get('Key')
                    else:
                        file_name = content.get('Key').split('/')[len(content.get('Key').split('/'))-1]

                    local_file_path = download_path + file_name
                    s3.download_file(bucket_name, content.get('Key'), local_file_path)
                    data = self.fileToBase64(local_file_path)
                    #print('data ===> \n' +  data)

                    image_data.insert(0, data)
                    image_data.insert(1, file_name)
                    image_data.insert(2, file_name.split('.')[len(file_name.split('.'))-1])
                    file_list.append(image_data)

            if response.get('IsTruncated'):
                response = s3.list_objects(Bucket=bucket_name, Delimiter=delimiter, MaxKeys=max_keys,
                                           Marker=response.get('NextMarker'))
            else:
                break

        return file_list


if __name__ == '__main__':
    
    # 1. 비공개 object storage에 접근하여 대상 파일 데이터 추출
    file_list = OCRTestSample().get_file_list

    if not file_list:
        print("\n## There is no files or the prefix name is incorrect")
    else:
        # 2. 대상파일 loop돌며 CLOVA OCR API호출
        for idx, ocr_img in enumerate(file_list):
            start = time.time()
            res = OCRTestSample().req_message_send(idx, ocr_img[0], ocr_img[1], ocr_img[2])
            print(res.status_code)

            if (res.status_code == 200):
                data = json.loads(res.text)

                fields = data['images'][0]['fields']
                fields_len = len(fields)
                image_name = data['images'][0]['name']

                text = ""
                confidence = 0

                for result in fields:
                    inferText = result['inferText']
                    text += inferText
                    text += ' '
                    confidence += result['inferConfidence']

                print("\n## image_name : " + image_name)
                print("\n## result : " + text)
                if fields_len > 0:
                    print("\n## confidence " + str(confidence / fields_len))
                else:
                    print("\n## There is no texts")
                print("## time :", time.time() - start)

