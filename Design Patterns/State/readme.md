# 🚦 State Design Pattern – Traffic Light Simulation (Python)

This project demonstrates the **State Design Pattern** by simulating a traffic light system that transitions between `Red`, `Green`, and `Yellow` lights, each with its own behavior.

---

## 🧠 What is the State Pattern?

The **State Design Pattern** allows an object to change its behavior when its internal state changes. It's as if the object changes its class at runtime.

> It helps you eliminate complex conditionals (`if-else` or `switch-case`) and encapsulates state-specific behavior in dedicated classes.

---

## ❓ Problem Statement

Imagine a `TrafficLight` object that behaves differently depending on whether it is `Red`, `Green`, or `Yellow`. Without the State pattern, this logic might become a tangled mess of `if/else`.

---

## ✅ Solution: State Pattern

We define:

- `TrafficLightState` – An interface for states
- Concrete state classes – `Red`, `Green`, `Yellow`, each handling their own transitions and display logic
- `TrafficLight` – The context class that delegates behavior to its current state

---

## 📄 Python Implementation

```python
# --- traffic_light.py ---
class TrafficLight:
    def __init__(self):
        self.state = Red()
    
    def next(self):
        self.state.next_state(self)
    
    def show(self):
        self.state.cur_state()

class TrafficLightState:
    def next_state(self, context):
        pass
    def cur_state(self):
        pass

class Green(TrafficLightState):
    def next_state(self, context):
        context.state = Yellow()
    def cur_state(self):
        print("Green : GO")

class Red(TrafficLightState):
    def next_state(self, context):
        context.state = Green()
    def cur_state(self):
        print("Red : STOP")

class Yellow(TrafficLightState):
    def next_state(self, context):
        context.state = Red()
    def cur_state(self):
        print("Yellow : SLOW DOWN")

# Example Usage
light = TrafficLight()
light.show()   # Red : STOP
light.next()
light.show()   # Green : GO
