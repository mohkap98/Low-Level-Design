# 🧠 Tic Tac Toe - Low Level Design (LLD)

A modular, extensible, and object-oriented design for the classic **Tic Tac Toe** game using design patterns like **State**, **Factory**, and **Observer**.

---

## ✅ Problem Requirements

Design a Tic Tac Toe game that:
- Supports **two players** (human or AI in the future)
- Alternates turns correctly
- Validates moves
- Detects **win** or **draw** state
- Can be easily extended for:
  - Custom board size (NxN)
  - AI players
  - Game analytics or viewers via Observer

---

## 🧩 Design Approach

We follow **SOLID principles** and **Design Patterns** to ensure:
- Low coupling and high cohesion
- Easy state transitions (`GameOn`, `GameWon`, `GameDrawn`)
- Extensibility (e.g., add `AIPlayer`, `Undo`, etc.)
- Code testability and separation of concerns

---

## 🧱 Core Components & Classes

| Component         | Description                                              |
|------------------|----------------------------------------------------------|
| `Tokens`          | Enum for possible board values (`X`, `O`, `EMPTY`)        |
| `Player`          | Represents a player with ID, name, and assigned token     |
| `PlayerFactory`   | Creates player instances using the **Factory Pattern**   |
| `Board`           | NxN board. Handles moves, validations, win/draw check   |
| `GameController`  | Controls game flow. Maintains state & player turn       |
| `GameState`       | Abstract class for game state logic                     |
| `GameOn` / `GameWon` / `GameDrawn` | Concrete classes for different game phases |
| `Observer` *(optional)* | For integrating UI or logging during moves          |

---

## 🧠 Design Patterns Used

| Pattern      | Usage                                                       |
|--------------|-------------------------------------------------------------|
| **State**     | Switch between `GameOn`, `GameWon`, `GameDrawn` dynamically |
| **Factory**   | Create players with selected token and ID                   |
| **Observer** *(planned)* | Notify external components on move/win/draw        |

---

## 🧮 Class Diagram (UML)

> Render this UML in [PlantUML](https://plantuml.com/) or any UML tool.

