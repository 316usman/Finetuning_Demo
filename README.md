# Finetuning_Demo
*This repository provides tools and resources for fine-tuning the LLaMA 2 language model to generate responses in a specific tone or style. Here we use 'Tapal Tea' Brand's data for this purpose. LLaMA 2 is a powerful open-source language model, capable of generating human-quality text in response to a wide range of prompts and questions. However, it can sometimes lack the ability to consistently maintain a specific tone or style in its responses. This repository aims to address this issue by providing a framework for fine-tuning LLaMA 2 on a dataset of text samples that exemplify the desired tone or style.*
<hr>
## 🧰 Languages and Tools:
<p align="center">

</p>

## Architecture:
This demo can be architecturally broen down into three main components or tasks
  * **1) Data Scraping / Cleaning**
  * **2) Fine-tuning**
  * **3) Evalutaion**

### Scraping
This project utilizes a combination of Puppeteer, Apify Facebook Scraper, and Apify Instagram Scraper to gather comprehensive data from a company's website, Facebook page, and Instagram account.

Prerequisites:

                                pip install pypuppteer
                                
#### <u>Scrape data from the company's website, follow these steps:</u>

  * Scrape tapal.com/home for potential links for data.
  * Save each link and extract text data for each page
  * Save the data of each page as a .txt file.

Run the 
  text_scrapper.py
file or see
  text_scrapper.ipynb
Notebook to get the scrapped data from Tapal's website. the data can be seen in the files folder of this repo.

#### <u>Clean data from the company's website, follow these steps:</u>

This step involves going through each file in the files folder and cleaning the data systematically.
Including
  * Removal of redundant tab spaces, newline characters.
  * Phone Numbers and or email addresses.
  * Because the files were scrapped each file had a footer that had Tapal's Head Office and Contact details.

Run the 
  cleaner.py
file or see
  cleaner.ipynb
Notebook to clean the data and store it in the cleaned_files folder.

#### <u>Scrape data from the Tapal's facebook and Instagram:</u>

I used Apify ready made scrappers to scrape the facebook and instagram pages of the company's website. 
Check:
https://apify.com/apify/facebook-pages-scraper
https://apify.com/apify/instagram-scraper
For details.

These scrappers take page links and scrape data according to set parameters. For this demo I scrapped 200 Facebook posts and 
783 Instagram posts. These scrappers ouptut JSON format files that contain many fields like url, likes etc but I used only the text for our use case.

#### <u>Combine all scraped data and convert into a 🤗 Dataset:</u>

🤗 Datasets is a library for easily accessing and sharing datasets for Audio, Computer Vision, and Natural Language Processing (NLP) tasks and makes dataprocessing very easir for our fine-tuning taks and is free to host as bog of a dataset you need for free.

Run the 
  dataset.py
file or see
 dataset.ipynb
Notebook to read all the data from .txt files and JSON files and convert these into a 🤗 dataset.

 * We obtained a total of **976** entries in our dataset and we split the data into a **90-10** Train and Test split.
 So we have **878** Training examples and **98** test examples.

 * We use **.push_to_hub('316usman/tapal_dataset_demo')** to push this data to the huggingface hub.
**Note this is a private dataset**
**Anything uploading / downlaoding to or from huggongface requires Access Tokesn**

## Fine-tuning:

**Pre-requisites**

     pip install -q accelerate==0.21.0 peft==0.4.0 bitsandbytes==0.40.2 transformers==4.31.0 trl==0.4.7 huggingface-hub datasets
Install the following dependencies before moving forward.

We use the QLoRA Technique to finetune the model for our use case. We use base model weights quantized to 4-bits and only the necessary layers, and attaching 'Adapters' that will learn our dataset.

Run the:
 Finetuning_Demo.ipynb
fine tune the model on our Tapal Dataset.

Some highlights of the file above are.
 * Install the requirements listed above

 * use **NousResearch/Llama-2-7b-chat-hf** as our base model from the huggingface hub.

 * load the base model in quantized form (4bit) using the bits and bytes library

 * Define a SFTTrainer Training Arguments

 * Start Fine-tuning the model

 * After finetuning reload the base model and merge its weights with the new trained adapters.

 * use **.push_to_hub("316usman/316usman/Llama-2-7b-chat-tapal-demo")** for later usage

We can now use this model to generate responses according to our tone

Use the 
 Finetuned_model_test.ipynb

to test the model and generate responses.

## Evaluation:

*Fine-tuning LLMs pose a unique challenge because their performance isn’t just a matter of accuracy; it’s about the value of the generated text. Traditional metrics such as loss or validation scores aren’t particularly insightful in these cases. More insightful metrics like perplexity and accuracy also fall short of providing a full performance picture, given that high confidence and correctness in predicting the next word don’t guarantee contextually appropriate or high-quality results.*

BLUE and ROUGE Scire are orignally meant for translation tasks but we can implement these to get an idea of model performance. The best metric is still human evaluation but for the sake f automation we need to settle on some metric that we can say with some what confidence 

#### Methodology

In this demo, we will employ a methodology novel. The focus of our evaluation lies in assessing the LLM's ability to generate coherent and contextually relevant text when presented with text segments split into half their original token length. To execute this methodology, we will begin by preparing a evaluation dataset by using the test part of our orignal tapal dataset. Following consistent tokenization with the method used during the model's training, each text row in the evaluation dataset will be split into segments, each containing half of the original token length. These segments will serve as input for the fine-tuned LLM during the evaluation setup, where the model will be tasked with generating the next words or tokens for each segment. 

To measure performance, we will utilize established metrics such as perplexity, BLEU score, and human assessment. Control variables, including a fixed random seed for reproducibility and the selection of a representative subset of the evaluation dataset, will be implemented. The evaluation process will be iterative, involving multiple runs with different subsets and potential fine-tuning iterations based on the results. The study will conclude with a summary of findings, potential areas for improvement, and an overall assessment of the fine-tuned LLM using the proposed half-token-length text splitting approach.
