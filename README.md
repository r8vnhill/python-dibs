# DIBS Course Companion Repository

[![License: BSD-2-Clause](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/downloads/)
[![Educational](https://img.shields.io/badge/purpose-educational-yellow)](https://dibs.pages.dev)
[![Build](https://img.shields.io/badge/status-stable-brightgreen)]()
[![DIBS Website](https://img.shields.io/badge/website-dibs.pages.dev-purple)](https://dibs.ravenhill.cl)

This repository contains companion code for the course **"Diseño e Implementación de Bibliotecas de Software" (DIBS)**.

>[!note]
> While the course is taught in **Spanish**, the code and documentation here are in **English** to ensure clarity, accessibility, and alignment with broader software development conventions.

---

## 🔍 About

This repository complements multiple lessons from the DIBS course, with a focus on writing **idiomatic, expressive, and reusable code** in Python. It showcases practical design techniques that are especially relevant when building libraries.

The repository includes examples covering:

- Loops, comprehensions, and functional combinators
- Variable binding and mutability (`Final`, `frozen=True`)
- Function declarations and idiomatic script entry points
- Data validation and type-safe modeling
- Pythonic patterns for configuration and control flow
- Usage of [`@dataclass`](https://docs.python.org/3/library/dataclasses.html) for product types (records)

It also uses [`uv`](https://github.com/astral-sh/uv) as a fast, modern Python package manager to streamline dependency management and execution — aligned with the course's goals on reproducibility and clean build systems.

All code is intended for **educational purposes** and designed to be lightweight, idiomatic, and easy to modify for experimentation.

---

## 📁 Project Structure

```text
type-fundamentals/
├── basics/
│   ├── __init__.py
│   ├── cycles.py              # Loops and iteration patterns
│   ├── functions.py           # Function declarations and behavior
│   ├── variables.py           # Variable binding, Final, mutability
│   └── main.py                # Idiomatic script entry point
├── algebraic_types/
│   └── product/
│       ├── comic.py           # Mutability and frozen dataclasses
│       ├── ghoul.py           # Immutability with replace()
│       ├── pokemon.py         # Properties and helper methods
│       ├── song.py            # Validation with __post_init__
│       ├── videogame.py       # Destructuring via astuple
│       └── __init__.py
├── pyproject.toml             # Project metadata
```

---

## 🧪 Usage

This project uses [`uv`](https://github.com/astral-sh/uv), a modern and fast Python package manager.

To run specific examples:

```bash
uv run type-fundamentals/basics/functions.py
uv run type-fundamentals/algebraic_types/product/ghoul.py
uv run type-fundamentals/algebraic_types/product/song.py
```

---

## 📝 License

This repository is licensed under the [BSD 2-Clause License](./LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please read our [Code of Conduct](./CODE_OF_CONDUCT.md) before submitting issues or pull requests.

---

For full course content (in Spanish), visit the [official DIBS site](https://dibs.ravenhill.cl).
