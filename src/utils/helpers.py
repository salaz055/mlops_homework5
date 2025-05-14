# Helper functions can live here\

# Helper functions can live here
import pickle
import pandas as pd
import os
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
PATH_CSV = "/mlops_homework5/data/6000_all_categories_questions_with_excerpts.csv"
embedding_PICKLE_FILE = "data/embedding.pkl"
df_PICKLE_FILE = "data/df.pkl"

def data_loader():
    if os.path.exists(embedding_PICKLE_FILE) and os.path.exists(df_PICKLE_FILE):
        with open(df_PICKLE_FILE,"rb") as pf_df:
            df = pickle.load(pf_df)
        with open(embedding_PICKLE_FILE,"rb") as pf_em:
            embedding = pickle.load(pf_em)
    
    else:
        df = pd.read_csv(PATH_CSV)
        df = df.dropna(subset = ["wikipedia_excerpt"])
        df["embedding"] = [MODEL.encode(x) for x in df['wikipedia_excerpt'].to_list()]
        with open(embedding_PICKLE_FILE, "wb") as pf_em:
            pickle.dump(np.array(df["embedding"].to_list()), pf_em)
        with open(df_PICKLE_FILE, "wb") as pf_df:
            pickle.dump(np.array(df["embedding"].to_list()), pf_df)   
