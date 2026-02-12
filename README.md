# Python Project

A Python project template with virtual environment setup.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project**
   ```bash
   python src/main.py
   ```

## Project Structure
```
.
├── src/                 # Source code
│   └── main.py         # Entry point
├── tests/              # Test files
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── venv/               # Virtual environment (created after setup)
```

## Development

### Adding Dependencies
1. Install the package: `pip install package-name`
2. Save to requirements: `pip freeze > requirements.txt`

### Running Tests
```bash
pytest tests/
```
