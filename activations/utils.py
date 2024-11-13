# def get_token_colors(tokens, model):

import torch
import numpy as np
from transformers import GPT2Model, GPT2Tokenizer
from matplotlib import colors as mcolors

# Load GPT-2 model and tokenizer
model = GPT2Model.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def get_color_from_activation(activation):
    """
    Map a normalized activation value to a color on a gradient from light blue to dark blue.
    """
    # Define color range for gradient from light to dark blue
    color_start = np.array(mcolors.to_rgb("#ADD8E6"))  # Light blue
    color_mid = np.array(mcolors.to_rgb("#4682B4"))    # Medium blue
    color_end = np.array(mcolors.to_rgb("#00008B"))    # Dark blue

    # Define custom thresholds for smooth transitions
    if activation < 0.5:
        # Interpolate between light blue and medium blue
        blend_ratio = activation / 0.5
        color = (1 - blend_ratio) * color_start + blend_ratio * color_mid
    else:
        # Interpolate between medium blue and dark blue
        blend_ratio = (activation - 0.5) / 0.5
        color = (1 - blend_ratio) * color_mid + blend_ratio * color_end

    # Convert color back to hex
    return mcolors.to_hex(color)

def get_token_colors(tokens):
    # Tokenize input text and convert to PyTorch tensors
    inputs = tokenizer(tokens, return_tensors="pt", is_split_into_words=True)
    outputs = model(**inputs)

    # Extract hidden states (last layer) and calculate L2 norm for each token
    last_hidden_state = outputs.last_hidden_state.squeeze(0)  # Shape: (sequence_length, hidden_dim)
    activation_levels = last_hidden_state.norm(dim=1).tolist()  # Calculate L2 norm for each token

    # Normalize activations to range [0, 1]
    min_activation = min(activation_levels)
    max_activation = max(activation_levels)
    normalized_activations = [
        (activation - min_activation) / (max_activation - min_activation)
        for activation in activation_levels
    ]

    # Map each normalized activation to a color using the gradient
    colors = [get_color_from_activation(activation) for activation in normalized_activations]

    # Map tokens to their color based on normalized activation level
    return {token: color for token, color in zip(tokens, colors)}

def get_activation_distribution():
    # Mocked activation distribution
    return {"0%": 0.1, "25%": 0.3, "50%": 0.5, "75%": 0.8, "100%": 1.0}
