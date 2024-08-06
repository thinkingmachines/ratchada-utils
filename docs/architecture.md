# Project Architecture

## Overview

Ratchada_Utils is a Python library designed to provide text processing utilities, particularly for tasks related to the Ratchada Whisper model. It's primarily used for tokenization and evaluation of speech-to-text outputs.

## Architecture Details

- Language: Python (3.10+)
- Package Manager: pip
- Documentation: MkDocs
- Testing: pytest
- Code Style: Black, Flake8
- Continuous Integration: GitHub Actions

## Main Components

1. Text Processor
   - Location: `ratchada_utils/processor/`
   - Key Function: `tokenize_text()`
   - Description: Handles text tokenization for both prediction and reference texts.

2. Evaluator
   - Location: `ratchada_utils/evaluator/`
   - Key Function: `simple_evaluation()`
   - Description: Provides metrics for comparing predicted text against reference text.

## Data Flow

1. Input: Raw text (string)
2. Processing: Tokenization
3. Evaluation: Comparison of tokenized prediction and reference texts
4. Output: Evaluation metrics (pandas DataFrame)

## Dependencies

Major dependencies include:
- pandas: For data manipulation and analysis
- numpy: For numerical operations
- concurrent.futures: For parallel processing

Full list of dependencies can be found in `requirements.txt`.

## Development Environment

The project is developed using a virtual environment to isolate dependencies. See the [Development Guide](development.md) for setup instructions.

## Deployment

The package is deployed to PyPI for easy installation by users. Deployment is handled through GitHub Actions. See the [Deployment Procedure](deployment.md) for details.

## Security Considerations

- The library doesn't handle sensitive data directly, but users should be cautious about the content they process.
- No external API calls are made by the library.

## Scalability

The `simple_evaluation` function uses `concurrent.futures.ProcessPoolExecutor` for parallel processing, allowing it to scale with available CPU cores.

## Limitations

- The library is designed for text processing and may not handle other data types effectively.
- Performance may degrade with extremely large input sizes due to memory constraints.

## Future Improvements

1. Implement more advanced tokenization methods
2. Add support for additional evaluation metrics
3. Optimize memory usage for large inputs

For any questions or issues regarding the architecture, please open an issue on the GitHub repository.
