from flask import Flask, render_template, jsonify, request
import numpy as np
import pickle

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
    feature = vectorizer.transform(text)

    prediction = model.predict(feature)[0]
    if prediction == 0:
        prediction_text = "This email is Not Spam"
    else:
        prediction_text = "This email is Spam"
    
    return render_template("index2.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)