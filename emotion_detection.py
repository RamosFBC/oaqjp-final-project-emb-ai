import requests

def emotion_detector(text_to_analyse):
    
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": { "text": text_to_analyse } }

    r = requests.post(url=URL, headers=headers, json=input_json)
    r_json = r.json()
    text = r_json['emotionPredictions'][0]['emotionMentions'][0]['span']['text']
    
    return text