"""Tests for the DummyEncoder model."""

import pytest
import torch

from src.models.encoder import DummyEncoder


class TestDummyEncoder:
    """Test suite for DummyEncoder."""
    
    def test_encoder_initialization(self):
        """Test that encoder initializes correctly."""
        encoder = DummyEncoder(input_dim=128, hidden_dim=64, output_dim=32)
        assert encoder.input_dim == 128
        assert encoder.hidden_dim == 64
        assert encoder.output_dim == 32
    
    def test_forward_pass(self):
        """Test forward pass produces correct output shape."""
        batch_size = 16
        input_dim = 128
        output_dim = 32
        
        encoder = DummyEncoder(input_dim=input_dim, output_dim=output_dim)
        x = torch.randn(batch_size, input_dim)
        output = encoder(x)
        
        assert output.shape == (batch_size, output_dim)
    
    def test_encode_batch(self):
        """Test batch encoding without gradients."""
        encoder = DummyEncoder(input_dim=128, output_dim=32)
        x = torch.randn(10, 128)
        
        output = encoder.encode_batch(x)
        
        assert output.shape == (10, 32)
        assert not output.requires_grad
    
    def test_get_embedding_dim(self):
        """Test getting embedding dimension."""
        output_dim = 32
        encoder = DummyEncoder(output_dim=output_dim)
        
        assert encoder.get_embedding_dim() == output_dim
    
    def test_get_model_info(self):
        """Test model info retrieval."""
        encoder = DummyEncoder()
        info = encoder.get_model_info()
        
        assert 'input_dim' in info
        assert 'hidden_dim' in info
        assert 'output_dim' in info
        assert 'num_layers' in info
        assert 'num_parameters' in info
        assert 'num_trainable_parameters' in info
        assert info['num_parameters'] > 0
