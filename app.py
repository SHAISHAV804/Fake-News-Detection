# from flask import Flask, render_template, request, jsonify
# from fake_news_classifier import model
# import pandas as pd
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# import string
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics import accuracy_score, confusion_matrix

# # Initialize Flask app
# app = Flask(__name__)

# # Initialize lemmatizer
# lemmatizer = WordNetLemmatizer()

# def preprocess_text(text):
#     tokens = []
#     if pd.isna(text):
#         text = ''
#     else:
#         text = text.lower()
#         text = text.translate(str.maketrans('', '', string.punctuation))
#         tokens = nltk.word_tokenize(text)
#         tokens = [token for token in tokens if token not in stopwords.words('english')]
#         tokens = [lemmatizer.lemmatize(token) for token in tokens]
#     return ' '.join(tokens)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the data from the POST request
#     data = request.get_json(force=True)
#     text = data['text']
    
#     # Preprocess the text
#     processed_text = preprocess_text(text)
    
#     # Vectorize the text
#     vectorizer = TfidfVectorizer()
#     X = vectorizer.fit_transform([processed_text])
    
#     # Make a prediction
#     prediction = model.predict(X)
    
#     # Return the prediction
#     return jsonify({'prediction': prediction[0]})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

