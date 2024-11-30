import torch
from transformers import GPT2Model, GPT2Tokenizer, GPT2LMHeadModel

# Load GPT-2 model and tokenizer
def load_gpt2_model():
    model = GPT2Model.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer

def load_gpt2_lm_head_model():
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer