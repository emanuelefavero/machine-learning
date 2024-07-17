# Machine Learning

This repository contains code for various machine learning concepts and algorithms. The code is written in Python and uses libraries such as NumPy, Pandas and Scikit-learn.

## Installation

> Note: Make sure you have Python 3.6 or higher installed on your system before proceeding with the installation

- Clone the repository
- Create a virtual environment using `python -m venv venv`
- Activate the virtual environment using `source venv/bin/activate`
- Upgrade pip using `pip install --upgrade pip`
- Install the required libraries using `pip install -r requirements.txt`

> Note: If you add any new library with `python -m pip install {library}`, please update the requirements.txt file using `pip freeze > requirements.txt`

## Usage

- Run any python file from the root directory using `python {folder}/{file}`
- Example: `python basics/statistics-basics.py`

> Tip: You can also use `nodemon` to automatically restart the output whenever you make changes to the file. Install nodemon using `npm install -g nodemon` and run the python file using `nodemon --exec python {folder}/{file}`

## Table of Contents

### Basics

- [Statistics Basics](basics/statistics-basics.py)

### Numpy

- [Array Create](numpy/array-create.py)
- [Array Iterate](numpy/array-iterate.py)
- [Array Reshape](numpy/array-reshape.py)
- [Array Slicing](numpy/array-slicing.py)
- [Array](numpy/array.py)
- [Basics](numpy/basics.py)
- [Copy vs View](numpy/copy-vs-view.py)
- [Data Types](numpy/data-types.py)

### Pandas

- [Manipulate Data](pandas/manipulate-data.py)
- [Read Data](pandas/read-data.py)

## License

- [MIT](LICENSE.md)
