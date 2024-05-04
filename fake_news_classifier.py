import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

# Load your data
data = pd.read_csv('testing_dataset.csv')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    # Initialize tokens as an empty list
    tokens = []
    
    # Check if the text is NaN and replace with an empty string if true
    if pd.isna(text):
        text = ''
    else:
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Tokenize
        tokens = nltk.word_tokenize(text)
        # Remove stopwords
        tokens = [token for token in tokens if token not in stopwords.words('english')]
        # Lemmatize
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into a single string
    return ' '.join(tokens)

# Apply preprocessing to both title and description
data['title'] = data['title'].apply(preprocess_text)
data['description'] = data['description'].apply(preprocess_text)

# Combine title and description into a single feature
data['combined_text'] = data['title'] + ' ' + data['description']

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the combined text
X = vectorizer.fit_transform(data['combined_text'])
y = data['Label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Initialize and train the Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# # debuging
# print(data['Label'].value_counts())
# importances = model.feature_importances_
# indices = np.argsort(importances)[::-1]

# # Print the feature ranking
# print("Feature ranking:")

# for f in range(X.shape[1]):
#     print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
# from sklearn.model_selection import cross_val_score

# scores = cross_val_score(model, X, y, cv=5)
# print("Cross-validation scores:", scores)
# print("Average cross-validation score:", scores.mean())

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save the model to a file
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as 'random_forest_model.pkl'")

# Save the TfidfVectorizer to a file
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

print("Vectorizer saved as 'vectorizer.pkl'")
