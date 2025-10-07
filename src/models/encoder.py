"""Dummy PyTorch encoder for eye-tracking data."""

import torch
import torch.nn as nn
from typing import Tuple


class DummyEncoder(nn.Module):
    """
    Dummy encoder for eye-tracking feature extraction.
    
    This is a simple placeholder architecture that can be replaced
    with more sophisticated models as the project evolves.
    """
    
    def __init__(
        self,
        input_dim: int = 128,
        hidden_dim: int = 64,
        output_dim: int = 32,
        num_layers: int = 2,
        dropout: float = 0.1
    ):
        """
        Initialize the dummy encoder.
        
        Args:
            input_dim: Dimension of input features
            hidden_dim: Dimension of hidden layers
            output_dim: Dimension of encoded output
            num_layers: Number of encoding layers
            dropout: Dropout probability
        """
        super(DummyEncoder, self).__init__()
        
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.num_layers = num_layers
        
        # Build encoder layers
        layers = []
        current_dim = input_dim
        
        for i in range(num_layers):
            next_dim = hidden_dim if i < num_layers - 1 else output_dim
            layers.extend([
                nn.Linear(current_dim, next_dim),
                nn.ReLU(),
                nn.Dropout(dropout)
            ])
            current_dim = next_dim
        
        # Remove last dropout layer
        layers = layers[:-1]
        
        self.encoder = nn.Sequential(*layers)
        
        # Layer normalization for stable training
        self.layer_norm = nn.LayerNorm(output_dim)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass through the encoder.
        
        Args:
            x: Input tensor of shape (batch_size, input_dim)
            
        Returns:
            Encoded tensor of shape (batch_size, output_dim)
        """
        encoded = self.encoder(x)
        normalized = self.layer_norm(encoded)
        return normalized
    
    def get_embedding_dim(self) -> int:
        """
        Get the output embedding dimension.
        
        Returns:
            Output dimension of the encoder
        """
        return self.output_dim
    
    def encode_batch(self, x: torch.Tensor) -> torch.Tensor:
        """
        Encode a batch of inputs with no gradient computation.
        
        Args:
            x: Input tensor of shape (batch_size, input_dim)
            
        Returns:
            Encoded tensor of shape (batch_size, output_dim)
        """
        with torch.no_grad():
            return self.forward(x)
    
    def get_model_info(self) -> dict:
        """
        Get model configuration information.
        
        Returns:
            Dictionary with model configuration
        """
        return {
            "input_dim": self.input_dim,
            "hidden_dim": self.hidden_dim,
            "output_dim": self.output_dim,
            "num_layers": self.num_layers,
            "num_parameters": sum(p.numel() for p in self.parameters()),
            "num_trainable_parameters": sum(p.numel() for p in self.parameters() if p.requires_grad)
        }


if __name__ == "__main__":
    # Example usage
    encoder = DummyEncoder(input_dim=128, hidden_dim=64, output_dim=32)
    print("Model Info:", encoder.get_model_info())
    
    # Test forward pass
    batch_size = 16
    dummy_input = torch.randn(batch_size, 128)
    output = encoder(dummy_input)
    print(f"Input shape: {dummy_input.shape}")
    print(f"Output shape: {output.shape}")
