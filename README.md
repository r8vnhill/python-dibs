# DIBS Course Companion Repository

[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/downloads/)
[![Educational](https://img.shields.io/badge/purpose-educational-yellow)](https://dibs.pages.dev)
[![Build](https://img.shields.io/badge/status-stable-brightgreen)]()
[![DIBS Website](https://img.shields.io/badge/website-dibs.pages.dev-purple)](https://dibs.pages.dev)

This repository contains the companion code for the course **"Diseño e Implementación de Bibliotecas de Software" (DIBS)**.

The course is taught in **Spanish**, but this repository is written in **English** to make it accessible to a broader audience and to align with common programming conventions and documentation standards.

## 🔍 About

The code in this repository is designed to support the lessons from DIBS, focusing on practical and idiomatic usage of language features such as:

- Loops and control flow
- Comprehensions (lists, sets, dictionaries)
- Collection transformations and filtering
- Optional values and configuration logic
- Pythonic patterns for executable scripts

It also uses [`uv`](https://github.com/astral-sh/uv) as a fast and modern Python package manager to simplify running examples and managing environments. This is aligned with the course's goal of exploring clean build systems and reproducible development workflows.

All examples are intended for **educational purposes**, helping learners understand core concepts before applying them in larger systems or libraries.

## 📁 Project Structure

```text
type-fundamentals/
├── basics/
│   ├── __init__.py
│   ├── cycles.py        # Functions related to loops and data processing
│   └── main.py          # Script entry point (with idiomatic main guard)
├── pyproject.toml       # Metadata for this subproject
```

## 🧪 Usage

This project uses [`uv`](https://github.com/astral-sh/uv), a modern Python tool for dependency resolution and execution.

To try out the examples interactively:

```bash
uv run type-fundamentals/basics/cycles.py
```

To run the `main.py` entry point (used in the lesson on script structure):

```bash
uv run type-fundamentals/basics/main.py
```

This will print a reflective quote, demonstrating Python’s idiomatic `if __name__ == '__main__'` usage.

## 📝 License

This repository is released under the terms of the [BSD 2-Clause License](./LICENSE).

## 🤝 Contributing

Please review our [Code of Conduct](./CODE_OF_CONDUCT.md) before contributing.

---

For the full course content (in Spanish), refer to the [official DIBS website](https://dibs.pages.dev).
