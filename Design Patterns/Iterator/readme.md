# 🔁 Iterator Design Pattern – Social Network Friends (Python)

---

## 📘 Overview

The **Iterator Pattern** is a behavioral design pattern that provides a way to access the elements of a collection **sequentially** without exposing its internal representation.

This example demonstrates the pattern through a `SocialNetwork` class, where each profile has a list of friends. The `FriendIterator` is used to iterate through these friends without giving access to the actual `friends` list.

---

## 🎯 Problem It Solves

- Hides the internal structure of a collection (encapsulation)
- Allows multiple ways to iterate over the same collection
- Enables multiple simultaneous iterators without interference
- Supports custom iteration logic

---

## 🧱 UML Diagram

```mermaid
classDiagram
    class ProfileIterator {
        <<interface>>
        +has_next()
        +get_next()
    }

    ProfileIterator <|-- FriendIterator

    class SocialNetwork {
        -name: str
        -friends: list
        +add_friend()
        +remove_friend()
        +display_friends()
    }

    SocialNetwork --> FriendIterator : uses
