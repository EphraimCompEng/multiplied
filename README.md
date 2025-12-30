# MultiPy

A powerful tool to build, test, and analyse multiplier designs.


# Why?

Generating and analysing multiplier designs by hand is labour intensive, even for small datasets, for entire [truth tables](https://en.wikipedia.org/wiki/Truth_table), this is close to impossible.

MultiPy provides tools for:

- Building partial product reduction layers
- Generating truth tables for custom algorithms
- Analysis, plotting, and finding trends across a dataset(s)
- Fine-grain access to bits, words or stages when building or analysing


# Documentation

Documentation continues to grow as the project progresses, including usage, general theory and implementations of algorithms using MultiPy.

For more information head to [/docs/](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs). 

<!--- [Installation](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs/installation.md)
- [Usage](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs/usage.md)
- [API Reference](https://github.com/EphraimCompEng/multiplier-lab/tree/master/docs/api_reference.md)-->


<!--
Use [sphinx](https://www.sphinx-doc.org/en/master/)?
-->


# Setup

### PIP
```
pip install multipy
```

```
<how to install module from source>
```

```Python3
>>> import multipy as mp
```

# Dependencies

| database | math    | visualization |
|:-------- |:------- |:------------- |
| [Parquet](https://github.com/apache/parquet-format)  | [NumPy](https://numpy.org/)   | [Matplotlib](https://matplotlib.org/ )   |
| [Pandas](https://pandas.pydata.org/)                 |                               |                                          |

Full list TBD.
