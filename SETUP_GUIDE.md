# Setup Guide for AI Eye Tracking Project

## Overview

This repository has been set up as an MLOps-ready Python 3.10+ project for dyslexia detection via eye-tracking analysis.

## Repository Structure

### 📁 Core Directories

- **configs/**: Configuration files (YAML format) for experiments and model training
- **data/**: Data storage with three stages
  - `raw/`: Original, immutable datasets
  - `interim/`: Intermediate processed data
  - `processed/`: Final datasets ready for modeling
- **src/**: Main source code
  - `data/`: Data loading and processing modules
  - `models/`: Model architectures (PyTorch)
  - `training/`: Training loops and utilities
  - `utils/`: Helper functions (logging, etc.)
- **notebooks/**: Jupyter notebooks for exploration and analysis
- **scripts/**: Standalone scripts for training and inference
- **tests/**: Unit and integration tests
- **models/**: Saved model checkpoints and artifacts
- **docker/**: Docker configuration files
- **infra/**: Infrastructure as Code configurations

## Key Components

### 1. BaseDatasetLoader (`src/data/base_loader.py`)

Abstract base class for loading eye-tracking datasets with placeholder API methods:

```python
from src.data.base_loader import BaseDatasetLoader

class MyDataLoader(BaseDatasetLoader):
    def load_data(self, file_path: str):
        # Implement your loading logic
        pass

loader = MyDataLoader(data_dir="data/raw", api_key="your_key")
loader.download_dataset("dataset_id")
```

**Features:**
- Placeholder API download methods
- Data validation
- Data preprocessing hooks
- Extensible architecture

### 2. DummyEncoder (`src/models/encoder.py`)

PyTorch-based neural network encoder for feature extraction:

```python
from src.models.encoder import DummyEncoder
import torch

encoder = DummyEncoder(
    input_dim=128,
    hidden_dim=64,
    output_dim=32,
    num_layers=2,
    dropout=0.1
)

# Forward pass
x = torch.randn(16, 128)  # batch_size=16
output = encoder(x)  # shape: [16, 32]
```

**Features:**
- Configurable architecture
- Layer normalization
- Dropout for regularization
- Model info and metrics

### 3. Logger Utility (`src/utils/logger.py`)

Comprehensive logging system:

```python
from src.utils.logger import setup_logger

logger = setup_logger(
    name="experiment",
    level=logging.INFO,
    log_file="my_experiment.log"
)

logger.info("Experiment started")
logger.warning("This is a warning")
```

**Features:**
- Console and file logging
- Configurable log levels
- Context manager for temporary settings
- Automatic log directory creation

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/mohamed682004/ai-eye-tracking.git
cd ai-eye-tracking

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Tests

```bash
pytest tests/ -v
```

All 16 tests should pass with 85% code coverage.

### 3. Training Example

```bash
python scripts/train_model.py --config configs/config.yaml
```

### 4. Docker Setup

```bash
cd docker
docker-compose up --build
```

## Development Workflow

### 1. Data Preparation

1. Place raw data in `data/raw/`
2. Create a custom loader inheriting from `BaseDatasetLoader`
3. Implement data loading and preprocessing logic

### 2. Model Development

1. Create or modify models in `src/models/`
2. Use the provided `DummyEncoder` as a template
3. Add tests in `tests/`

### 3. Training

1. Update configuration in `configs/config.yaml`
2. Modify training script in `scripts/train_model.py`
3. Run training and monitor logs

### 4. Experimentation

1. Use Jupyter notebooks in `notebooks/`
2. Log experiments with the logger utility
3. Save models to `models/` directory

## Testing

The project includes comprehensive tests:

- `test_base_loader.py`: Tests for BaseDatasetLoader
- `test_encoder.py`: Tests for DummyEncoder
- `test_logger.py`: Tests for logger utility

Run tests with coverage:
```bash
pytest tests/ --cov=src --cov-report=html
```

## Configuration

Main configuration file: `configs/config.yaml`

Key sections:
- `project`: Project metadata
- `data`: Data paths and parameters
- `model`: Model architecture settings
- `training`: Training hyperparameters
- `logging`: Logging configuration

## MLOps Features

- ✅ Version control with Git
- ✅ Modular, testable code structure
- ✅ Comprehensive logging
- ✅ Configuration management
- ✅ Data versioning structure
- ✅ Model registry directory
- ✅ Docker support
- ✅ Infrastructure as Code support
- ✅ Test suite with good coverage

## Next Steps

1. **Implement Data Loading**: Extend `BaseDatasetLoader` with actual API integration
2. **Enhance Models**: Replace `DummyEncoder` with domain-specific architectures
3. **Add Training Logic**: Implement complete training loops in `src/training/`
4. **Set Up CI/CD**: Add GitHub Actions or similar in `infra/`
5. **Add Documentation**: Expand notebooks with data analysis and examples

## Troubleshooting

### Import Errors
Make sure you're in the project root and the virtual environment is activated:
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Test Failures
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Docker Issues
Make sure Docker and docker-compose are installed and running.

## Contributing

1. Create a feature branch
2. Make your changes
3. Add/update tests
4. Ensure all tests pass
5. Submit a pull request

## Support

For questions or issues:
- Open an issue on GitHub
- Check the documentation in `README.md`
- Review example notebook in `notebooks/01_exploration.ipynb`
