# %%
import os
import re
website_text = []

def text_cleaner(text):
    cleaned_text = re.sub(r'(\n{3,}|\t{3,}|\t)|\xa0', '', text)
    cleaned_text = re.sub(r' \n', '', cleaned_text)
    return (cleaned_text)

for file in os.listdir("C:\\Users\\Dell\\Desktop\\scrapper_tapal\\cleaned_files\\"):
    with open("C:\\Users\\Dell\\Desktop\\scrapper_tapal\\cleaned_files\\" + file, "r") as f:
        file_text = f.read()
        file_text = file_text.replace(" \n", "")
        website_text.append(text_cleaner(file_text))


# %%
website_text

# %%
import json
def load_json(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data

facebook_posts = load_json("C:\\Users\\Dell\\Desktop\\scrapper_tapal\\dataset_facebook-posts-scraper_2023-11-25_17-04-48-236.json")
instagram_posts = load_json("C:\\Users\\Dell\\Desktop\\scrapper_tapal\\dataset_instagram-scraper_2023-11-25_17-05-35-311.json")

facebook_posts_text = []
for post in facebook_posts:
    facebook_posts_text.append(post['text'])
instagram_posts_text = []
for post in instagram_posts:
    instagram_posts_text.append(post['caption'])

# %%
dataset_list = website_text + facebook_posts_text + instagram_posts_text
dataset_list = [item for item in dataset_list if item != '']

# %%
len(dataset_list)

# %%
from datasets import Dataset
dataset = Dataset.from_dict({'text':dataset_list})

# %%
from huggingface_hub import notebook_login
notebook_login()

# %%
dataset.push_to_hub("316usman/tapal_dataset")

# %%
from huggingface_hub import notebook_login
notebook_login()

# %%
from datasets import load_dataset
dataset = load_dataset("316usman/tapal_dataset")

# %%
dataset.shuffle()
dataset = dataset.train_test_split(test_size=0.1)
dataset.save_to_disk("test_dataset")


# %%
dataset

# %%
validation_set = dataset['test']

# %%
validation_set[]

# %%



