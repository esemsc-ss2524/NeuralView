# Load model directly
import torch
import torch.nn as nn
from transformers import BertTokenizer, BertModel


def load_transformer_model():
    model_name = "bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)
    
    return model, tokenizer

class SparseAutoencoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, sparsity_weight=0.01):
        super(SparseAutoencoder, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.sparsity_weight = sparsity_weight
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU()
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(hidden_dim, input_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded
    
    def sparsity_loss(self, encoded):
        # Regularize the sparsity using KL divergence
        mean_activation = encoded.mean(dim=0)
        sparsity_loss = torch.sum(torch.log(mean_activation / 0.05) * mean_activation)
        return self.sparsity_weight * sparsity_loss

def build_sparse_autoencoder(input_dim=784, hidden_dim=256, sparsity_weight=0.01):
    model = SparseAutoencoder(input_dim, hidden_dim, sparsity_weight)
    return model


    
