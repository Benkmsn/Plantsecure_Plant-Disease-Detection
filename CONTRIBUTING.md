# Contributing to PlantSecure

First off, thank you for considering contributing to PlantSecure! It's people like you that make PlantSecure such a great tool.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Include your environment details** (OS, Python version, browser)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Your First Code Contribution

Unsure where to begin? You can start by looking through `beginner` and `help-wanted` issues.

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Plantsecure_Plant-Disease-Detection.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it and install dependencies: `pip install -r requirements.txt`
5. Create a new branch: `git checkout -b feature/your-feature-name`

## Pull Request Process

1. **Update Documentation**: Ensure any new features are documented
2. **Update Requirements**: Add any new dependencies to requirements.txt
3. **Test Your Changes**: Make sure everything works as expected
4. **Follow Coding Standards**: See below
5. **Write Clear Commit Messages**: Use present tense ("Add feature" not "Added feature")
6. **Create the PR**: 
   - Provide a clear description of the changes
   - Reference any related issues
   - Include screenshots for UI changes

## Coding Standards

### Python Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Maximum line length: 100 characters

### Example:
```python
def detect_disease(image_path):
    """
    Detect plant disease from an image.
    
    Args:
        image_path (str): Path to the plant leaf image
        
    Returns:
        int: Index of the predicted disease class
    """
    # Implementation
    pass
```

### HTML/CSS/JavaScript
- Use consistent indentation (2 spaces)
- Add comments for complex logic
- Keep CSS organized by component
- Use semantic HTML elements

### Git Commit Messages
- Use present tense ("Add feature" not "Added feature")
- First line: brief summary (50 chars or less)
- Add detailed description if needed

Example:
```
Add disease prediction caching

- Implement Redis caching for repeated predictions
- Reduce API calls by 40%
- Add cache invalidation after 24 hours
```

## Questions?

Feel free to open an issue with your question or contact the maintainers directly.

Thank you for contributing! 🌿
