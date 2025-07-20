# 💬 ChatRoom - Mediator Design Pattern in Python

## 🧩 Overview

This project demonstrates the **Mediator Design Pattern** through a `ChatRoom` example where multiple `User` instances communicate **indirectly** via a central `ChatRoom` (the Mediator).

Instead of users sending messages directly to each other, they **delegate the communication to the mediator** — promoting **loose coupling** and centralizing interaction logic.

---

## 🎯 Problem It Solves

Without a mediator, each user needs a reference to all other users, causing:

- Tight coupling
- Complex dependency management
- Code that's hard to extend or modify

The Mediator pattern **decouples** communication, making the system more maintainable and scalable.

---
## 📐 UML Diagram (Mermaid.js)

```mermaid
classDiagram
    class Mediator {
        <<interface>>
        +send_message(sender, message)
    }

    class ChatRoom {
        +users: dict
        +register(user)
        +send_message(sender, message)
    }

    class Colleague {
        -name
    }

    class User {
        +mediator: Mediator
        +send(msg)
        +receive(sender, msg)
    }

    Mediator <|.. ChatRoom
    Colleague <|-- User
    ChatRoom o-- User : registers
    User --> Mediator : uses
