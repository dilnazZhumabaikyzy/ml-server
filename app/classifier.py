import joblib
import pandas as pd
directory = "app/"

model_input = joblib.load(directory + "models/updated/input_classifier.joblib")
model_output =  joblib.load(directory + "models/updated/output_classifier.joblib")
model_difficulty = joblib.load(directory + "models/difficulty_classifier.joblib")
model_topics = joblib.load(directory + "models/updated/topics_classifier.pkl")
keywords_extractor = joblib.load(directory + "models/keywords_extractor.pkl")
keywords_decode = joblib.load(directory + "models/keywords_decode.pkl")

tfidf_vectorizer = joblib.load(directory + "vectorizer/tfidf_vectorizer_beta.joblib")
tfidf_vectorizer_sigma = joblib.load(directory + "vectorizer/sigma_vectorizer.pkl")


directory_binary = directory + "models/binary_classifications/"
model_1 = joblib.load(directory_binary + "1.joblib")
model_2 = joblib.load(directory_binary + "2.joblib")
model_3 = joblib.load(directory_binary + "3.joblib")
model_4 = joblib.load(directory_binary + "4.joblib")
model_5 = joblib.load(directory_binary + "5.joblib")

def predict_five_features(user_input):
    user_input_vectorized = tfidf_vectorizer.transform([user_input])
    
    prediction_1 = int(model_1.predict(user_input_vectorized)[0])
    prediction_2 = int(model_2.predict(user_input_vectorized)[0])
    prediction_3 = int(model_3.predict(user_input_vectorized)[0])
    prediction_4 = int(model_4.predict(user_input_vectorized)[0])
    prediction_5 = int(model_5.predict(user_input_vectorized)[0])

    return [prediction_1, prediction_2, prediction_3, prediction_4, prediction_5]


def predict_input(user_input):
    user_input_vectorized = tfidf_vectorizer.transform([user_input])
    prediction = model_input.predict(user_input_vectorized)[0]

    return prediction

def predict_output(user_input):
    user_input_vectorized = tfidf_vectorizer.transform([user_input])
    prediction = model_output.predict(user_input_vectorized)[0]

    return prediction

def predict_topic(user_input):
    user_input_vectorized = tfidf_vectorizer_sigma.transform([user_input])
    prediction = model_topics.predict(user_input_vectorized)[0]

    return prediction


def predict_difficulty(user_input):
    user_input_vectorized = tfidf_vectorizer.transform([user_input])
    prediction = model_difficulty.predict(user_input_vectorized)[0]

    return prediction

def extract_keywords(user_input):
    user_input_vectorized = tfidf_vectorizer.transform([user_input])
    predicted_keywords = keywords_decode.inverse_transform(keywords_extractor.predict(user_input_vectorized))
    

    return predicted_keywords

def classify_all(user_input):  
    predictions = {}

    predictions['input'] = predict_input(user_input)
    predictions['output'] = predict_output(user_input)
    predictions['topic'] = predict_topic(user_input)
    predictions['difficulty'] = predict_difficulty(user_input)
    predictions['keywords'] = extract_keywords(user_input)
    predictions['binary'] = predict_five_features(user_input)

    return predictions

