import requests
import json

def emotion_detector(text_to_analyse):
    url = '<URL endpoint Watson NLP Emotion Predict mà bài lab cung cấp>'
    headers = {"grpc-metadata-mm-model-id": "<model id mà bài lab cung cấp>"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=input_json, headers=headers)
    # Task 2 chỉ cần in/trả về kết quả thô để kiểm tra hoạt động đúng
    return response.text
