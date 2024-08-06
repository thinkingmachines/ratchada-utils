# Ratchada_Utils

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/ratchada-utils.svg)](https://badge.fury.io/py/ratchada-utils)
[![Python Versions](https://img.shields.io/pypi/pyversions/ratchada-utils.svg)](https://pypi.org/project/ratchada-utils/)

## Project Brief

Ratchada_Utils is a Python library designed to provide text processing utilities, particularly for tasks related to the Ratchada Whisper model. It offers tools for tokenization and evaluation of speech-to-text outputs.

## Features

- Text tokenization
- Simple evaluation of speech-to-text outputs
- Parallel processing for improved performance

## Installation

You can install `ratchada_utils` using pip:

```bash
pip install ratchada_utils
```

For the latest development version, you can install directly from the GitHub repository:
```bash
pip install git+https://github.com/yourusername/ratchada_utils.git
```

## Usage
### Tokenizing Text

```bash
from ratchada_utils.processor import tokenize_text

text = "Your input text here."
tokenized_text = tokenize_text(text, pred=True)
print("Tokenized Text:", tokenized_text)
# Output: Tokenized Text: ['your', 'input', 'text', 'here']
```

### Evaluate

```bash
import pandas as pd
from ratchada_utils.evaluator import simple_evaluation

result = pd.read_csv("./output/result-whisper-ratchada.csv")
summary = simple_evaluation(result["pred_text"], result["true_text"])
print(summary)
```

## Requirements

1. Python 3.10 or higher
2. Dependencies are listed in requirements.txt

## Documentation
For full documentation, please visit our documentation page.
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Contact
For any questions or issues, please open an issue on the GitHub repository.
