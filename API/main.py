from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json

import lightgbm as lgb
from lightgbm import LGBMClassifier

app = Flask(__name__)


@app.route('/api/', methods=['GET', 'POST'])


def makecalc():
    data = request.get_json()
    if model.predict(data) < 0.5:
        prediction = 'died'
    else:
        prediction = 'survived'
    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'final_prediction.pickle'
    #model = joblib.load(modelfile)
    model = lgb.Booster(model_file='mode.txt')
    app.run(debug=True, host='0.0.0.0')