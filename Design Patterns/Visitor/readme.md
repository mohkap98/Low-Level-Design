# 🧮 Visitor Pattern: Shape Area Calculator in Python

This project demonstrates the **Visitor Design Pattern** by calculating the **area of different shapes** (`Circle`, `Rectangle`) without modifying their classes — keeping data and operations decoupled.

---

## 🧠 What is the Visitor Pattern?

The **Visitor Pattern** lets you define a new operation (like calculating area or exporting SVG) on a set of objects **without changing their structure**.

Instead of putting the logic inside the `Shape` classes, you create a separate `Visitor` class and let each shape **accept** the visitor.

---

## 📐 UML Diagram (Mermaid.js)

```mermaid
classDiagram
    class Shape {
        <<abstract>>
        +accept(visitor)
    }

    class Circle {
        -radius
        +accept(visitor)
    }

    class Rectangle {
        -length
        -width
        +accept(visitor)
    }

    class Visitor {
        <<interface>>
        +visit_circle(circle)
        +visit_rectangle(rectangle)
    }

    class AreaVisitor {
        +visit_circle(circle)
        +visit_rectangle(rectangle)
    }

    Shape <|-- Circle
    Shape <|-- Rectangle
    Visitor <|-- AreaVisitor
    Circle --> Visitor : accept
    Rectangle --> Visitor : accept
