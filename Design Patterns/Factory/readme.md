# 🏭 Factory Method Design Pattern

---

## 📘 Overview

The **Factory Method Pattern** is a **creational design pattern** used to define an interface for creating an object, but allows subclasses or separate classes (factories) to decide which class to instantiate.

It enables a class to delegate instantiation to subclasses or factories, following the **Open/Closed Principle** — open for extension but closed for modification.

---

## 🎯 Problem It Solves

- You have a superclass or interface, and you want to allow clients to instantiate its subclasses **without knowing the exact class name**.
- You want to **decouple object creation from its usage**, especially if instantiation logic can change or needs to support multiple variants.
- You want your system to be **easily extensible** — e.g., plug in new types without modifying the core logic.

---

## 🚀 When To Use

- The exact class to instantiate is determined at **runtime**.
- You want to delegate the responsibility of instantiation to a child class or external factory.
- Object creation code is **complex, repeated**, or likely to change.
- You want to **scale** your application with plug-and-play modules (e.g., new notification types, payment methods, document readers, etc.).

---

## 🧱 UML Diagram (Mermaid)

```mermaid
classDiagram
    class NotificationService {
        +get_type()
        +send()
    }

    NotificationService <|-- EmailNotification
    NotificationService <|-- SMSNotification
    NotificationService <|-- PushNotification

    class EmailNotification {
        +send()
    }

    class SMSNotification {
        +send()
    }

    class PushNotification {
        +send()
    }

    class NotificationFactory {
        +createNotificationService(type) NotificationService
    }

    NotificationFactory --> NotificationService : creates
