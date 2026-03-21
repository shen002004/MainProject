import os
import django
import pandas as pd
import nltk
import string
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealEstate.settings')
django.setup()

from Admin.models import tbl_chatbot

nltk.download('punkt')
nltk.download('stopwords')


def preprocess(text):

    stop_words = set(stopwords.words('english'))

    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))

    words = nltk.word_tokenize(text)

    words = [w for w in words if w not in stop_words]

    return " ".join(words)


def train_chatbot():

    # 1️⃣ Export database to CSV
    data = tbl_chatbot.objects.all().values('question', 'answer')

    df = pd.DataFrame(list(data))

    df.to_csv("Assets/Model/chatbot_data.csv", index=False)

    print("CSV Exported")

    # 2️⃣ Load CSV
    df = pd.read_csv("Assets/Model/chatbot_data.csv")

    questions = df['question'].tolist()
    answers = df['answer'].tolist()

    print("Total Questions:", len(questions))

    # 3️⃣ Preprocess
    processed_questions = [preprocess(q) for q in questions]

    # 4️⃣ TF-IDF
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf_matrix = vectorizer.fit_transform(processed_questions)

    # 5️⃣ Save model
    joblib.dump(vectorizer, "Assets/Model/tfidf_vectorizer.pkl")
    joblib.dump(tfidf_matrix, "Assets/Model/tfidf_matrix.pkl")
    joblib.dump(answers, "Assets/Model/answers.pkl")

    print("Model Trained & Saved")


if __name__ == "__main__":
    train_chatbot()