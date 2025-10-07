"""
Data loading and preprocessing package.

This module provides unified access to different dataset loaders
(e.g., OneStop, ZuCo) used throughout the eye-tracking + EEG pipeline.

Each loader follows the same interface defined in BaseDatasetLoader:
    - download()   → retrieves raw data
    - preprocess() → cleans and standardizes format
    - load()       → returns processed tensors or DataFrames
"""

from .base_loader import BaseDatasetLoader
from .onestop_loader import OneStopLoader
from .zuco_loader import ZucoLoader

# Registry for easy access
DATASET_LOADERS = {
    "onestop": OneStopLoader,
    "zuco": ZucoLoader,
}

__all__ = [
    "BaseDatasetLoader",
    "OneStopLoader",
    "ZucoLoader",
    "DATASET_LOADERS",
]
