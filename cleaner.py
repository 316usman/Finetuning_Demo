# %%
import re
import os

# %%
def clean_text(input_file):
    with open(input_file, 'r') as infile:
        content = infile.read()
    content = content.replace('     \n', '')
    cleaned_content = re.sub(r'\n{2,}', '\n', content)
    cleaned_content = re.sub(r'Head Office[\s\S]*$', '', cleaned_content)
    cleaned_content = re.sub(r'\b\d{1,3}[-.]?\d{1,3}[-.]?\d{1,5}\b', '', cleaned_content)
    cleaned_content = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', cleaned_content)
    
    with open('C:\\Users\\Dell\\Desktop\\scrapper_tapal\\cleaned_files\\' + input_file, 'w') as outfile:
        outfile.write(cleaned_content)

# %%
for file in os.listdir('C:\\Users\\Dell\\Desktop\\scrapper_tapal\\'):
    if file.endswith('.txt'):
        print (file)
        clean_text(file)

# %%



