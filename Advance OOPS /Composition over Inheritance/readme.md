
# 🧱 Composition Over Inheritance

## 🔍 What Is It?

**Composition over Inheritance** is a software design principle that favors **building classes using other classes (composition)** instead of **extending classes (inheritance)**.

> Instead of saying "My class *is a* type of X," we say "My class *has a* type of X."

---

## 🤔 Why Should You Care?

While **inheritance** seems simple, it can lead to:
- ❌ Tight coupling between classes
- ❌ Fragile and deep class hierarchies
- ❌ Hard-to-change behavior

**Composition**, on the other hand:
- ✅ Promotes flexibility
- ✅ Makes code easier to test, reuse, and scale
- ✅ Encourages loose coupling

---

## 🪄 Real-Life Analogy

> Think of a **LEGO car**.

- You **compose** it using **wheels, engines, and seats** — small pieces you can swap.
- If you want to make it a **flying car**, you just add a **propeller piece**.
  
🔁 You're not *inheriting* from a car — you're **composing** it from interchangeable parts.

---

## 👨‍💻 Code Example

### 🚫 Inheritance (Too Rigid)
```python
class Animal:
    def walk(self):
        print("Walking")

class Bird(Animal):
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    pass

ostrich = Ostrich()
ostrich.fly()  # ❌ Ostrich can't fly!

class WalkBehavior:
    def walk(self):
        print("Walking")

class FlyBehavior:
    def fly(self):
        print("Flying")

class Ostrich:
    def __init__(self):
        self.walk_behavior = WalkBehavior()

    def walk(self):
        self.walk_behavior.walk()

class Eagle:
    def __init__(self):
        self.walk_behavior = WalkBehavior()
        self.fly_behavior = FlyBehavior()

    def walk(self):
        self.walk_behavior.walk()

    def fly(self):
        self.fly_behavior.fly()

ostrich = Ostrich()
ostrich.walk()       # ✅

eagle = Eagle()
eagle.fly()          # ✅
eagle.walk()         # ✅
