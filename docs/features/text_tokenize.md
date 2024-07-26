## 1. Text Tokenization

### Description
The text tokenization feature allows users to split input text into individual tokens or words, which is a crucial preprocessing step for many natural language processing tasks.

### How it works
1. The input text is passed to the `tokenize_text` function.
2. The function removes punctuation and splits the text on whitespace.
3. If `pred=True`, additional preprocessing steps are applied for prediction tasks.
4. The function returns a list of tokens.

### Gotchas / Specific Behaviors
- The tokenizer treats hyphenated words as a single token.
- Numbers are treated as separate tokens.
- The tokenizer is case-sensitive by default.
