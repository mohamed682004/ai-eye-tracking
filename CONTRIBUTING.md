# Contributing to AI Eye Tracking

Thank you for your interest in contributing to the AI Eye Tracking project for dyslexia detection! 

## Code of Conduct

Please be respectful and constructive in all interactions. This is a research project aimed at helping people with dyslexia.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Relevant error messages or logs

### Suggesting Enhancements

For feature requests, please open an issue describing:
- The use case and motivation
- Proposed solution or API
- Any alternatives you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the guidelines below
3. **Add tests** for any new functionality
4. **Run the test suite** and ensure all tests pass
5. **Update documentation** if needed
6. **Submit a pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-eye-tracking.git
cd ai-eye-tracking

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov black flake8 isort mypy
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use descriptive variable names

### Code Formatting

Format your code before committing:

```bash
# Format with black
black src/ tests/

# Sort imports
isort src/ tests/

# Check for style issues
flake8 src/ tests/

# Type checking
mypy src/
```

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Update README.md for user-facing changes
- Add examples for new features

Example docstring:
```python
def my_function(param1: str, param2: int) -> bool:
    """
    Brief description of the function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: Description of when this error occurs
    """
    pass
```

## Testing

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Use descriptive test names: `test_<feature>_<scenario>`
- Group related tests in classes

Example test:
```python
import pytest
from src.models.encoder import DummyEncoder

class TestDummyEncoder:
    def test_forward_pass_shape(self):
        """Test that forward pass produces correct output shape."""
        encoder = DummyEncoder(input_dim=128, output_dim=32)
        x = torch.randn(16, 128)
        output = encoder(x)
        assert output.shape == (16, 32)
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_encoder.py -v

# Run specific test
pytest tests/test_encoder.py::TestDummyEncoder::test_forward_pass -v
```

### Test Coverage

- Aim for at least 80% code coverage
- Test edge cases and error conditions
- Test with different input sizes and types

## Commit Messages

Write clear, concise commit messages:

```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `style`: Code style changes (formatting)
- `chore`: Maintenance tasks

Example:
```
feat: Add LSTM encoder for sequential eye-tracking data

- Implement LSTMEncoder class with bidirectional support
- Add unit tests for LSTM encoder
- Update documentation with usage examples

Closes #42
```

## Project Structure Guidelines

### Adding New Modules

When adding new functionality:

1. **Data processing**: Add to `src/data/`
2. **Models**: Add to `src/models/`
3. **Training**: Add to `src/training/`
4. **Utilities**: Add to `src/utils/`

### Adding Dependencies

- Add core dependencies to `requirements.txt`
- Add development dependencies to `setup.py` under `extras_require`
- Pin versions for reproducibility

### Configuration

- Use YAML for configuration files in `configs/`
- Add configuration validation
- Document all configuration options

## Pull Request Process

1. **Update documentation** for any user-facing changes
2. **Add tests** and ensure they pass
3. **Update CHANGELOG** if applicable
4. **Ensure CI passes** (when set up)
5. **Request review** from maintainers
6. **Address feedback** promptly

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
```

## Review Process

- Maintainers will review PRs as soon as possible
- Address review comments and push updates
- Once approved, maintainers will merge the PR

## Questions?

Feel free to open an issue or reach out to maintainers if you have questions!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
