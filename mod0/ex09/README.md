# ft_package

A sample test package for counting occurrences in an iterable.

## Installation 📥

Install the package using `pip` from the distribution files:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

or:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage 🛠️

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```