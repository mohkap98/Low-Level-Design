# 🏗️ Builder Design Pattern in Python

The **Builder Pattern** is a creational design pattern used to construct complex objects step-by-step. Unlike telescoping constructors, it provides a clear and flexible way to create objects with many optional parameters.

---

## 📌 Problem It Solves

In scenarios where object construction becomes complicated due to many parameters (some required, some optional), using constructors directly can lead to code that's:

- ❌ Hard to read  
- ❌ Difficult to scale  
- ❌ Easy to misuse  

This is especially true when optional fields are passed as positional arguments — it’s easy to mix things up.

---

## 🧱 The Telescoping Constructor Problem

When you overload constructors to handle different combinations of parameters:

```python
# Simulated in Python (not truly overloaded)
computer = Computer("Intel i7", "16GB", "512GB SSD", None, "Linux", True)

classDiagram
    class Computer {
        +cpu: str
        +ram: str
        +storage: str
        +graphics_card: str
        +os: str
        +wifi: bool
    }

    class ComputerBuilder {
        -computer: Computer
        +with_storage(str): ComputerBuilder
        +with_graphics_card(str): ComputerBuilder
        +with_OS(str): ComputerBuilder
        +enable_wifi(bool): ComputerBuilder
        +build(): Computer
    }

    ComputerBuilder --> Computer : builds

