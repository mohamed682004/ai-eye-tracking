# AI Eye Tracking for Dyslexia Detection

An MLOps-ready Python 3.10+ repository for detecting dyslexia through eye-tracking data analysis.

## 🎯 Project Overview

This project aims to leverage eye-tracking technology and machine learning to assist in dyslexia detection. The repository is structured following MLOps best practices for reproducible research and production deployment.

## 📁 Repository Structure

```
ai-eye-tracking/
├── configs/              # Configuration files for experiments and models
├── data/
│   ├── raw/             # Original, immutable data
│   ├── interim/         # Intermediate transformed data
│   └── processed/       # Final datasets for modeling
├── docker/              # Dockerfile and docker-compose configurations
├── infra/               # Infrastructure as Code (IaC) configurations
├── models/              # Trained model artifacts
├── notebooks/           # Jupyter notebooks for exploration and analysis
├── scripts/             # Utility scripts for data processing and training
├── src/
│   ├── data/           # Data loading and processing modules
│   ├── models/         # Model architectures and components
│   ├── training/       # Training loops and utilities
│   └── utils/          # Helper functions and utilities
└── tests/              # Unit and integration tests
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip or conda for package management
- (Optional) Docker for containerized deployment

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mohamed682004/ai-eye-tracking.git
cd ai-eye-tracking
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Data Loading

The project includes a `BaseDatasetLoader` class with placeholder API methods:

```python
from src.data.base_loader import BaseDatasetLoader

# Create a custom loader by inheriting from BaseDatasetLoader
class MyDataLoader(BaseDatasetLoader):
    def load_data(self, file_path: str):
        # Implement your data loading logic
        pass

# Use the loader
loader = MyDataLoader(data_dir="data/raw")
loader.download_dataset("my_dataset_id")
```

### Model Usage

A dummy PyTorch encoder is provided as a starting point:

```python
from src.models.encoder import DummyEncoder
import torch

# Initialize encoder
encoder = DummyEncoder(input_dim=128, hidden_dim=64, output_dim=32)

# Forward pass
input_data = torch.randn(16, 128)  # batch_size=16
encoded = encoder(input_data)

print(f"Output shape: {encoded.shape}")  # [16, 32]
```

### Logging

Use the built-in logger utility:

```python
from src.utils.logger import setup_logger, get_logger

# Setup logger
logger = setup_logger(
    name="my_experiment",
    level=logging.INFO,
    log_file="experiment.log"
)

logger.info("Starting experiment...")
logger.warning("This is a warning")
logger.error("This is an error")
```

## 🧪 Testing

Run tests using pytest:

```bash
pytest tests/
```

## 📊 MLOps Features

- **Version Control**: Git-based versioning for code and configurations
- **Modular Design**: Separation of concerns with clear module boundaries
- **Logging**: Comprehensive logging utilities for tracking experiments
- **Configuration Management**: Centralized configuration in `configs/`
- **Data Versioning**: Structured data storage (raw/interim/processed)
- **Model Registry**: Dedicated `models/` directory for model artifacts
- **Infrastructure**: IaC support in `infra/` for deployment
- **Containerization**: Docker support for reproducible environments

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Eye-tracking research community
- Dyslexia research organizations
- Open-source ML/DL frameworks

## 📧 Contact

For questions or collaboration opportunities, please open an issue or contact the maintainers.

---

**Note**: This is a research project under active development. The provided components (BaseDatasetLoader, DummyEncoder) are placeholders meant to be extended with actual implementation based on your specific use case.