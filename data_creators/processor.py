import pandas as pd
import re
from pathlib import Path
STOPWORDS = {'the', 'and', 'is', 'in', 'to', 'of', 'a', 'that', 'it', 'with', 'for', 'as', 'was', 'on', 'are', 'by', 'this', 'be', 'or', 'from', 'at', 'an', 'have', 'which', 'has'}


def process_db(df: pd.DataFrame, name: str, filter: bool = True) -> pd.DataFrame:
    df["text_length"] = df["text"].str.len()
    if filter:
        df['text'] = df['text'].str.replace('\xa0', ' ')
        df['text'] = df['text'].str.split(r'\n+', regex=True)
        df = df.explode('text')
        df = df[df['text'].apply(is_actual_prose)].reset_index(drop=True)
    output_dir = Path("../.idea/data/processed_dbs").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = str(output_dir / f"{name}.parquet")
    print(f"Writing {output_path}")
    df.to_parquet(output_path, engine='pyarrow')
    print(f"Successfully saved to: {output_path}")
    return df


def is_actual_prose(text):
    if not isinstance(text, str):
        return False
    text = text.strip()
    if len(text) < 15:
        return False
    noise_chars = len(re.findall(r'[\d_\%\×\=\+\<\>\|\-\/]', text))
    if (noise_chars / len(text)) > 0.15:
        return False
    words = set(re.findall(r'\b[a-zA-Z]+\b', text.lower()))
    stopword_count = len(words.intersection(STOPWORDS))
    if stopword_count < 2:
        return False
    return True
import os
from pathlib import Path