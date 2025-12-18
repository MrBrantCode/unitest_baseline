"""
QUESTION:
Write a function which makes a list of strings representing all of the ways you can balance `n` pairs of parentheses

### Examples

```python
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
```
"""

def generate_balanced_parens(n):
    def dfs(s, open_count, close_count, max_pairs):
        if close_count == max_pairs:
            yield ''.join(s)
            return
        if open_count > close_count:
            s.append(')')
            yield from dfs(s, open_count, close_count + 1, max_pairs)
            s.pop()
        if open_count < max_pairs:
            s.append('(')
            yield from dfs(s, open_count + 1, close_count, max_pairs)
            s.pop()
    
    return list(dfs([], 0, 0, n))