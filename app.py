from flask import Flask, render_template, jsonify, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)

#load pickle files
model = pickle.load(open('model.pkl','rb'))
vectorizer = pickle.load(open('vect.pkl','rb'))

@app.route("/")

def Home():
    return render_template("index2.html")

@app.route("/predict", methods = ['POST'])

def predict():
    text = str(request.form['text'])
    text = [text]

    df = pd.DataFrame(index=[0])
    df['Message'] = text

    #removing stop words from the mail
    mail = ['Message']
    for i in mail:
        df[i] = df[i].apply(lambda x : x.replace(',', ' '))
        df[i] = df[i].apply(lambda x: x.replace('!',''))
        df[i] = df[i].apply(lambda x: x.replace('\r\n\r\n',' '))
        df[i] = df[i].apply(lambda x : x.replace('.', ' '))
        df[i] = df[i].apply(lambda x: x.replace('?',' '))
        df[i] = df[i].apply(lambda x: x.replace('/',' '))

    feature = vectorizer.transform(text)

    prediction = model.predict(feature)[0]
    if prediction == 0:
        prediction_text = "This email is Not Spam"
    else:
        prediction_text = "This email is Spam"
    
    return render_template("index2.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)