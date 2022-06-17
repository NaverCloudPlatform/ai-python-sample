# ai-python-sample-1.0

**네이버클라우드플랫폼 AI 상품**을 쉽게 사용하기 위한, Python 샘플소스를 제공 합니다. 

## AI API 샘플
* chatbot_custom_api.py : 웹서비스 및 모바일 앱등에서 사용할 수 있는 Chatbot Custom API
* clova_face_recognition_sample.py : 얼굴과 관련된 다양한 정보를 제공하는 얼굴 인식 API
* clova_premium_voice_sample.py : 자연스러운 합성음을 제공하는 CPV API
* clova_speech_recognition_sample.py : 가장 뛰어난 한국어 음석 인식률을 가진 음석 인식 API
* clova_speech_synthesis_sample.py : 텍스트를 음성으로 변환해주는 음성 합성 API
* object_detection_sample.py : 이미지 속 객체를 탐지하고 위치 식별을 위한 API
* ocr_general_api.py : 이미지를 텍스트로 변환할 수 있는 API
* ocr_general_api_use_object_storage.py : 비공개 object storage의 이미지를 텍스트로 변환할 수 있는 API (python boto3 install필요)
* papago_korean_name_romanizer_sample.py : 한국 인명 로마자 변환 API
* papago_language_detection_sample.py : 언어의 종류를 감지할 수 있는 API
* papago_nmt_sample.py : 가장 뛰어난 한국어 번역 품질을 제공하는 인공 신경망기반 기계 번역 API
* pose_estimation_sample.py : 주요 신체 영역을 인식하여 좌표 정보를 제공하는 포즈 인식 API

## 관련 API 참조서

* Clova Speech Synthesis(CSS) : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/clova_speech_synthesis/tts/)
* Clova Speech Recognition(CSR) : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/clova_speech_recognition/stt/)
* Clova Premium Voice(CPV) : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/clova_premium_voice/)
* Clova Face Recognition(CFR) : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/clova_face_recognition/)
* Papago NMT : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/papago_nmt/translation/)
* Papago Language Detection : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/papago_language_detection/)
* Papago Korean Name Romanizer : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/papago_korean_name_romanizer/)
* Chatbot Custom API : [API 참조서](https://apidocs.ncloud.com/ko/ai-application-service/chatbot/)
* Object Detection : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/object_detection/object/)
* Pose Estimation : [API 참조서](https://apidocs.ncloud.com/ko/ai-naver/pose_estimation/)

## 참고사항

* Chatbot Custom API 와 OCR General API를 제외한 AI API는 네이버클라우드플랫폼의 AI NAVER API 메뉴에서 Application 등록을 해야 합니다.
등록후에 인증정보를 확인 할 수 있고, 해당 인증정보를 통해 샘플소스에 있는 client_id, Client_Secret 값을 변경해야 합니다. [설명서](https://docs.ncloud.com/ko/naveropenapi_v3/application.html)
* Chatbot Custom API는 대화 목록에 대화가 생성이 되어 있어야 하며, 대화 모델 빌드까지 끝난 상태에서 "챗봇 설정" > "메신저 연동" > "Custom"을 통해 API Gateway URL을 통해 호출하게 됩니다. 인증정보는 네이버클라우드플랫폼의 서비스 계정 또는 SubAccount의 AccessKey, AccessSecret가 필요 합니다.
[설명서](https://docs.ncloud.com/ko/chatbot/chatbot-2-5.html)
* OCR General API는 이미지에 있는 모든 텍스트를 추출하는 API 입니다. 인증정보는 네이버클라우드플랫폼의 서비스 계정 또는 SubAccount의 AccessKey, AccessSecret가 필요 합니다. [설명서](https://docs.ncloud.com/ko/ocr/ocr-1-2.html)



