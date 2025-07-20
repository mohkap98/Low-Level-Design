# 🍽️ Composite Pattern – Restaurant Menu System in Python

This project demonstrates the **Composite Design Pattern** by building a **menu system** where `Menu` objects can contain both individual `MenuItem`s and nested `Menu`s.

---

## 🧠 What is the Composite Pattern?

> The Composite pattern lets you treat **individual objects** and **groups of objects** uniformly. It’s ideal for representing tree structures like menus, folders, or GUIs.

---

## 📐 UML Diagram (Mermaid.js)

```mermaid
classDiagram
    class MenuComponent {
        <<abstract>>
        +name
        +show(indent)
    }

    class MenuItem {
        -price
        +show(indent)
    }

    class Menu {
        -items : dict
        +add_menu_item(item)
        +remove_menu_item(item)
        +show(indent)
    }

    MenuComponent <|-- Menu
    MenuComponent <|-- MenuItem
    Menu --> MenuComponent : contains
