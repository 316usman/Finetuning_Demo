# %%
from huggingface_hub import notebook_login
notebook_login()

# %%
from datasets import load_dataset
dataset = load_dataset("316usman/tapal_validation_dataset")

# %%
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
tfidf_vectorizer = TfidfVectorizer()
cosine_similarities = []

for i in range (len(dataset['train'])):
    text1 = dataset['train']['text'][i]
    text2 = dataset['train']['generated_text_1'][i]

    preprocessed_text1 = text1.lower().strip()
    preprocessed_text2 = text2.lower().strip()

    tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_text1, preprocessed_text2])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)[0, 1]
    cosine_similarities.append(cosine_sim)
    # Print the cosine similarity score
    print("Cosine similarity:", cosine_sim , "for text ", i)

# %%
print (dataset['train']['text'][25])
print (dataset['train']['generated_text_1'][25])

# %%
print (dataset['train']['text'][20])
print("************")
print (dataset['train']['generated_text_1'][20])

# %%
print (dataset['train']['text'][38])
print("************")
print (dataset['train']['generated_text_1'][38])

# %%
count = 0
for i in cosine_similarities:
    if i > 0.35:
        count += 1
print(count/len(cosine_similarities)* 100)

# %% [markdown]
# ## Rouge Score

# %%
from rouge_score import rouge_scorer
scorer = rouge_scorer.RougeScorer(['rouge1'])

# %%
for i in range(len(dataset['train'])):
    candidate = dataset['train']['text'][i]
    reference = dataset['train']['generated_text_2'][i]
    scores = scorer.score(reference, candidate)
    for key in scores:
        print(f'{key}: {scores[key]}')


