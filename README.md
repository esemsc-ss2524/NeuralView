# NeuralView

NeuralView is a Django-powered visualization tool designed for understanding and analyzing neural network models, with a specific focus on Sparse Autoencoders (SAEs) and Transformer-based models. The application includes features for visualizing token activations, attention mechanisms, and exploring connections within neural networks.

## Features

Model Management: Load and manage Sparse Autoencoders (SAEs) and Transformer models.  
Token Activation Visualization: Color text tokens based on neuron activations.  
Activation Distribution: Analyze activation distributions and quantiles.  
Attention Visualization: Explore attention weights through color-coded token backgrounds.  
Interactive Text Editing: View live activations as text is modified (under development).  
Crowdsourced Notes: Collaboratively annotate neurons for better analysis.

## Project Structure

NeuralView/  
├── manage.py             # Django management script  
├── NeuralView/           # Django project settings  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
├── models/               # Handles ML models and model loading  
│   ├── views.py          # Endpoint to load models  
│   ├── urls.py  
│   └── utils.py          # Helper functions for model loading  
├── activations/          # Processes neuron activations and distributions  
│   ├── views.py          # Token coloring, activation distribution  
│   ├── urls.py  
│   └── utils.py          # Helper functions for activations  
├── attention/            # Handles attention visualization  
│   ├── views.py          # Attention visualization endpoints  
│   ├── urls.py  
│   └── utils.py          # Helper functions for attention  
├── api/                  # Central API to route requests  
│   └── urls.py  
├── frontend/             # Simple HTML for frontend  
│   └── templates/  
│       └── index.html  
└── requirements.txt      # Project dependencies

## Setup Instructions

**Prerequisites:**

Python 3.x  
Virtual Environment (recommended): To isolate dependencies.

### Clone the Repository

    git clone https://github.com/yourusername/NeuralView.git
    cd NeuralView

### Set Up Virtual Environment

    python3 -m venv env
    source env/bin/activate  # On Windows use `.\env\Scripts\activate`

## Install Dependencies

    pip install -r requirements.txt

## Initialize the Django Application

Run migrations to set up the database:

    python manage.py migrate

## Start the Development Server

    python manage.py runserver

Access the app at http://127.0.0.1:8000/.

## Usage

Loading Models: Access the endpoint to load models to initialize Sparse Autoencoders and Transformers. (Detailed API endpoint below)

Visualize Token Activations: Retrieve token-level activations and color codes based on the neuron’s response to specific input texts.

Explore Attention Mechanisms: Hover over tokens to view attention weights or visualize connections between specific attention heads.

Quantile-based Text Exploration: Select texts based on activation levels across different quantiles.

API Endpoints  
Here are the key endpoints provided by NeuralView:  
- Model Management  
/api/load_models/ (POST): Initializes and loads the Sparse Autoencoder and Transformer models.  
- Activation Processing  
/api/token_activation_coloring/ (GET): Fetches token activations and colors based on specified inputs.  
/api/activation_distribution/ (GET): Provides distribution statistics for activations.  
/api/quantile_texts/ (GET): Retrieves texts corresponding to specific activation quantiles.  
- Attention Processing  
/api/attention_coloring/ (GET): Returns token coloring based on attention weights.  
/api/attention_hover/ (GET): Provides hover effects for selected attention heads.  

For details, please refer to the in-app API documentation or use tools like Postman to test each endpoint.  

Contributing  
We welcome contributions to improve NeuralView! Here’s how you can help:  
Fork the Repository: Create your own fork of NeuralView.  
Create a Feature Branch: Name your branch descriptively (e.g., feature/activation-distribution).  
Commit Your Changes: Write clear, concise commit messages.  
Push to GitHub: Push your feature branch to GitHub.  
Open a Pull Request: Describe your feature and any testing you performed.
