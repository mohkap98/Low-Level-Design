# 🚘 Abstract Factory Design Pattern – Car Dealership Example

---

## 📘 Overview

The **Abstract Factory Pattern** is a creational design pattern that provides an interface for creating **families of related or dependent objects** without specifying their concrete classes.

This pattern is useful when the system needs to be **independent of how its objects are created**, composed, and represented.

---

## 💡 Real-World Analogy: Car Dealership

A car dealership can sell vehicles from **multiple brands**. Each brand offers a **Car** and a **Bike**. Instead of hardcoding brand logic, we use factories to abstract the creation process.

| Brand    | Car         | Bike         |
|----------|-------------|--------------|
| BMW      | BMWCar      | BMWBike      |
| Maruti   | MarutiCar   | MarutiBike   |

Using **Abstract Factory**, we ensure that:
- Clients (like the dealership) don't need to know the brand-specific classes.
- We can switch the whole family of products easily (e.g., from BMW to Maruti).

---

## 🧱 UML Diagram

```mermaid
classDiagram
    class VehicleFactory {
        <<interface>>
        +create_car()
        +create_bike()
    }

    class BMWFactory {
        +create_car()
        +create_bike()
    }

    class MarutiFactory {
        +create_car()
        +create_bike()
    }

    class Car {
        <<interface>>
        +drive()
    }

    class Bike {
        <<interface>>
        +ride()
    }

    class BMWCar {
        +drive()
    }

    class BMWBike {
        +ride()
    }

    class MarutiCar {
        +drive()
    }

    class MarutiBike {
        +ride()
    }

    class Dealership {
        -car: Car
        -bike: Bike
        +showroom()
    }

    VehicleFactory <|-- BMWFactory
    VehicleFactory <|-- MarutiFactory

    Car <|-- BMWCar
    Car <|-- MarutiCar

    Bike <|-- BMWBike
    Bike <|-- MarutiBike

    Dealership --> Car
    Dealership --> Bike
