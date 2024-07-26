## 3. Flexible Tokenization Options

### Description
The tokenization function provides flexibility through its `pred` parameter, allowing different tokenization strategies for prediction and reference texts.

### How it works
1. When `pred=True`, the tokenization applies additional preprocessing steps suitable for prediction texts.
2. When `pred=False` (default), it applies standard tokenization suitable for reference texts.

### Gotchas / Specific Behaviors
- Users need to ensure they're using the appropriate `pred` value based on whether they're tokenizing prediction or reference text.
- The exact differences in tokenization between `pred=True` and `pred=False` should be clearly documented in the function's docstring.
