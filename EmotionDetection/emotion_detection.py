import requests
import json

def emotion_detector(text_to_analyse):  
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": { "text": text_to_analyse } }
    r = requests.post(url=URL, headers=HEADERS, json=input_json)
    
    if r.status_code == 400:
        output = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    else:
        r_dict = json.loads(r.text)
        output = {
            'anger': r_dict['emotionPredictions'][0]["emotion"]["anger"],
            'disgust': r_dict['emotionPredictions'][0]["emotion"]["disgust"],
            'fear': r_dict['emotionPredictions'][0]["emotion"]["fear"],
            'joy': r_dict['emotionPredictions'][0]["emotion"]["joy"],
            'sadness': r_dict['emotionPredictions'][0]["emotion"]["sadness"],
            }
        
        output['dominant_emotion'] = max(output, key=output.get)

    return output