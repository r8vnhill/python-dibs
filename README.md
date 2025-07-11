# DIBS Course Companion Repository

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/badge/build%20tool-uv-blue?logo=uv)](https://docs.astral.sh/uv/getting-started/)
[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](./LICENSE)
[![Educational](https://img.shields.io/badge/purpose-educational-yellow)](https://dibs.ravenhill.cl)
[![Status](https://img.shields.io/badge/status-stable-brightgreen)]()
[![DIBS Site](https://img.shields.io/badge/website-dibs.ravenhill.cl-purple)](https://dibs.ravenhill.cl)

This repository contains companion code for the course **"Diseño e Implementación de Bibliotecas de Software" (DIBS)**.

> [!note]
> While the course is taught in **Spanish**, the code and documentation here are in **English** to ensure clarity, accessibility, and alignment with broader software development conventions.

## 📖 Table of Contents

- [DIBS Course Companion Repository](#dibs-course-companion-repository)
  - [📖 Table of Contents](#-table-of-contents)
  - [🎓 Lessons](#-lessons)
  - [🧑‍💻 Getting Started](#-getting-started)
    - [Requirements](#requirements)
    - [Clone the Repository](#clone-the-repository)
  - [🛡️ License](#️-license)
  - [🌐 DIBS Website](#-dibs-website)

## 🎓 Lessons

This repository includes working examples and code fragments discussed in the following lessons from the DIBS course:

1. 📘 **[Variable Declarations](https://dibs.ravenhill.cl/docs/type-fundamentals/basics/variables/py)**: Learn how Python’s flexible approach to variables and properties enables rapid development, while also exploring the trade-offs it presents when building maintainable libraries.
2. 📘 **[Sum Types as Enumerations in Python](https://dibs.ravenhill.cl/docs/type-fundamentals/algebraic-data-types/enums/py/)**: Exploring how to model sum types using `Enum` and `match` in Python, introduced in Python 3.10.
3. 📘 **[Advanced Modeling with Enumerations](https://dibs.ravenhill.cl/docs/type-fundamentals/algebraic-data-types/idiom-enum/py)**: A deeper dive into using `Enum` for more complex data modeling scenarios.

More lessons will be added as the course progresses.

## 🧑‍💻 Getting Started

### Requirements

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/) for running the examples
- Recommended: [PyCharm](https://www.jetbrains.com/pycharm/) or any other Python IDE for a better development experience.

> For installation help, see the [setup guide](https://dibs.ravenhill.cl/docs/build-systems/init/uv).

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://gitlab.com/r8vnhill/python-dibs.git
cd python-dibs
```

To run the examples, you can use the `uv` command:

```bash
uv run <example_file.py>
```

> Replace `<example_file.py>` with the specific Python file you want to run.

For example:

```bash
uv run type-fundamentals/basics/main.py
```

## 🛡️ License

This project is licensed under the **[BSD 2-Clause License](./LICENSE)**.

You may use, adapt, and share this code freely for personal, academic, or educational purposes, as long as attribution is given.

## 🌐 DIBS Website

To access the full course (in Spanish), visit:
👉 [https://dibs.ravenhill.cl](https://dibs.ravenhill.cl)

There you'll find lesson explanations, exercises, and supporting materials.
