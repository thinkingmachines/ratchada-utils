## 2. Simple Evaluation

### Description
The simple evaluation feature provides a way to compare predicted text against reference text, which is particularly useful for assessing the performance of speech-to-text models.

### How it works
1. The `simple_evaluation` function takes two lists: predicted texts and actual (reference) texts.
2. It tokenizes both lists using the `tokenize_text` function.
3. The function uses parallel processing to flatten and filter the tokenized lists.
4. It then calls an `evaluate` function (not shown in the provided code) to compute evaluation metrics.
5. The result is returned as a pandas DataFrame.

### Gotchas / Specific Behaviors
- The evaluation is performed on a token level, not character level.
- The function uses multiprocessing, which may not work in all environments (e.g., some Jupyter notebook setups).
- The exact metrics computed depend on the implementation of the `evaluate` function.
