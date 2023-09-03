from app import app
from flask import request
from polyglot.detect import Detector
import json
from polyglot.text import Text
@app.route('/predict',methods=['POST'])
def predict():
    text=request.form['text']
    result = {}
    try:
        str = text
        text = Text(str)
        detector = Detector(str)
        result["lang"] = detector.language.code
        result["lang_str"] = detector.language.name
        sum = 0
        for w in text.words:
            sum = sum + w.polarity
        if sum > 0:
            result['polarity'] = 1
        elif sum < 0:
            result['polarity'] = -1
        else:
            result['polarity'] = 0
        first_sentence = text.sentences[0]
        if sum != 0 and len(first_sentence.entities) > 0:
            first_entity = first_sentence.entities[0]
            if first_entity.positive_sentiment > first_entity.negative_sentiment:
                result['subjectivity'] = first_entity.positive_sentiment
            else:
                result['subjectivity'] = first_entity.negative_sentiment
        else:
            result['subjectivity'] = 0
        result['sentence'] = str
        result['ps_rating'] = (result['polarity'] + result['subjectivity']) / 2
    except:
        result["message"] = "system error"
    return json.dumps(result)
