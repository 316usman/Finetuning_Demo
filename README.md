# Finetuning_Demo
*This repository provides tools and resources for fine-tuning the LLaMA 2 language model to generate responses in a specific tone or style. LLaMA 2 is a powerful open-source language model, capable of generating human-quality text in response to a wide range of prompts and questions. However, it can sometimes lack the ability to consistently maintain a specific tone or style in its responses. This repository aims to address this issue by providing a framework for fine-tuning LLaMA 2 on a dataset of text samples that exemplify the desired tone or style.*
<hr>
## 🧰 Languages and Tools:
<p align="center">

</p>

## Architecture:
This demo can be architecturally broen down into three main components or tasks
  * **1) Data Scraping / Cleaning**
  * **2) Fine-tuning**
  * **3)Evalutaion**

### Scraping
This project utilizes a combination of Puppeteer, Apify Facebook Scraper, and Apify Instagram Scraper to gather comprehensive data from a company's website, Facebook page, and Instagram account.

Prerequisites:

                                pip install pypuppteer
                                
#### Scrape data from the company's website, follow these steps:

  * Scrape tapal.com/home for potential links for data.
  * Save each link and extract text data for each page
  * Save the data of each page as a .txt file.

Run the 
  text_scrapper.py
file or see
  text_scrapper.ipynb
Notebook to get the scrapped data from Tapal's website. the data can be seen in the files folder of this repo.

#### Clean data from the company's website, follow these steps:

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

#### Scrape data from the Tapal's facebook and Instagram:

I used Apify ready made scrappers to scrape the facebook and instagram pages of the company's website. 
Check:
https://apify.com/apify/facebook-pages-scraper
https://apify.com/apify/instagram-scraper
For details.

These scrappers take page links and scrape data according to set parameters. For this demo I scrapped 200 Facebook posts and 
783 Instagram posts. These scrappers ouptut JSON format files that contain many fields like url, likes etc but I used only the text for our use case.



