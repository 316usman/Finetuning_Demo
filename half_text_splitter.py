# %%
from transformers import AutoTokenizer
model_name = "NousResearch/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

# %%
def half_text_splitter(text, tokenizer):
    encoded_text = tokenizer(text, return_tensors="pt")
    input_ids_length = len(encoded_text["input_ids"][0])
    halfway_point = input_ids_length // 2
    first_half_input_ids = encoded_text["input_ids"][0][:halfway_point]
    decoded_text = tokenizer.decode(first_half_input_ids)
    return (decoded_text)

# %%
text = "This is a text that is going to be split into two halves. This is the first half"
half_text_splitter(text, tokenizer)

# %%
half_text = []
for item in validation_set:
    half_text.append(half_text_splitter(item['text'], tokenizer))

# %%
validation_set = validation_set.add_column("half_text", half_text)

# %%
validation_set.push_to_hub('316usman/tapal_validation_dataset')


