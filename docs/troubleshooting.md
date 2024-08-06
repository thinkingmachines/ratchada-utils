# Troubleshooting

## Common Issues

### ImportError: No module named 'ratchada_utils'

Make sure you have installed the package correctly. Try reinstalling:

```zsh
pip uninstall ratchada_utils
pip install ratchada_utils
```

### TypeError when using tokenize_text

Make sure you're passing the correct type of arguments to the function. The `text` parameter should be a string, and `pred` should be a boolean.

## Debugging

If you encounter any issues, you can enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Then run your code, and you'll see more detailed logging output.

## Reporting Issues

If you encounter a bug or have a feature request, please open an issue on our GitHub repository.
When reporting an issue, please include:

- A clear description of the problem
- Steps to reproduce the issue
- Your operating system and Python version
- The version of ratchada_utils you're using

## Getting Help
If you need help using ratchada_utils, you can:

- Check the documentation
- Open an issue on GitHub
- Reach out to the maintainers directly (contact information in README)
