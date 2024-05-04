from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Load the trained model and vectorizer
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

app = Flask(__name__)

def preprocess_text(text):
    tokens = []
    if pd.isna(text):
        text = ''
    else:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        tokens = [token for token in tokens if token not in stopwords.words('english')]
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_text = request.form.get("input_text", "")
        preprocessed_text = preprocess_text(input_text)
        X = vectorizer.transform([preprocessed_text])
        prediction = model.predict(X)
        prediction_result = int(prediction[0])
        return jsonify({"prediction": prediction_result})
    except Exception as e:
        return jsonify({"error": "An error occurred while making the prediction."})

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
