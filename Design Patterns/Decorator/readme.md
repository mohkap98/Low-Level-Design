# 📣 Decorator Pattern – Notification System (Python)

This project demonstrates the **Decorator Design Pattern** using a flexible notification system, where each notifier (like Email, SMS, Slack) wraps another notifier and adds its own behavior.

---

## 🧠 What is the Decorator Pattern?

> The **Decorator Pattern** allows you to dynamically add behavior to objects without modifying their original class. It follows the **Open/Closed Principle** – open for extension, closed for modification.

---

## 📦 Use Case

A `BaseNotifier` sends a basic notification.  
You can decorate it with layers like:

- 📧 `Email`
- 📱 `SMS`
- 💬 `Slack`

Each one wraps the existing notifier and adds to the `send()` behavior.

---

## 📐 UML (Mermaid.js)

```mermaid
classDiagram
    class Notifier {
        +send(msg)
    }

    class BaseNotifier {
        +send(msg)
    }

    class Decorator {
        -notifier: Notifier
        +send(msg)
    }

    class Email {
        +send(msg)
    }

    class SMS {
        +send(msg)
    }

    class Slack {
        +send(msg)
    }

    Notifier <|-- BaseNotifier
    Notifier <|-- Decorator
    Decorator <|-- Email
    Decorator <|-- SMS
    Decorator <|-- Slack
    Email --> Notifier
    SMS --> Notifier
    Slack --> Notifier
