# Deployment Procedure

## PyPI Deployment

### Pre-requisites
- PyPI account
- `setuptools` and `wheel` installed
- `.pypirc` file configured with your PyPI credentials

### How-to-Guide
1. Update the version number in `setup.py`.
2. Create source distribution and wheel:

```zsh
python setup.py sdist bdist_wheel
```

3. Upload to PyPI:
```zsh
twine upload dist/*
```

## Documentation Deployment

### Pre-requisites
- MkDocs installed
- GitHub Pages configured for your repository

### How-to-Guide
1. Build the documentation:
```zsh
mkdocs build
```
2. Deploy to GitHub Pages:
```zsh
mkdocs gh-deploy
```
3. docs/features/example.md:
This file should be replaced with actual features of your project. Here's an example:
```markdown
# Feature: Text Tokenization

## Description
The text tokenization feature allows users to split input text into individual tokens or words.

## How does it work
1. The input text is passed to the `tokenize_text` function.
2. The function removes punctuation and splits the text on whitespace.
3. If `pred=True`, additional preprocessing steps are applied for prediction tasks.
4. The function returns a list of tokens.

## Gotchas / Specific Behaviors
- The tokenizer treats hyphenated words as a single token.
- Numbers are treated as separate tokens.
- The tokenizer is case-sensitive by default.
```

4. docs/README.md:
This file should be updated to reflect your project. Here's a suggested update:
```markdown
# Ratchada Utils Documentation

## Project Brief

`ratchada_utils` is a Python library for text processing and utilities related to the Ratchada Whisper model. It provides tools for tokenization and evaluation of speech-to-text models.

Status: **In Development**

## How To Use

Refer to the [Installation](../README.md#installation) and [Usage](../README.md#usage) sections in the main README for basic usage instructions. For more detailed information on each feature, check the individual documentation pages.
```
