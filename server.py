from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyse = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyse)
    print(output)
    system_response = f'''
    For the given statement, the system response is
    'anger': {output['anger']},
    'disgust': {output['disgust']},
    'fear': {output['fear']},
    'joy': {output['joy']} and
    'sadness': {output['sadness']}.
    The dominant emotion is <strong>{output['dominant_emotion']}<strong>.
    '''
    return system_response


if __name__ == "__main__":
    app.run(debug=True)