# completely
*High-quality* data is extremely important nowadays. But before you start cleaning/processing it,
you might want to check how **complete** the dataset really is:

```python
from completely import measure

data = [{'name': 'Bob', 'age': 42}, {'name': 'Alice', 'age': None}, {'name': '', 'age': 100}]
print(measure(data))

# Output: 0.667
```

**completely** currently works with:
- Lists of strings / ints / floats
- Lists of dicts
- Nested lists of one of the above

## Setup
```bash
pip install completely
```

## Contributing
We're happy about every meaningful contribution to this project via pull requests. If needed, we'll setup more precise guidelines on how to contribute at some point.
