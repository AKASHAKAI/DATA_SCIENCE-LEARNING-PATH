# NLP Review Cleaning Pipeline
import re

import pandas as pd
df=pd.read_csv(r"C:\MEGA\nlp_reviews_dataset.csv")
df
reviews=df["review_text"]
cleaned_reviews=[]
for review in reviews:
    review=str(review).lower().strip()
    review=re.findall(r'\w+',review)
    seen3=set()
    with_duplicates=[]
    for word in review:
        if word not in seen3:
            with_duplicates.append(word)
            seen3.add(word)
    cleaned_reviews.append(with_duplicates)
for i,review in enumerate(cleaned_reviews,start=1):
    print(f"Review {i}: {' '.join(review)}")