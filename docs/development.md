# Development Guide

## Setting Up Development Environment

1. Clone the repository:

```zsh
git clone https://github.com/yourusername/ratchada_utils.git
cd ratchada_utils
```

2. Create a virtual environment:
```zsh
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. Install development dependencies:
```zsh
pip install -r requirements-dev.txt
```

## Code Style

We follow PEP 8 guidelines. We use Black for code formatting and Flake8 for linting.

To format your code:
```zsh
black .
```
To run the linter:
```zsh
flake8 .
```
## Making a Release

1. Update the version number in `setup.py`.
2. Update `CHANGELOG.md`.
3. Commit these changes with a message like "Bump version to x.x.x".
4. Tag the commit: `git tag vx.x.x`
5. Push to GitHub: `git push origin master --tags`
6. Create a new release on GitHub using this tag.
7. The GitHub Action will automatically publish to PyPI.

## Documentation

We use MkDocs for documentation. To build the docs locally:
```zsh
mkdocs serve
```
Then visit `http://localhost:8000` to view the documentation.
