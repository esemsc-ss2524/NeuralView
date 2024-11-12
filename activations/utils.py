def get_token_colors(tokens, model):
    # Mock activation levels based on token length or random values
    activations = [0.1, 0.5, 0.9]  # Placeholder, replace with real model-based activation
    colors = ["#ADD8E6", "#4682B4", "#00008B"]  # Light to dark blue

    return {token: color for token, color in zip(tokens, colors[:len(tokens)])}

def get_activation_distribution():
    # Mocked activation distribution
    return {"0%": 0.1, "25%": 0.3, "50%": 0.5, "75%": 0.8, "100%": 1.0}
