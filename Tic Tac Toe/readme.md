# 🧠 Tic Tac Toe - Low Level Design (LLD)

A clean object-oriented design of the classic Tic Tac Toe game using Python. This version supports human vs human, and human vs AI play, and demonstrates how to design modular, extensible game systems using key software design patterns.

---

## ✅ Requirements

- 3x3 board for two players
- Turn-based gameplay
- Detect win, draw, invalid moves
- Clean game state management
- Support for:
  - Human vs Human
  - Human vs AI (extensible to multiple AI strategies)
- Ability to swap players
- Display current board state

---

## 🔧 Design Patterns Used

- **State Pattern** – Manage game flow (`GameOn`, `GameWon`, `GameDrawn`)
- **Factory Pattern** – Create players (Human or AI)
- **Strategy Pattern** – Support different AI behaviors
- **Enum** – Represent player tokens (X, O)
- **Separation of Concerns** – Split logic across Board, Player, GameState, GameController

---

## 🧩 Key Classes

- `Token` – Enum for X, O, EMPTY
- `Player`, `AIPlayer` – Abstract base for players
- `PlayerFactory` – Dynamically creates players
- `Board` – Represents the 3x3 grid
- `GameState` – Abstract base class for game states
  - `GameOn`, `GameWon`, `GameDrawn`
- `GameController` – Orchestrates the game logic
- `AIStrategy` – Interface for AI logic (e.g., random, minimax)

---

## 📐 UML Class Diagram (Mermaid.js)

```mermaid
classDiagram

  class GameController {
    -board: Board
    -p1: Player
    -p2: Player
    -curPlayer: Player
    -state: GameState
    -winner: Player
    +make_move(row, col)
    +switch_turn()
    +set_state(state)
  }

  class Board {
    -rows: int
    -cols: int
    -board: list
    +is_valid_move(row, col)
    +make_move(row, col, token)
    +print_board()
    +check_win(token)
    +check_draw()
  }

  class Player {
    -name: str
    -id: str
    -token: Token
    +get_name()
    +get_id()
    +get_token()
  }

  class HumanPlayer {
  }

  class AIPlayer {
    -strategy: AIStrategy
    +make_move(board)
  }

  class Token {
    <<enum>>
    X
    O
    EMPTY
  }

  class PlayerFactory {
    +createPlayer(name, id, token, type, strategy=None)
  }

  class GameState {
    <<interface>>
    +make_move(context, row, col)
  }

  class GameOn {
    +make_move(context, row, col)
  }

  class GameWon {
    +make_move(context, row, col)
  }

  class GameDrawn {
    +make_move(context, row, col)
  }

  class AIStrategy {
    <<interface>>
    +choose_move(board)
  }

  class RandomStrategy {
    +choose_move(board)
  }

  GameController --> Board
  GameController --> Player
  GameController --> GameState

  GameState <|-- GameOn
  GameState <|-- GameWon
  GameState <|-- GameDrawn

  Player <|-- HumanPlayer
  Player <|-- AIPlayer

  AIPlayer --> AIStrategy
  AIStrategy <|-- RandomStrategy

  PlayerFactory --> Player
  AIPlayer --> Token
  HumanPlayer --> Token
  Board --> Token
