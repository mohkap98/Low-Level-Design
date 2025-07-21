# 🚗 Bridge Pattern – Car and Engine Example (Python)

This project demonstrates the **Bridge Design Pattern** using a car and engine abstraction. It decouples the `Car` abstraction from the `Engine` implementation so that both can vary independently.

---

## 🌉 What is the Bridge Pattern?

> The **Bridge Pattern** allows an abstraction and its implementation to vary independently. It is a structural design pattern that prevents a **combinatorial explosion** of subclasses when you need different variations of two (or more) dimensions.

---

## 🎯 Use Case

You want to build:

- Different types of **cars**: `Sedan`, `SUV`, etc.
- With different types of **engines**: `PetrolEngine`, `DieselEngine`, `ElectricEngine`

Instead of creating combinations like `SedanDiesel`, `SUVPetrol`, the **Bridge pattern** lets you **combine them dynamically**.

---

## 📐 UML (Mermaid.js)

```mermaid
classDiagram
    class Engine {
        <<interface>>
        +start()
    }

    class PetrolEngine {
        +start()
    }

    class DieselEngine {
        +start()
    }

    class ElectricEngine {
        +start()
    }

    class Car {
        -engine: Engine
        +drive()
    }

    class Sedan {
        +drive()
    }

    class SUV {
        +drive()
    }

    Engine <|.. PetrolEngine
    Engine <|.. DieselEngine
    Engine <|.. ElectricEngine

    Car <|-- Sedan
    Car <|-- SUV
    Car --> Engine : uses
