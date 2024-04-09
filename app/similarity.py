import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib


vectorizer = joblib.load('app/vectorizer/similarity_vectorizer.joblib')
df = pd.read_csv("app/dataset/sigma_v_1.csv")

def find_similar_problems(user_input):
    # Load the DataFrame
    df['Keywords'] = df['Keywords'].astype(str)
    # Preprocess text data
    df['Keywords'] = df['Keywords'].str.lower().str.split(',')
    df['Input'] = df['Input'].str.lower()
    df['Output'] = df['Output'].str.lower()

    # Convert user input to text
    user_input_text = ' '.join([
        user_input['Topic'].lower(), 
        user_input['Keywords'].lower(), 
        user_input['Input'].lower(), 
        user_input['Output'].lower()
    ])
    
    # Transform user input to vector
    user_vector = vectorizer.transform([user_input_text])
    text_data = df['Keywords'].apply(lambda x: ' '.join(x)) + ' ' + df['Input'] + ' ' + df['Output']
    tfidf_matrix = vectorizer.fit_transform(text_data)

    # Calculating similarity
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)

    # Getting indices of top 3 similar problems
    top_indices = similarity_scores.argsort()[0][-3:][::-1]

    # Getting top 3 similar problems and their IDs
    top_problems = {}
    for i, idx in enumerate(top_indices):
        problem_id = df.iloc[idx]['Id']
        sim_score = similarity_scores[0, idx] * 100  # Converting similarity score to percentage
        top_problems[f"problem_{i+1}"] = {
            "id": str(problem_id),
            "similarity_score": str(round(sim_score, 2))
        }
    
    return top_problems

