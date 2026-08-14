# Python for Data Science — 42 Lisboa

> Python and Data Science specialization piscine at 42 Lisboa.
> Five modules, 29 exercises, ~2000 lines of Python 3.10 written under the 42 norm.

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![flake8](https://img.shields.io/badge/flake8-passing-brightgreen)](#code-quality)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)](https://matplotlib.org/)
[![Exercises](https://img.shields.io/badge/exercises-29-blue)](#module-by-module)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](mod0/ex09/LICENSE)

---

## About

The **Python for Data Science piscine** is the intensive track through which
[42 Lisboa](https://www.42lisboa.com/) introduces Python to students who already
know C. There are no classes and no teachers: every day brings a PDF *subject*
with a set of exercises, explicit constraints, and the exact expected output.
Work is validated through **peer evaluation** — another student runs your code
on their own machine and questions every implementation decision.

The pedagogical interest of the format lies in the constraints. It's not enough
for the program to work: the *subject* forbids libraries for the core problem,
mandates specific constructs (a *list comprehension* here, a `yield` there, a
decorator elsewhere), and invalidates the exercise if a single exception escapes.
The result is that you reimplement by hand what you'd normally import —
`filter`, `tqdm`, matrix transposition, standard deviation — and only afterwards
earn the right to use the library version.

This repository is my complete solution to the five modules.

---

## Table of contents

- [Module overview](#module-overview)
- [Skills demonstrated](#skills-demonstrated)
- [Repository structure](#repository-structure)
- [42 rules and constraints](#42-rules-and-constraints)
- [Module by module](#module-by-module)
  - [mod0 — Starting](#mod0--starting)
  - [mod1 — Array](#mod1--array)
  - [mod2 — DataTable](#mod2--datatable)
  - [mod3 — Oriented Object Programming](#mod3--oriented-object-programming)
  - [mod4 — Data Oriented Design](#mod4--data-oriented-design)
- [How to run](#how-to-run)
- [Code quality](#code-quality)
- [Design notes](#design-notes)
- [Data and credits](#data-and-credits)
- [License and author](#license-and-author)

---

## Module overview

| Module | Subject | Ex. | Stack | Core concept |
|:---|:---|:---:|:---|:---|
| [`mod0`](mod0/) | *Starting* | 10 | stdlib, `tqdm`, `setuptools` | Fundamentals, `sys.argv`, generators, packaging |
| [`mod1`](mod1/) | *Array* | 6 | `numpy`, `Pillow`, `matplotlib` | N-dimensional arrays and image processing |
| [`mod2`](mod2/) | *DataTable* | 4 | `pandas`, `matplotlib` | Loading, cleaning and visualizing datasets |
| [`mod3`](mod3/) | *Oriented Object Programming* | 5 | stdlib (`abc`) | Inheritance, MRO/C3, magic methods, `property` |
| [`mod4`](mod4/) | *Data Oriented Design* | 4 | stdlib (`dataclasses`) | Closures, decorators, `*args`/`**kwargs` |

---

## Skills demonstrated

Each row links to the actual implementation in the repository.

### Idiomatic and functional Python

| Concept | Where |
|:---|:---|
| *List comprehensions* as a substitute for `filter` | [`mod0/ex06/ft_filter.py`](mod0/ex06/ft_filter.py) |
| `lambda` functions and first-class functions | [`mod0/ex06/filterstring.py`](mod0/ex06/filterstring.py) |
| Generators and the `yield` operator | [`mod0/ex08/Loading.py`](mod0/ex08/Loading.py), [`generators.py`](mod0/ex08/generators.py) |
| Generator exhaustion and infinite generators | [`mod0/ex08/generators.py`](mod0/ex08/generators.py) |
| Closures and `nonlocal` | [`mod4/ex01/in_out.py`](mod4/ex01/in_out.py) |
| Parameterized decorators (3-level factory) | [`mod4/ex02/callLimit.py`](mod4/ex02/callLimit.py) |
| `*args` / `**kwargs` with keyword-driven dispatch | [`mod4/ex00/statistics.py`](mod4/ex00/statistics.py) |
| Introspection: `__doc__`, `__dict__`, `__name__`, `mro()` | [`mod0/ex02`](mod0/ex02/find_ft_type.py), [`mod3/ex02`](mod3/ex02/DiamondTrap.py) |
| PEP 604 type hints (`int \| float`, `list[float]`) | [`mod1/ex00/give_bmi.py`](mod1/ex00/give_bmi.py), [`mod3/ex04`](mod3/ex04/ft_calculator.py) |

### Object-oriented programming

| Concept | Where |
|:---|:---|
| Abstract classes (`ABC`, `@abstractmethod`) | [`mod3/ex00/S1E9.py`](mod3/ex00/S1E9.py) |
| Inheritance and `super()` | [`mod3/ex01/S1E7.py`](mod3/ex01/S1E7.py) |
| `__repr__` / `__str__` | [`mod3/ex01/S1E7.py`](mod3/ex01/S1E7.py) |
| `@classmethod` as a factory | [`mod3/ex01/S1E7.py`](mod3/ex01/S1E7.py) |
| Diamond inheritance and C3 linearization | [`mod3/ex02/DiamondTrap.py`](mod3/ex02/DiamondTrap.py) |
| `property()` — getters/setters | [`mod3/ex02/DiamondTrap.py`](mod3/ex02/DiamondTrap.py) |
| Operator overloading (`__add__`, `__truediv__`, …) | [`mod3/ex03/ft_calculator.py`](mod3/ex03/ft_calculator.py) |
| `@staticmethod` | [`mod3/ex04/ft_calculator.py`](mod3/ex04/ft_calculator.py) |
| `@dataclass`, `field(init=False)`, `__post_init__` | [`mod4/ex03/new_student.py`](mod4/ex03/new_student.py) |

### Data science

| Concept | Where |
|:---|:---|
| Vectorized arithmetic in NumPy | [`mod1/ex00/give_bmi.py`](mod1/ex00/give_bmi.py) |
| Boolean masks | [`mod1/ex00/give_bmi.py`](mod1/ex00/give_bmi.py) |
| Multi-axis slicing and `slice()` objects | [`mod1/ex01/array2D.py`](mod1/ex01/array2D.py), [`mod1/ex03/zoom.py`](mod1/ex03/zoom.py) |
| Fancy indexing over the channel axis | [`mod1/ex05/pimp_image.py`](mod1/ex05/pimp_image.py) |
| Axis reduction (`np.mean(axis=-1)`) | [`mod1/ex05/pimp_image.py`](mod1/ex05/pimp_image.py) |
| Matrix transposition implemented from scratch | [`mod1/ex04/rotate.py`](mod1/ex04/rotate.py) |
| Image → array via Pillow | [`mod1/ex02/load_image.py`](mod1/ex02/load_image.py) |
| CSV I/O and indexing in pandas | [`mod2/ex00/load_csv.py`](mod2/ex00/load_csv.py) |
| Data cleaning (`'29M'` → `29000000.0`) | [`mod2/ex02/aff_pop.py`](mod2/ex02/aff_pop.py) |
| Label-based selection (`.loc`) and `Series.apply` | [`mod2/ex02/aff_pop.py`](mod2/ex02/aff_pop.py) |
| Time series, scatter plots, log scale | [`mod2/ex01`](mod2/ex01/aff_life.py), [`mod2/ex03`](mod2/ex03/projection_life.py) |
| Descriptive statistics implemented from scratch | [`mod4/ex00/statistics.py`](mod4/ex00/statistics.py) |

### Software engineering

| Concept | Where |
|:---|:---|
| Packaging with `pyproject.toml` / `setuptools` | [`mod0/ex09/pyproject.toml`](mod0/ex09/pyproject.toml) |
| `__init__.py`, relative imports, `__all__` | [`mod0/ex09/ft_package/__init__.py`](mod0/ex09/ft_package/__init__.py) |
| `pip`-installable distribution (wheel + sdist) | [`mod0/ex09/README.md`](mod0/ex09/README.md) |
| Error handling with no exception left uncaught | cross-cutting |
| Terminal rendering with `\r` and `os.get_terminal_size` | [`mod0/ex08/Loading.py`](mod0/ex08/Loading.py) |
| Linter compliance (flake8 / PEP 8) | [see section](#code-quality) |

---

## Repository structure

Every exercise is a self-contained, runnable directory — a rule enforced by 42,
which evaluates each `ex` in isolation.

```
python_for_data_science/
├── en.subject python.pdf              # general presentation of the piscine
│
├── mod0/  Starting                    # fundamentals, CLI, generators, packaging
│   ├── ex00/  Hello.py                # list, tuple, set, dict
│   ├── ex01/  format_ft_time.py       # time, strftime, format specs
│   ├── ex02/  find_ft_type.py         # type introspection
│   ├── ex03/  NULL_not_found.py       # None, NaN, 0, "", False
│   ├── ex04/  whatis.py               # sys.argv, assert
│   ├── ex05/  building.py             # string analysis, stdin
│   ├── ex06/  ft_filter.py            # filter reimplemented
│   │          filterstring.py         # lambda + list comprehension
│   ├── ex07/  sos.py                  # Morse code encoder
│   ├── ex08/  Loading.py              # ft_tqdm — generator-driven progress bar
│   │          generators.py           # generators playground
│   └── ex09/  ft_package/             # installable Python package
│              pyproject.toml, LICENSE, README.md
│
├── mod1/  Array                       # NumPy and images
│   ├── ex00/  give_bmi.py             # vectorization, boolean masks
│   ├── ex01/  array2D.py              # shape, 2D slicing
│   ├── ex02/  load_image.py           # Pillow → np.array
│   ├── ex03/  zoom.py                 # centered crop + grayscale
│   ├── ex04/  rotate.py               # manual transpose
│   └── ex05/  pimp_image.py           # 5 color filters
│
├── mod2/  DataTable                   # pandas + matplotlib (Gapminder)
│   ├── ex00/  load_csv.py             # robust CSV loading
│   ├── ex01/  aff_life.py             # life expectancy in Portugal
│   ├── ex02/  aff_pop.py              # population: Portugal vs France
│   └── ex03/  projection_life.py      # GDP vs life expectancy, 1900
│
├── mod3/  Oriented Object Programming # Game of Thrones as a case study
│   ├── ex00/  S1E9.py                 # Character (ABC) + Stark
│   ├── ex01/  S1E7.py                 # Baratheon, Lannister, classmethod
│   ├── ex02/  DiamondTrap.py          # King(Baratheon, Lannister) — C3
│   ├── ex03/  ft_calculator.py        # operator overloading
│   └── ex04/  ft_calculator.py        # dot product via staticmethod
│
└── mod4/  Data Oriented Design        # functional Python
    ├── ex00/  statistics.py           # statistics from scratch
    ├── ex01/  in_out.py               # closures and nonlocal
    ├── ex02/  callLimit.py            # parameterized decorator
    └── ex03/  new_student.py          # dataclass
```

Each module includes its own `en.subject*.pdf`. The `tester.py` files are my own
test harnesses — 42 doesn't grade them, but they're the tool used during the defense.

---

## 42 rules and constraints

The code in this repository follows the rules laid out in the *subjects*. They're
worth spelling out, because they explain decisions that would otherwise look arbitrary:

- **Python 3.10** required.
- **Zero global variables.**
- **No code in the global scope.** Every program has a `main()` guarded by
  `if __name__ == "__main__": main()`.
- **`__doc__` required** on every function, class and method.
- **Explicit imports.** `import numpy as np` is mandatory; `from pandas import *`
  scores **0** on the exercise.
- **No exception may escape** — not even for the error cases the subject explicitly
  asks you to test. An uncaught exception invalidates the exercise.
- **Norm compliance**, which at 42 means `flake8` with zero warnings.

Out of this comes an error-handling idiom used consistently across the repository:
the assertion documents the precondition, the `try` guarantees nothing escapes, and
errors of other kinds are translated into `AssertionError` to keep the message to
the user consistent.

```python
try:
    assert len(sys.argv) == 3, "the arguments are bad"
    length = int(sys.argv[2])
except ValueError:
    print("AssertionError: the arguments are bad")
except AssertionError as msg:
    print(f"AssertionError: {msg}")
```

---

## Module by module

### mod0 — *Starting*

> *"Today, you will learn the basics of the Python programming language."*

From the first `print` to a `pip`-installable package. Halfway through the module —
right after `ex04` — the *subject* introduces the additional rules (`main()`,
docstrings, flake8), and the code style visibly changes from there on.

| Ex | File | What it does | Key concept |
|:---:|:---|:---|:---|
| 00 | [`Hello.py`](mod0/ex00/Hello.py) | Mutates the four base containers and prints them | `list`, `tuple`, `set`, `dict` and mutability |
| 01 | [`format_ft_time.py`](mod0/ex01/format_ft_time.py) | Epoch with thousands separator and scientific notation | `time`, `strftime`, format specs (`,.4f`, `.2e`) |
| 02 | [`find_ft_type.py`](mod0/ex02/find_ft_type.py) | Prints the object's type and returns 42 | Introspection via `type()` and `__name__` |
| 03 | [`NULL_not_found.py`](mod0/ex03/NULL_not_found.py) | Distinguishes the five forms of "nothing" in Python | Semantics of `None`, `NaN`, `0`, `""`, `False` |
| 04 | [`whatis.py`](mod0/ex04/whatis.py) | Odd or even, from a CLI argument | `sys.argv`, `assert`, exception translation |
| 05 | [`building.py`](mod0/ex05/building.py) | Counts uppercase, lowercase, punctuation, digits and spaces | `string.punctuation`, `str.is*` predicates, `stdin` |
| 06 | [`ft_filter.py`](mod0/ex06/ft_filter.py) · [`filterstring.py`](mod0/ex06/filterstring.py) | Reimplements `filter` and filters words by length | *List comprehension*, `lambda` |
| 07 | [`sos.py`](mod0/ex07/sos.py) | Encodes a string into Morse code | Dictionary as a lookup table |
| 08 | [`Loading.py`](mod0/ex08/Loading.py) | Reimplements `tqdm` | Generators, `yield`, terminal control |
| 09 | [`ft_package/`](mod0/ex09/) | Publishable, installable package | `pyproject.toml`, `setuptools`, `__all__` |

#### Highlight — `ex06`: reimplementing `filter`

The *subject* requires that `ft_filter.__doc__` return the same as `filter.__doc__`,
and that the recoding use a *list comprehension*. Note the `func is None` branch,
which replicates a lesser-known behavior of the original `filter`: with no function,
what survives is whatever is *truthy*.

```python
def ft_filter(func, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if func is None:
        newlist = [it for it in iterable if it]
    else:
        newlist = [it for it in iterable if func(it)]
    return newlist
```

```console
$ python3 filterstring.py "Hello the World" 4
['Hello', 'World']

$ python3 filterstring.py 3 "Hello the World"
AssertionError: the arguments are bad
```

#### Highlight — `ex08`: a hand-rolled `tqdm`

The only library allowed is `os`. The bar is a **generator**: it hands the element
back to the caller with `yield` and, on every iteration, rewrites the line with
`\r`. The usable width is computed from `os.get_terminal_size()` minus the space
taken by the bar's frame, so it adapts to any terminal.

```python
def ft_tqdm(lst: range) -> None:
    """..."""
    total = len(lst)
    terminal_length = os.get_terminal_size().columns
    progress_count_len = len(str(total))
    bar_elements = len("100%|[]| /  ") + ((progress_count_len) * 2)
    bar_total_range = terminal_length - bar_elements

    for elem in lst:
        percent = ((elem + 1) / total) * 100
        percent_str = (str(int(percent)) + "%").rjust(4)
        filled = int(((elem + 1) / total) * bar_total_range)
        progress_bar = (("=" * (filled)) + ">").ljust(bar_total_range)
        progress_count = str(elem).rjust(progress_count_len)

        print(
            f"\r{percent_str}|[{progress_bar}]| {progress_count}/{total}",
            end="",
            flush=True
        )

        yield elem
```

```console
100%|[==========================================================>]| 333/333
100%|██████████████████████████████████| 333/333 [00:01<00:00, 191.61it/s]
```

The companion [`generators.py`](mod0/ex08/generators.py) explores the rest of the
topic: a generator being exhausted on the second `for` loop, `next()`, and
infinite generators.

#### Highlight — `ex09`: a real package

```console
$ pip install ./dist/ft_package-0.0.1-py3-none-any.whl
$ python3 test/tester.py
2
0
```

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "ft_package"
version = "0.0.1"
requires-python = ">=3.10"
license = { text = "MIT" }
```

---

### mod1 — *Array*

> *"Today, you will discover arrays, their manipulations, and work on images."*

An image is an `np.array` of shape `(height, width, channels)`. The whole module
explores that identity: cropping is *slicing*, isolating a color is indexing the
last axis, converting to grayscale is reducing it.

| Ex | File | What it does | Key concept |
|:---:|:---|:---|:---|
| 00 | [`give_bmi.py`](mod1/ex00/give_bmi.py) | Vectorized BMI + boolean threshold | Vectorization, boolean masks |
| 01 | [`array2D.py`](mod1/ex01/array2D.py) | Prints `shape` and truncates via *slicing* | `slice()` objects, matrix validation |
| 02 | [`load_image.py`](mod1/ex02/load_image.py) | Loads JPG/JPEG into `np.array` | Pillow, per-type error handling |
| 03 | [`zoom.py`](mod1/ex03/zoom.py) | Centered 400×400 crop in grayscale | Multi-axis slicing |
| 04 | [`rotate.py`](mod1/ex04/rotate.py) | Transposes the image **with no library** | Manual transposition, `np.zeros` |
| 05 | [`pimp_image.py`](mod1/ex05/pimp_image.py) | Five color filters | Fancy indexing, broadcasting, axis reduction |

#### Highlight — `ex00`: vectorization instead of loops

```console
$ python3 tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
```

BMI is computed for the whole vector at once, and the threshold produces a boolean
array directly — not a single `for` loop.

#### Highlight — `ex04`: a transpose you're not allowed to import

> *"You have to do the transpose yourself, no library is allowed for the transpose."*

No `.T`, no `np.transpose`. The destination is allocated with the `dtype` preserved,
and both axes are walked, swapping indices and collapsing the channel axis:

```python
def transpose(img: np.array) -> np.array:
    """..."""
    height, width = img.shape[0], img.shape[1]
    transposed_img = np.zeros((height, width), dtype=img.dtype)

    for y in range(height):
        for x in range(width):
            transposed_img[x][y] = img[y][x][0]
```

#### Highlight — `ex05`: filters under operator restrictions

The *subject* restricts which operators each filter may use — `invert` may use
`= + - *`, `red` only `= *`, `green` only `= -`, `blue` only `=`, and `grey` only
`= /`. The restriction forces you to think in terms of broadcasting and axis
indexing, not pixel-by-pixel loops.

```python
def ft_invert(img: np.array):
    """Inverts the color of the image received."""
    return_img = 255 - img          # broadcasting over the whole array

def ft_green(img: np.array):
    """Applies a green filter by setting blue and red channels to zero."""
    return_img = img.copy()         # .copy() so the source isn't mutated
    return_img[:, :, [0, 2]] = 0    # fancy indexing on the channel axis

def ft_grey(img: np.array):
    return_img = np.mean(img, axis=-1)   # reduction of the channel axis
```

---

### mod2 — *DataTable*

> *"Today, you will learn how to load, manipulate and display data table."*

Real [Gapminder](https://www.gapminder.org/) data in wide format — one row per
country, one column per year, from 1800 to 2100.

| Ex | File | What it does | Key concept |
|:---:|:---|:---|:---|
| 00 | [`load_csv.py`](mod2/ex00/load_csv.py) | Loads the CSV, indexes by country, returns `None` on error | `read_csv`, `set_index`, `.shape` |
| 01 | [`aff_life.py`](mod2/ex01/aff_life.py) | Life expectancy in Portugal across 3 centuries | `.loc`, time series |
| 02 | [`aff_pop.py`](mod2/ex02/aff_pop.py) | Population of Portugal vs France, 1800–2050 | Data cleaning, `Series.apply`, legends |
| 03 | [`projection_life.py`](mod2/ex03/projection_life.py) | GDP *per capita* vs life expectancy in 1900 | Scatter plot, log scale, index-based join |

#### Highlight — `ex00`: loading that never crashes

The *subject*'s contract is clear: return `None` if the path is bad, if the format
is bad, if anything at all goes wrong.

```python
def load(path: str) -> pd.DataFrame:
    """..."""
    try:
        df = pd.read_csv(path)
        if "country" in df.columns:
            df = df.set_index("country")
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as msg:
        print(f"Error: {msg}")
    return None
```

```console
$ python3 tester.py
Loading dataset of dimensions (195, 301)
```

The test fixtures in the repository are deliberate: [`test.csv`](mod2/ex00/test.csv)
is empty, and [`life_expectancy_years copy.csv`](mod2/ex00/) is identical to the
original except for its header — `pais` instead of `country` — to exercise the
branch where the index column doesn't exist.

#### Highlight — `ex02`: the data arrives dirty

Gapminder writes population as `'29M'`, `'10k'`, `'1.4B'`. Before plotting,
everything has to be normalized to `float`:

```python
def clean_pop(val):
    """Converts population string formatted values
    (e.g., '29M', '10k') to numeric float."""
    if isinstance(val, str):
        if val.endswith('M'):
            return float(val[:-1]) * 1_000_000
        elif val.endswith('k'):
            return float(val[:-1]) * 1_000
        elif val.endswith('B'):
            return float(val[:-1]) * 1_000_000_000
    return float(val)
```

```python
df_subset = df.loc[:, "1800":"2050"]           # label-based column slicing
campus_data = df_subset.loc["France"].apply(clean_pop)
other_data = df_subset.loc["Portugal"].apply(clean_pop)
```

#### Highlight — `ex03`: the subject's question

> *"Do you see a correlation between lifespan and gross domestic product?"*

The chart joins two datasets on their shared index (the country) and uses a
logarithmic scale on the GDP axis — without it, the cloud of points collapses
against the axis, because income spans orders of magnitude rather than a linear
range.

```python
plt.scatter(df_income["1900"], df_life["1900"])
plt.xscale("log")
plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
```

The answer reads off the chart: the correlation exists and is positive, but it's
**logarithmic** — doubling the income of the poorest countries buys far more years
of life than doubling the income of the richest.

---

### mod3 — *Oriented Object Programming*

> *"Today, you will see the classes and the heritage."*

The *subject* opens with a warning: the usual complaint about data scientists is
that they write bad code, because they neglect object-oriented programming. The
module uses *Game of Thrones* as its domain.

| Ex | File | What it does | Key concept |
|:---:|:---|:---|:---|
| 00 | [`S1E9.py`](mod3/ex00/S1E9.py) | Abstract `Character` + `Stark` | `ABC`, `@abstractmethod` |
| 01 | [`S1E7.py`](mod3/ex01/S1E7.py) | `Baratheon` and `Lannister` | `super()`, `__repr__`/`__str__`, `@classmethod` |
| 02 | [`DiamondTrap.py`](mod3/ex02/DiamondTrap.py) | `King(Baratheon, Lannister)` | Diamond inheritance, C3, `property()` |
| 03 | [`ft_calculator.py`](mod3/ex03/ft_calculator.py) | Vector with a scalar | `__add__`, `__mul__`, `__sub__`, `__truediv__` |
| 04 | [`ft_calculator.py`](mod3/ex04/ft_calculator.py) | Dot product between vectors | `@staticmethod`, `zip` |

#### Highlight — `ex01`: `@classmethod` as an alternate constructor

`cls` — not the class's literal name — is what keeps the factory correct in any
subclass:

```python
@classmethod
def create_lannister(cls, first_name: str, is_alive: bool = True):
    """Factory method to create a Lannister instance."""
    return cls(first_name, is_alive)
```

#### Highlight — `ex02`: the diamond trap

Joffrey Baratheon is heir to both houses. In Python, `King(Baratheon, Lannister)`
raises the question of which `__init__` runs and where the attributes come from —
the problem that **C3 linearization** has solved since Python 2.3.

The subtle part is in the setters. If `set_eyes` did `self.eyes = color`, and
`eyes` is a `property` whose setter is `set_eyes` itself, the result would be
infinite recursion. Writing directly to `self.__dict__` bypasses the descriptor
protocol and solves the problem:

```python
class King(Baratheon, Lannister):
    """Representing the King"""
    def set_eyes(self, color: str):
        """Setter for eyes attribute modifying __dict__ directly."""
        self.__dict__['eyes'] = color

    def get_eyes(self):
        """Getter for eyes attribute accessing __dict__ directly."""
        return self.__dict__['eyes']

    eyes = property(get_eyes, set_eyes)
```

`main()` prints the MRO to make the linearization visible:

```console
$ python3 DiamondTrap.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}

Inspecting the data structure of class inheritance of King
['King', 'Baratheon', 'Lannister', 'Character', 'ABC', 'object']
Inspecting the data structure of class inheritance of Baratheon
['Baratheon', 'Character', 'ABC', 'object']
```

That's the answer to why Joffrey is born with brown eyes: `Baratheon` comes before
`Lannister` in the MRO, so its `__init__` is the one that prevails.

#### Highlight — `ex03` and `ex04`: the two calculators

```console
$ python3 mod3/ex03/ft_calculator.py       $ python3 mod3/ex04/ft_calculator.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]           Dot product is: 56
---                                        Add Vector is : [7.0, 14.0, 5.0]
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]        Sous Vector is: [3.0, 6.0, -1.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
float division by zero
```

`ex03` does operator overloading on an instance; `ex04` answers a hint from the
*subject* — *"find a decorator that can help you to use the Methods without
instantiating this class"* — with `@staticmethod` and `zip`:

```python
@staticmethod
def dotproduct(V1: list[float], V2: list[float]) -> None:
    """..."""
    print(f"Dot product is: {sum([it[0] * it[1] for it in zip(V1, V2)])}")
```

---

### mod4 — *Data Oriented Design*

> *"Today, you will see some Structure Design."*

Functional Python: functions that take functions, functions that return
functions, and functions that remember what happened before.

| Ex | File | What it does | Key concept |
|:---:|:---|:---|:---|
| 00 | [`statistics.py`](mod4/ex00/statistics.py) | Mean, median, quartiles, standard deviation and variance | `*args`/`**kwargs`, keyword-driven dispatch |
| 01 | [`in_out.py`](mod4/ex01/in_out.py) | Counter that preserves state across calls | Closures, `nonlocal` |
| 02 | [`callLimit.py`](mod4/ex02/callLimit.py) | Blocks a function past N calls | Parameterized decorator |
| 03 | [`new_student.py`](mod4/ex03/new_student.py) | Student with a derived login and ID | `@dataclass`, `field(init=False)` |

#### Highlight — `ex00`: statistics with no library

Neither `statistics` nor `numpy`. Everything is derived from the positional
arguments, and what gets computed is decided by the **values** of the keyword
arguments — not their keys, which the *subject* deliberately fills with junk
(`toto=`, `tutu=`, `tata=`).

```python
def ft_statistics(*args: any, **kwargs: any) -> None:
    """..."""
    for operation in kwargs.values():
        if operation == "std" or operation == "var":
            mean = sum(args) / n_values
            sqr_deviation = [(num - mean) ** 2 for num in args]
            variance = sum(sqr_deviation) / n_values
            std_deviation = variance ** 0.5
```

```console
$ python3 statistics.py
mean : 95.6
median : 42
quartile : [11.0, 64.0]
-----
std : 17982.70124086944
var : 323377543.9183673
-----
-----
ERROR
ERROR
ERROR
```

The third block is empty on purpose — the keywords don't match any known
operation, so nothing is computed and nothing crashes. The fourth prints `ERROR`
three times: operations are requested but there's no data to operate on.

#### Highlight — `ex02`: a decorator with a parameter

Three levels of nesting, because that's what a parameterized decorator is:
`callLimit(3)` **returns** the decorator, which **returns** the wrapped function.
The counter lives in the closure — `global` is forbidden by the *subject*.

```python
def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if count < limit:
                function(*args, **kwds)
                count += 1
            elif count == limit:
                print(f"Error: {function} call too many times")
        return limit_function

    return callLimiter
```

```console
$ python3 tester.py
f()
g()
f()
Error: <function g at 0x785960224280> call too many times
f()
Error: <function g at 0x785960224280> call too many times
```

#### Highlight — `ex03`: a dataclass with derived fields

The *subject* forbids writing `__str__` and `__repr__`, and requires `login` and
`id` to be impossible to pass to the constructor. `field(init=False)` removes
them from the generated signature; `__post_init__` computes them afterward:

```python
@dataclass
class Student:
    name: str
    surname: str

    active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.active = True
        self.login = self.name[0] + self.surname.lower()
        self.id = generate_id()
```

```console
$ python3 tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='ymXBxDevlDzNKvx')

>>> Student(name="Edward", surname="agle", id="toto")
TypeError: Student.__init__() got an unexpected keyword argument 'id'
```

---

## How to run

**Requirements:** Python 3.10 or newer.

```bash
git clone https://github.com/DinisPetrukha/python_for_data_science.git
cd python_for_data_science
pip install numpy pandas matplotlib Pillow tqdm
```

Every exercise is self-contained and expects to be run **from its own
directory** — images, CSVs and imported modules are resolved by relative path:

```bash
cd mod0/ex08 && python3 tester.py        # ft_tqdm vs tqdm side by side
cd mod1/ex05 && python3 pimp_image.py    # generates invert/red/green/blue/grey.png
cd mod2/ex03 && python3 projection_life.py
cd mod3/ex02 && python3 DiamondTrap.py
cd mod4/ex00 && python3 statistics.py
```

The `mod1` and `mod2` exercises save charts as PNG files in the working directory
(`zoom_output.png`, `pop_comparison.png`, `projection_1900.png`, …). These files
aren't version-controlled: they're generated at run time.

**Installing the `mod0/ex09` package:**

```bash
cd mod0/ex09
pip install build
python3 -m build                              # produces dist/
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
pip show -v ft_package
```

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))   # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))   # 0
```

---

## Code quality

At 42, the Python norm means `flake8` with zero warnings.

```bash
pip install flake8
python3 -m flake8 .
```

**Every file submitted from `mod0/ex05` onward passes with zero warnings** —
which covers `mod1` through `mod4` in full.

The exception is the first five exercises of `mod0` (`ex00`–`ex04`), and the
reason is the *subject* itself: the norm rules only appear in Chapter VII, titled
*"From now on you must follow these additional rules"*, **after** `ex04`. Those
files are left as they are, because they document the module's progression. The
few remaining warnings sit in `tester.py` files, which 42 doesn't grade.

To verify the scope the badge refers to:

```bash
python3 -m flake8 . | grep -v tester.py | grep -v "mod0/ex0[0-4]"
# no output
```

---

## Design notes

**Deliberate file duplication.** [`load_csv.py`](mod2/ex00/load_csv.py) appears
four times, [`S1E9.py`](mod3/ex00/S1E9.py) three times, `load_image.py` four
times. This isn't an oversight: 42 grades each `exNN` directory in isolation, and
the *subject* explicitly lists previous files as "*Files to turn in: Files from
previous exercises + …*". Every exercise has to run on its own.

Not all copies are identical, either. `load_image.py` evolves with the exercise
it serves: in `mod1/ex04` it also embeds the `zoom` function, and in `mod1/ex05`
it prints the array in addition to the shape. It's the same function, adapted to
what each program needs.

**Consistent error handling.** The `assert` documents the precondition, the `try`
guarantees nothing escapes, and errors from other sources are translated into
`AssertionError` so the message shown to the user stays consistent. This directly
answers the rule that any uncaught exception invalidates the exercise.

**Reimplement before importing.** `ft_filter` instead of `filter`, `ft_tqdm`
instead of `tqdm`, `transpose` instead of `.T`, variance and standard deviation
instead of `statistics`. In several cases the *subjects* have you run both
versions side by side — the library version is the spec the hand-written
implementation has to match.

---

## Data and credits

The `mod2` datasets are free educational material from the
**[Gapminder Foundation](https://www.gapminder.org/data/)**, distributed under a
**[CC-BY](https://creativecommons.org/licenses/by/4.0/)** license:

| File | Content |
|:---|:---|
| `life_expectancy_years.csv` | Life expectancy by country, 1800–2100 |
| `population_total.csv` | Total population by country, 1800–2100 |
| `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` | GDP *per capita* PPP, inflation-adjusted |

The PDF subjects are the property of **[42 School](https://42.fr/)** and are
included only as context for whoever reads this repository.

---

## License and author

The code in this repository is distributed under the **MIT** license — see
[`mod0/ex09/LICENSE`](mod0/ex09/LICENSE).

**dpetrukh** · [42 Lisboa](https://www.42lisboa.com/) · `dpetrukh@student.42.fr`
· [github.com/DinisPetrukha](https://github.com/DinisPetrukha)
