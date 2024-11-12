# Contributing to Treecraft

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/treecraft.git
   cd treecraft
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # or `env\Scripts\activate` on Windows
   ```
4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```

## Running Tests
```bash
pytest tests/
```

## Making Changes
1. Create a new branch
2. Make your changes
3. Run tests
4. Submit a pull request

## Release Process
1. Update version in `src/treecraft/__init__.py` and `setup.py`
2. Update CHANGELOG.md
3. Create a new GitHub release
4. GitHub Actions will automatically publish to PyPI