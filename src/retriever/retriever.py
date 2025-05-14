import pickle
import pandas as pd
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.helpers import data_loader

MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
embedding_matrix_p = pickle.load("data/embedding.pkl")
df_PICKLE_FILE = pickle.load("data/df.pkl")

def get_similar_responses(question: str, top_k = 5) -> list:
    # TODO: Implement the logic to get the similar responses
    data_loader()
    embedding_matrix = pickle.load(embedding_matrix_p)
    df = pickle.load(df_PICKLE_FILE)
    question_encoding = MODEL.encode(question)
    similarity = cosine_similarity([question_encoding], embedding_matrix)
    top_k_responses = similarity.argsort()[top_k:]
    return df.iloc[top_k_responses]['wikipedia_excerpt'].to_list()
