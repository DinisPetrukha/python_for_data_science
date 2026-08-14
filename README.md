# Python for Data Science — 42 Lisboa

> Piscine de especialização em Python e Data Science da 42 Lisboa.
> Cinco módulos, 29 exercícios, ~2000 linhas de Python 3.10 escritas sob a norm da 42.

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![flake8](https://img.shields.io/badge/flake8-passing-brightgreen)](#qualidade-de-código)
[![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)](https://matplotlib.org/)
[![Exercícios](https://img.shields.io/badge/exerc%C3%ADcios-29-blue)](#módulo-a-módulo)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](mod0/ex09/LICENSE)

---

## Sobre

A **Piscine Python for Data Science** é o percurso intensivo com que a [42 Lisboa](https://www.42lisboa.com/)
introduz Python a quem já domina C. Não há aulas nem professores: cada dia traz um
*subject* em PDF com um conjunto de exercícios, restrições explícitas e o output
esperado ao carácter. O trabalho é validado em **peer-evaluation** — outro estudante
corre o código na sua própria máquina e questiona cada decisão de implementação.

O interesse pedagógico do formato está nas restrições. Não basta que o programa
funcione: o *subject* proíbe bibliotecas para o problema central, obriga a
construções específicas (uma *list comprehension* aqui, um `yield` ali, um
decorador acolá) e invalida o exercício se uma única exceção escapar. O resultado
é que se reimplementa à mão aquilo que normalmente se importa — `filter`, `tqdm`,
a transposição de matrizes, o desvio-padrão — e só depois se ganha o direito de
usar a versão da biblioteca.

Este repositório é a minha resolução completa dos cinco módulos.

---

## Índice

- [Panorama dos módulos](#panorama-dos-módulos)
- [Competências demonstradas](#competências-demonstradas)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Regras e restrições da 42](#regras-e-restrições-da-42)
- [Módulo a módulo](#módulo-a-módulo)
  - [mod0 — Starting](#mod0--starting)
  - [mod1 — Array](#mod1--array)
  - [mod2 — DataTable](#mod2--datatable)
  - [mod3 — Oriented Object Programming](#mod3--oriented-object-programming)
  - [mod4 — Data Oriented Design](#mod4--data-oriented-design)
- [Como executar](#como-executar)
- [Qualidade de código](#qualidade-de-código)
- [Notas de design](#notas-de-design)
- [Dados e créditos](#dados-e-créditos)
- [Licença e autor](#licença-e-autor)

---

## Panorama dos módulos

| Módulo | Subject | Ex. | Stack | Conceito central |
|:---|:---|:---:|:---|:---|
| [`mod0`](mod0/) | *Starting* | 10 | stdlib, `tqdm`, `setuptools` | Fundamentos, `sys.argv`, geradores, empacotamento |
| [`mod1`](mod1/) | *Array* | 6 | `numpy`, `Pillow`, `matplotlib` | Arrays N-dimensionais e processamento de imagem |
| [`mod2`](mod2/) | *DataTable* | 4 | `pandas`, `matplotlib` | Carregamento, limpeza e visualização de datasets |
| [`mod3`](mod3/) | *Oriented Object Programming* | 5 | stdlib (`abc`) | Herança, MRO/C3, métodos mágicos, `property` |
| [`mod4`](mod4/) | *Data Oriented Design* | 4 | stdlib (`dataclasses`) | Closures, decoradores, `*args`/`**kwargs` |

---

## Competências demonstradas

Cada linha aponta para a implementação real no repositório.

### Python idiomático e funcional

| Conceito | Onde |
|:---|:---|
| *List comprehensions* como substituto de `filter` | [`mod0/ex06/ft_filter.py`](mod0/ex06/ft_filter.py) |
| Funções `lambda` e funções de primeira classe | [`mod0/ex06/filterstring.py`](mod0/ex06/filterstring.py) |
| Geradores e o operador `yield` | [`mod0/ex08/Loading.py`](mod0/ex08/Loading.py), [`generators.py`](mod0/ex08/generators.py) |
| Exaustão de geradores e geradores infinitos | [`mod0/ex08/generators.py`](mod0/ex08/generators.py) |
| Closures e `nonlocal` | [`mod4/ex01/in_out.py`](mod4/ex01/in_out.py) |
| Decoradores parametrizados (fábrica de 3 níveis) | [`mod4/ex02/callLimit.py`](mod4/ex02/callLimit.py) |
| `*args` / `**kwargs` com despacho por keyword | [`mod4/ex00/statistics.py`](mod4/ex00/statistics.py) |
| Introspeção: `__doc__`, `__dict__`, `__name__`, `mro()` | [`mod0/ex02`](mod0/ex02/find_ft_type.py), [`mod3/ex02`](mod3/ex02/DiamondTrap.py) |
| *Type hints* PEP 604 (`int \| float`, `list[float]`) | [`mod1/ex00/give_bmi.py`](mod1/ex00/give_bmi.py), [`mod3/ex04`](mod3/ex04/ft_calculator.py) |

### Programação orientada a objetos

| Conceito | Onde |
|:---|:---|
| Classes abstratas (`ABC`, `@abstractmethod`) | [`mod3/ex00/S1E9.py`](mod3/ex00/S1E9.py) |
| Herança e `super()` | [`mod3/ex01/S1E7.py`](mod3/ex01/S1E7.py) |
| `__repr__` / `__str__` | [`mod3/ex01/S1E7.py`](mod3/ex01/S1E7.py) |
| `@classmethod` como *factory* | [`mod3/ex01/S1E7.py`](mod3/ex01/S1E7.py) |
| Herança em diamante e linearização C3 | [`mod3/ex02/DiamondTrap.py`](mod3/ex02/DiamondTrap.py) |
| `property()` — getters/setters | [`mod3/ex02/DiamondTrap.py`](mod3/ex02/DiamondTrap.py) |
| Sobrecarga de operadores (`__add__`, `__truediv__`, …) | [`mod3/ex03/ft_calculator.py`](mod3/ex03/ft_calculator.py) |
| `@staticmethod` | [`mod3/ex04/ft_calculator.py`](mod3/ex04/ft_calculator.py) |
| `@dataclass`, `field(init=False)`, `__post_init__` | [`mod4/ex03/new_student.py`](mod4/ex03/new_student.py) |

### Data Science

| Conceito | Onde |
|:---|:---|
| Aritmética vetorizada em NumPy | [`mod1/ex00/give_bmi.py`](mod1/ex00/give_bmi.py) |
| Máscaras booleanas | [`mod1/ex00/give_bmi.py`](mod1/ex00/give_bmi.py) |
| *Slicing* multi-eixo e objetos `slice()` | [`mod1/ex01/array2D.py`](mod1/ex01/array2D.py), [`mod1/ex03/zoom.py`](mod1/ex03/zoom.py) |
| *Fancy indexing* sobre o eixo dos canais | [`mod1/ex05/pimp_image.py`](mod1/ex05/pimp_image.py) |
| Redução de eixo (`np.mean(axis=-1)`) | [`mod1/ex05/pimp_image.py`](mod1/ex05/pimp_image.py) |
| Transposição de matrizes implementada de raiz | [`mod1/ex04/rotate.py`](mod1/ex04/rotate.py) |
| Imagem → array via Pillow | [`mod1/ex02/load_image.py`](mod1/ex02/load_image.py) |
| I/O de CSV e indexação em pandas | [`mod2/ex00/load_csv.py`](mod2/ex00/load_csv.py) |
| Limpeza de dados (`'29M'` → `29000000.0`) | [`mod2/ex02/aff_pop.py`](mod2/ex02/aff_pop.py) |
| Seleção por rótulo (`.loc`) e `Series.apply` | [`mod2/ex02/aff_pop.py`](mod2/ex02/aff_pop.py) |
| Séries temporais, dispersão, escala logarítmica | [`mod2/ex01`](mod2/ex01/aff_life.py), [`mod2/ex03`](mod2/ex03/projection_life.py) |
| Estatística descritiva implementada de raiz | [`mod4/ex00/statistics.py`](mod4/ex00/statistics.py) |

### Engenharia de software

| Conceito | Onde |
|:---|:---|
| Empacotamento com `pyproject.toml` / `setuptools` | [`mod0/ex09/pyproject.toml`](mod0/ex09/pyproject.toml) |
| `__init__.py`, imports relativos, `__all__` | [`mod0/ex09/ft_package/__init__.py`](mod0/ex09/ft_package/__init__.py) |
| Distribuição instalável por `pip` (wheel + sdist) | [`mod0/ex09/README.md`](mod0/ex09/README.md) |
| Tratamento de erros sem exceções por apanhar | transversal |
| Renderização em terminal com `\r` e `os.get_terminal_size` | [`mod0/ex08/Loading.py`](mod0/ex08/Loading.py) |
| Conformidade com linter (flake8 / PEP 8) | [ver secção](#qualidade-de-código) |

---

## Estrutura do repositório

Cada exercício é um diretório autónomo e executável — regra imposta pela 42, que
avalia cada `ex` isoladamente.

```
python_for_data_science/
├── en.subject python.pdf              # apresentação geral da piscine
│
├── mod0/  Starting                    # fundamentos, CLI, geradores, packaging
│   ├── ex00/  Hello.py                # list, tuple, set, dict
│   ├── ex01/  format_ft_time.py       # time, strftime, format specs
│   ├── ex02/  find_ft_type.py         # introspeção de tipos
│   ├── ex03/  NULL_not_found.py       # None, NaN, 0, "", False
│   ├── ex04/  whatis.py               # sys.argv, assert
│   ├── ex05/  building.py             # análise de strings, stdin
│   ├── ex06/  ft_filter.py            # filter reimplementado
│   │          filterstring.py         # lambda + list comprehension
│   ├── ex07/  sos.py                  # codificador de Morse
│   ├── ex08/  Loading.py              # ft_tqdm — gerador com barra
│   │          generators.py           # laboratório de geradores
│   └── ex09/  ft_package/             # pacote Python instalável
│              pyproject.toml, LICENSE, README.md
│
├── mod1/  Array                       # NumPy e imagem
│   ├── ex00/  give_bmi.py             # vetorização, máscaras booleanas
│   ├── ex01/  array2D.py              # shape, slicing 2D
│   ├── ex02/  load_image.py           # Pillow → np.array
│   ├── ex03/  zoom.py                 # crop centrado + escala de cinzentos
│   ├── ex04/  rotate.py               # transposição manual
│   └── ex05/  pimp_image.py           # 5 filtros de cor
│
├── mod2/  DataTable                   # pandas + matplotlib (Gapminder)
│   ├── ex00/  load_csv.py             # carregamento robusto de CSV
│   ├── ex01/  aff_life.py             # esperança de vida em Portugal
│   ├── ex02/  aff_pop.py              # população: Portugal vs França
│   └── ex03/  projection_life.py      # PIB vs esperança de vida, 1900
│
├── mod3/  Oriented Object Programming # Game of Thrones como caso de estudo
│   ├── ex00/  S1E9.py                 # Character (ABC) + Stark
│   ├── ex01/  S1E7.py                 # Baratheon, Lannister, classmethod
│   ├── ex02/  DiamondTrap.py          # King(Baratheon, Lannister) — C3
│   ├── ex03/  ft_calculator.py        # sobrecarga de operadores
│   └── ex04/  ft_calculator.py        # produto escalar via staticmethod
│
└── mod4/  Data Oriented Design        # Python funcional
    ├── ex00/  statistics.py           # estatística de raiz
    ├── ex01/  in_out.py               # closures e nonlocal
    ├── ex02/  callLimit.py            # decorador parametrizado
    └── ex03/  new_student.py          # dataclass
```

Cada módulo inclui o respetivo `en.subject*.pdf`. Os ficheiros `tester.py` são
bancos de ensaio meus — a 42 não os avalia, mas são a ferramenta usada na defesa.

---

## Regras e restrições da 42

O código deste repositório obedece às regras dos *subjects*. Valem a pena
explicitar-se, porque explicam decisões que de outra forma pareceriam arbitrárias:

- **Python 3.10** obrigatório.
- **Zero variáveis globais.**
- **Nenhum código no *global scope*.** Todo o programa tem `main()` e a guarda
  `if __name__ == "__main__": main()`.
- **`__doc__` obrigatório** em cada função, classe e método.
- **Imports explícitos.** `import numpy as np` é obrigatório; `from pandas import *`
  vale **0** no exercício.
- **Nenhuma exceção pode escapar** — nem sequer nos casos de erro que o subject
  manda testar. Uma exceção não apanhada invalida o exercício.
- **Conformidade com a norm**, que na 42 significa `flake8` sem avisos.

Daqui nasce um idioma de tratamento de erros usado de forma uniforme em todo o
repositório: a asserção descreve a pré-condição, o `try` garante que nada escapa,
e erros de outros tipos são traduzidos para `AssertionError` para uniformizar a
mensagem ao utilizador.

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

## Módulo a módulo

### mod0 — *Starting*

> *"Today, you will learn the basics of the Python programming language."*

Do primeiro `print` até um pacote instalável por `pip`. A meio do módulo — logo a
seguir ao `ex04` — o *subject* introduz as regras adicionais (`main()`, docstrings,
flake8), e o estilo do código muda visivelmente a partir daí.

| Ex | Ficheiro | O que faz | Conceito-chave |
|:---:|:---|:---|:---|
| 00 | [`Hello.py`](mod0/ex00/Hello.py) | Muta os quatro contentores base e imprime-os | `list`, `tuple`, `set`, `dict` e mutabilidade |
| 01 | [`format_ft_time.py`](mod0/ex01/format_ft_time.py) | Epoch com separador de milhares e notação científica | `time`, `strftime`, format specs (`,.4f`, `.2e`) |
| 02 | [`find_ft_type.py`](mod0/ex02/find_ft_type.py) | Imprime o tipo do objeto e devolve 42 | Introspeção via `type()` e `__name__` |
| 03 | [`NULL_not_found.py`](mod0/ex03/NULL_not_found.py) | Distingue as cinco formas de "nada" em Python | Semântica de `None`, `NaN`, `0`, `""`, `False` |
| 04 | [`whatis.py`](mod0/ex04/whatis.py) | Par ou ímpar, a partir de um argumento CLI | `sys.argv`, `assert`, tradução de exceções |
| 05 | [`building.py`](mod0/ex05/building.py) | Conta maiúsculas, minúsculas, pontuação, dígitos e espaços | `string.punctuation`, predicados `str.is*`, `stdin` |
| 06 | [`ft_filter.py`](mod0/ex06/ft_filter.py) · [`filterstring.py`](mod0/ex06/filterstring.py) | Reimplementa `filter` e filtra palavras por comprimento | *List comprehension*, `lambda` |
| 07 | [`sos.py`](mod0/ex07/sos.py) | Codifica uma string em código Morse | Dicionário como tabela de conversão |
| 08 | [`Loading.py`](mod0/ex08/Loading.py) | Reimplementa `tqdm` | Geradores, `yield`, controlo de terminal |
| 09 | [`ft_package/`](mod0/ex09/) | Pacote publicável e instalável | `pyproject.toml`, `setuptools`, `__all__` |

#### Destaque — `ex06`: reimplementar `filter`

O *subject* exige que `ft_filter.__doc__` devolva o mesmo que `filter.__doc__` e
que a recodificação use uma *list comprehension*. Repare-se no ramo `func is None`,
que replica o comportamento pouco conhecido do `filter` original: sem função, o que
sobrevive é o que for *truthy*.

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

#### Destaque — `ex08`: um `tqdm` escrito à mão

A única biblioteca autorizada é `os`. A barra é um **gerador**: entrega o elemento
ao chamador com `yield` e, a cada iteração, reescreve a linha com `\r`. A largura
útil é calculada a partir de `os.get_terminal_size()` menos o espaço ocupado pela
moldura, para que a barra se adapte a qualquer terminal.

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

O acompanhamento em [`generators.py`](mod0/ex08/generators.py) explora o resto do
tema: a exaustão de um gerador ao segundo `for`, `next()` e geradores infinitos.

#### Destaque — `ex09`: um pacote a sério

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

Uma imagem é um `np.array` de forma `(altura, largura, canais)`. Todo o módulo
explora essa identidade: recortar é *slicing*, isolar uma cor é indexar o último
eixo, converter para cinzentos é reduzi-lo.

| Ex | Ficheiro | O que faz | Conceito-chave |
|:---:|:---|:---|:---|
| 00 | [`give_bmi.py`](mod1/ex00/give_bmi.py) | IMC vetorizado + limiar booleano | Vetorização, máscaras booleanas |
| 01 | [`array2D.py`](mod1/ex01/array2D.py) | Imprime `shape` e trunca por *slicing* | Objetos `slice()`, validação de matrizes |
| 02 | [`load_image.py`](mod1/ex02/load_image.py) | Carrega JPG/JPEG para `np.array` | Pillow, tratamento de erros por tipo |
| 03 | [`zoom.py`](mod1/ex03/zoom.py) | Recorte centrado 400×400 em escala de cinzentos | *Slicing* multi-eixo |
| 04 | [`rotate.py`](mod1/ex04/rotate.py) | Transpõe a imagem **sem biblioteca** | Transposição manual, `np.zeros` |
| 05 | [`pimp_image.py`](mod1/ex05/pimp_image.py) | Cinco filtros de cor | *Fancy indexing*, *broadcasting*, redução de eixo |

#### Destaque — `ex00`: vetorização em vez de ciclos

```console
$ python3 tester.py
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
```

O IMC é calculado de uma vez para todo o vetor, e o limiar produz diretamente um
array de booleanos — sem um único `for`.

#### Destaque — `ex04`: transposição proibida de importar

> *"You have to do the transpose yourself, no library is allowed for the transpose."*

Sem `.T`, sem `np.transpose`. Aloca-se o destino com o `dtype` preservado e
percorrem-se os dois eixos, trocando os índices e colapsando o eixo dos canais:

```python
def transpose(img: np.array) -> np.array:
    """..."""
    height, width = img.shape[0], img.shape[1]
    transposed_img = np.zeros((height, width), dtype=img.dtype)

    for y in range(height):
        for x in range(width):
            transposed_img[x][y] = img[y][x][0]
```

#### Destaque — `ex05`: filtros sob restrição de operadores

O *subject* limita os operadores permitidos por filtro — `invert` pode usar
`= + - *`, `red` apenas `= *`, `green` apenas `= -`, `blue` apenas `=`, e `grey`
apenas `= /`. A restrição força a pensar em termos de *broadcasting* e de indexação
de eixos, e não em ciclos sobre píxeis.

```python
def ft_invert(img: np.array):
    """Inverts the color of the image received."""
    return_img = 255 - img          # broadcasting sobre todo o array

def ft_green(img: np.array):
    """Applies a green filter by setting blue and red channels to zero."""
    return_img = img.copy()         # .copy() para não mutar a origem
    return_img[:, :, [0, 2]] = 0    # fancy indexing no eixo dos canais

def ft_grey(img: np.array):
    return_img = np.mean(img, axis=-1)   # redução do eixo dos canais
```

---

### mod2 — *DataTable*

> *"Today, you will learn how to load, manipulate and display data table."*

Dados reais da [Gapminder](https://www.gapminder.org/) em formato largo — uma
linha por país, uma coluna por ano, de 1800 a 2100.

| Ex | Ficheiro | O que faz | Conceito-chave |
|:---:|:---|:---|:---|
| 00 | [`load_csv.py`](mod2/ex00/load_csv.py) | Carrega o CSV, indexa por país, devolve `None` em erro | `read_csv`, `set_index`, `.shape` |
| 01 | [`aff_life.py`](mod2/ex01/aff_life.py) | Esperança de vida em Portugal ao longo de 3 séculos | `.loc`, série temporal |
| 02 | [`aff_pop.py`](mod2/ex02/aff_pop.py) | População de Portugal vs França, 1800–2050 | Limpeza de dados, `Series.apply`, legendas |
| 03 | [`projection_life.py`](mod2/ex03/projection_life.py) | PIB *per capita* vs esperança de vida em 1900 | Dispersão, escala logarítmica, junção por índice |

#### Destaque — `ex00`: carregamento que nunca rebenta

O contrato do *subject* é claro: devolver `None` se o caminho for mau, se o formato
for mau, se o que quer que seja correr mal.

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

Os *fixtures* de teste estão no repositório e são deliberados: [`test.csv`](mod2/ex00/test.csv)
está vazio, e [`life_expectancy_years copy.csv`](mod2/ex00/) é idêntico ao original
exceto no cabeçalho — `pais` em vez de `country` — para exercitar o ramo em que a
coluna de índice não existe.

#### Destaque — `ex02`: os dados vêm sujos

A Gapminder escreve a população como `'29M'`, `'10k'`, `'1.4B'`. Antes de plotar,
é preciso normalizar tudo para `float`:

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
df_subset = df.loc[:, "1800":"2050"]           # slicing de colunas por rótulo
campus_data = df_subset.loc["France"].apply(clean_pop)
other_data = df_subset.loc["Portugal"].apply(clean_pop)
```

#### Destaque — `ex03`: a pergunta do subject

> *"Do you see a correlation between lifespan and gross domestic product?"*

O gráfico cruza dois datasets pelo índice comum (o país) e usa escala logarítmica
no eixo do PIB — sem ela, a nuvem de pontos colapsa contra o eixo, porque o
rendimento distribui-se por ordens de grandeza e não linearmente.

```python
plt.scatter(df_income["1900"], df_life["1900"])
plt.xscale("log")
plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
```

A resposta lê-se no gráfico: a correlação existe e é positiva, mas é **logarítmica**
— duplicar o rendimento dos países mais pobres compra muitos mais anos de vida do
que duplicar o dos mais ricos.

---

### mod3 — *Oriented Object Programming*

> *"Today, you will see the classes and the heritage."*

O *subject* abre com um aviso: a queixa habitual sobre cientistas de dados é que
escrevem mau código, porque ignoram a orientação a objetos. O módulo usa *Game of
Thrones* como domínio.

| Ex | Ficheiro | O que faz | Conceito-chave |
|:---:|:---|:---|:---|
| 00 | [`S1E9.py`](mod3/ex00/S1E9.py) | `Character` abstrata + `Stark` | `ABC`, `@abstractmethod` |
| 01 | [`S1E7.py`](mod3/ex01/S1E7.py) | `Baratheon` e `Lannister` | `super()`, `__repr__`/`__str__`, `@classmethod` |
| 02 | [`DiamondTrap.py`](mod3/ex02/DiamondTrap.py) | `King(Baratheon, Lannister)` | Herança em diamante, C3, `property()` |
| 03 | [`ft_calculator.py`](mod3/ex03/ft_calculator.py) | Vetor com escalar | `__add__`, `__mul__`, `__sub__`, `__truediv__` |
| 04 | [`ft_calculator.py`](mod3/ex04/ft_calculator.py) | Produto escalar entre vetores | `@staticmethod`, `zip` |

#### Destaque — `ex01`: `@classmethod` como construtor alternativo

`cls` — e não o nome literal da classe — é o que faz o *factory* continuar correto
em qualquer subclasse:

```python
@classmethod
def create_lannister(cls, first_name: str, is_alive: bool = True):
    """Factory method to create a Lannister instance."""
    return cls(first_name, is_alive)
```

#### Destaque — `ex02`: a armadilha do diamante

Joffrey Baratheon é herdeiro das duas casas. Em Python, `King(Baratheon, Lannister)`
levanta a questão de qual `__init__` corre e de onde vêm os atributos — o problema
que a **linearização C3** resolve desde o Python 2.3.

O detalhe fino está nos *setters*. Se `set_eyes` fizesse `self.eyes = color`, e
`eyes` é uma `property` cujo *setter* é o próprio `set_eyes`, o resultado seria
recursão infinita. Escrever diretamente em `self.__dict__` contorna o protocolo de
descritores e resolve o problema:

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

O `main()` imprime a MRO para tornar a linearização visível:

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

Lê-se ali porque é que Joffrey nasce de olhos castanhos: `Baratheon` precede
`Lannister` na MRO, logo é o seu `__init__` que prevalece.

#### Destaque — `ex03` e `ex04`: os dois calculadores

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

O `ex03` faz sobrecarga de operadores sobre uma instância; o `ex04` responde a uma
pista do *subject* — *"find a decorator that can help you to use the Methods
without instantiating this class"* — com `@staticmethod` e `zip`:

```python
@staticmethod
def dotproduct(V1: list[float], V2: list[float]) -> None:
    """..."""
    print(f"Dot product is: {sum([it[0] * it[1] for it in zip(V1, V2)])}")
```

---

### mod4 — *Data Oriented Design*

> *"Today, you will see some Structure Design."*

Python funcional: funções que recebem funções, funções que devolvem funções e
funções que se lembram do que aconteceu antes.

| Ex | Ficheiro | O que faz | Conceito-chave |
|:---:|:---|:---|:---|
| 00 | [`statistics.py`](mod4/ex00/statistics.py) | Média, mediana, quartis, desvio-padrão e variância | `*args`/`**kwargs`, despacho por keyword |
| 01 | [`in_out.py`](mod4/ex01/in_out.py) | Contador com estado preservado entre chamadas | Closures, `nonlocal` |
| 02 | [`callLimit.py`](mod4/ex02/callLimit.py) | Bloqueia uma função acima de N chamadas | Decorador parametrizado |
| 03 | [`new_student.py`](mod4/ex03/new_student.py) | Aluno com login e ID derivados | `@dataclass`, `field(init=False)` |

#### Destaque — `ex00`: estatística sem bibliotecas

Nem `statistics`, nem `numpy`. Tudo derivado dos argumentos posicionais, e o que
é calculado é decidido pelos **valores** dos argumentos nomeados — não pelas suas
chaves, que o *subject* deliberadamente enche de lixo (`toto=`, `tutu=`, `tata=`).

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

O terceiro bloco é vazio de propósito — as *keywords* não correspondem a nenhuma
operação conhecida, portanto nada é calculado e nada rebenta. O quarto imprime
`ERROR` três vezes: há operações pedidas mas não há dados sobre que operar.

#### Destaque — `ex02`: decorador com parâmetro

Três níveis de aninhamento, porque é isso que um decorador parametrizado é:
`callLimit(3)` **devolve** o decorador, que **devolve** a função embrulhada. O
contador vive na closure — `global` é proibido pelo *subject*.

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

#### Destaque — `ex03`: dataclass com campos derivados

O *subject* proíbe escrever `__str__` e `__repr__`, e exige que `login` e `id`
sejam impossíveis de passar ao construtor. `field(init=False)` remove-os da
assinatura gerada; `__post_init__` calcula-os depois:

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

## Como executar

**Requisitos:** Python 3.10 ou superior.

```bash
git clone https://github.com/DinisPetrukha/python_for_data_science.git
cd python_for_data_science
pip install numpy pandas matplotlib Pillow tqdm
```

Cada exercício é autónomo e espera ser executado **a partir do seu próprio
diretório** — as imagens, os CSV e os módulos importados são resolvidos por
caminho relativo:

```bash
cd mod0/ex08 && python3 tester.py        # comparação ft_tqdm vs tqdm
cd mod1/ex05 && python3 pimp_image.py    # gera invert/red/green/blue/grey.png
cd mod2/ex03 && python3 projection_life.py
cd mod3/ex02 && python3 DiamondTrap.py
cd mod4/ex00 && python3 statistics.py
```

Os exercícios de `mod1` e `mod2` gravam os gráficos em PNG no diretório de trabalho
(`zoom_output.png`, `pop_comparison.png`, `projection_1900.png`, …). Esses ficheiros
não estão versionados: são gerados na execução.

**Instalar o pacote do `mod0/ex09`:**

```bash
cd mod0/ex09
pip install build
python3 -m build                              # gera dist/
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
pip show -v ft_package
```

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))   # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))   # 0
```

---

## Qualidade de código

Na 42, a norm de Python é `flake8` sem avisos.

```bash
pip install flake8
python3 -m flake8 .
```

**Todos os ficheiros entregues a partir de `mod0/ex05` passam com zero avisos** —
o que abrange os módulos `mod1` a `mod4` na íntegra.

A exceção são os cinco primeiros exercícios do `mod0` (`ex00`–`ex04`), e a razão é
o próprio *subject*: as regras da norm só aparecem no Capítulo VII, sob o título
*"From now on you must follow these additional rules"*, **depois** do `ex04`. Esses
ficheiros ficam como estão, porque documentam a progressão do módulo. Os poucos
avisos restantes estão em ficheiros `tester.py`, que a 42 não avalia.

Para verificar o âmbito coberto pelo badge:

```bash
python3 -m flake8 . | grep -v tester.py | grep -v "mod0/ex0[0-4]"
# sem output
```

---

## Notas de design

**Duplicação deliberada de ficheiros.** [`load_csv.py`](mod2/ex00/load_csv.py)
aparece quatro vezes, [`S1E9.py`](mod3/ex00/S1E9.py) três, `load_image.py` quatro.
Não é descuido: a 42 avalia cada diretório `exNN` isoladamente, e o *subject*
enumera explicitamente os ficheiros anteriores como "*Files to turn in: Files from
previous exercises + …*". Cada exercício tem de correr sozinho.

Nem todas as cópias são iguais, aliás. `load_image.py` evolui com o exercício que
serve: no `mod1/ex04` incorpora também a função `zoom`, e no `mod1/ex05` imprime
o array além da forma. É a mesma função, adaptada ao que cada programa precisa.

**Tratamento de erros uniforme.** O `assert` documenta a pré-condição, o `try`
garante que nada escapa, e erros de outras origens são traduzidos para
`AssertionError` para que a mensagem ao utilizador seja consistente. Isto responde
diretamente à regra de que qualquer exceção não apanhada invalida o exercício.

**Reimplementar antes de importar.** `ft_filter` em vez de `filter`, `ft_tqdm` em
vez de `tqdm`, `transpose` em vez de `.T`, variância e desvio-padrão em vez de
`statistics`. Em vários casos os *subjects* mandam correr as duas versões lado a
lado — a de biblioteca é a especificação a que a implementação manual tem de
corresponder.

---

## Dados e créditos

Os datasets do `mod2` são material educativo livre da
**[Gapminder Foundation](https://www.gapminder.org/data/)**, distribuído sob
licença **[CC-BY](https://creativecommons.org/licenses/by/4.0/)**:

| Ficheiro | Conteúdo |
|:---|:---|
| `life_expectancy_years.csv` | Esperança de vida por país, 1800–2100 |
| `population_total.csv` | População total por país, 1800–2100 |
| `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` | PIB *per capita* PPP, ajustado à inflação |

Os *subjects* em PDF são propriedade da **[42 School](https://42.fr/)** e estão
incluídos apenas como contexto para quem lê este repositório.

---

## Licença e autor

O código deste repositório é distribuído sob licença **MIT** — ver
[`mod0/ex09/LICENSE`](mod0/ex09/LICENSE).

**dpetrukh** · [42 Lisboa](https://www.42lisboa.com/) · `dpetrukh@student.42.fr`
· [github.com/DinisPetrukha](https://github.com/DinisPetrukha)
