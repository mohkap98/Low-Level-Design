# 🤖 Strategy Design Pattern — Payment System (Python)

---

## 📘 Overview

The **Strategy Pattern** is a behavioral design pattern that enables selecting an algorithm's behavior at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.

Rather than using conditionals to switch behavior, you **delegate behavior to a strategy object** that implements a shared interface.

---

## 🎯 Problem It Solves

- Eliminates the need for long `if-else` or `switch` statements
- Allows the behavior of a class to be changed at runtime
- Promotes open/closed design — add new behaviors without modifying existing code

---

## 🧱 UML Diagram

```mermaid
classDiagram
    class PaymentStrategy {
        <<interface>>
        +pay(amount)
    }

    PaymentStrategy <|-- UPI
    PaymentStrategy <|-- PayPal
    PaymentStrategy <|-- CreditCard

    class PaymentProcessor {
        -strategy: PaymentStrategy
        +pay(amount)
    }

    PaymentProcessor --> PaymentStrategy : uses
