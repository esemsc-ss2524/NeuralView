# def get_token_colors(tokens, model):

import torch
import numpy as np
from transformers import GPT2Model, GPT2Tokenizer

# Load GPT-2 model and tokenizer
model = GPT2Model.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def get_token_colors(tokens):
    # Tokenize input text and convert to PyTorch tensors
    inputs = tokenizer(tokens, return_tensors="pt", is_split_into_words=True)
    outputs = model(**inputs)

    # Extract hidden states (last layer) and calculate L2 norm for each token
    last_hidden_state = outputs.last_hidden_state.squeeze(0)  # Shape: (sequence_length, hidden_dim)
    activation_levels = last_hidden_state.norm(dim=1).tolist()  # Calculate L2 norm for each token

    # print(activation_levels)

    # Normalize activations to range [0, 1]
    min_activation = min(activation_levels)
    max_activation = max(activation_levels)
    normalized_activations = [
        (activation - min_activation) / (max_activation - min_activation)
        for activation in activation_levels
    ]

    # Define color thresholds and mapping logic
    colors = []
    for activation in normalized_activations:
        if activation < 0.5:
            colors.append("#ADD8E6")  # Light blue for low activations
        elif activation == 0.5:
            colors.append("#4682B4")  # Medium blue for moderate activations
        else:
            colors.append("#00008B")  # Dark blue for high activations

    # Map tokens to their color based on normalized activation level
    return {token: color for token, color in zip(tokens, colors)}


def get_activation_distribution():
    # Mocked activation distribution
    return {"0%": 0.1, "25%": 0.3, "50%": 0.5, "75%": 0.8, "100%": 1.0}
