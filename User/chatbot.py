import os
import string
import nltk
import joblib

from sklearn.metrics.pairwise import cosine_similarity
from django.conf import settings
from nltk.corpus import stopwords

MODEL_PATH = os.path.join(settings.BASE_DIR, 'Assets', 'Model')

stop_words = set(stopwords.words('english'))

def preprocess(text):

    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))

    words = nltk.word_tokenize(text)

    words = [w for w in words if w not in stop_words]

    return " ".join(words)


def predict_response(user_input):

    # 🔹 Load model every time (IMPORTANT)
    vectorizer = joblib.load(os.path.join(MODEL_PATH, "tfidf_vectorizer.pkl"))
    tfidf_matrix = joblib.load(os.path.join(MODEL_PATH, "tfidf_matrix.pkl"))
    answers = joblib.load(os.path.join(MODEL_PATH, "answers.pkl"))

    user_input = preprocess(user_input)

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, tfidf_matrix)

    index = similarity.argmax()

    score = similarity[0][index]

    if score < 0.3:
        return "Sorry, I didn't understand."

    return answers[index]