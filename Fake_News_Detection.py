import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

def load_data(file_path):
    """Load the dataset from a CSV file."""
    dataframe = pd.read_csv(file_path)
    return dataframe

def preprocess_text(text):
    """Preprocess the text data."""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    text = ' '.join(words)
    return text

def prepare_data(dataframe):
    """Prepare the data for training and testing."""
    x = dataframe['text']
    y = dataframe['label']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    return x_train, x_test, y_train, y_test

def vectorize_data(x_train, x_test):
    """Vectorize the text data using TF-IDF."""
    tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
    tfid_x_train = tfvect.fit_transform(x_train)
    tfid_x_test = tfvect.transform(x_test)
    return tfid_x_train, tfid_x_test

def train_model(tfid_x_train, y_train):
    """Train the PassiveAggressiveClassifier."""
    classifier = PassiveAggressiveClassifier(max_iter=50)
    classifier.fit(tfid_x_train, y_train)
    return classifier

def evaluate_model(classifier, tfid_x_test, y_test):
    """Evaluate the model's performance."""
    y_pred = classifier.predict(tfid_x_test)
    score = accuracy_score(y_test, y_pred)
    cf = confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
    print(f'Accuracy: {round(score * 100, 2)}%')
    print(classification_report(y_test, y_pred, target_names=['FAKE', 'REAL']))
    print(cf)

def save_model(classifier, file_path):
    """Save the trained model to a file."""
    with open(file_path, 'wb') as file:
        pickle.dump(classifier, file)

def load_model(file_path):
    """Load the saved model from a file."""
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def predict_news(news, classifier,tfvect):
    """Predict whether a news article is fake or real."""
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = classifier.predict(vectorized_input_data)
    return prediction

# Main execution
if __name__ == "_main_":
    file_path = 'news.csv'
    dataframe = load_data(file_path)
    # Preprocess the text data
    dataframe['text'] = dataframe['text'].apply(preprocess_text)
    x_train, x_test, y_train, y_test = prepare_data(dataframe)
    tfid_x_train, tfid_x_test = vectorize_data(x_train, x_test)
    classifier = train_model(tfid_x_train, y_train)
    evaluate_model(classifier, tfid_x_test, y_test)
    save_model(classifier, 'model.pkl')
    loaded_model = load_model('model.pkl')
    print(predict_news("Sample news article text here", loaded_model))