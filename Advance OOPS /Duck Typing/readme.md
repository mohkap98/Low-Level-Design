# 🦆 Duck Typing in Python

## 📘 What is Duck Typing?

**Duck typing** is a concept in dynamic languages like Python where the type or class of an object is **less important** than the methods and properties it defines.

> “If it looks like a duck, swims like a duck, and quacks like a duck — then it probably is a duck.”

In Python, this means:
> You don’t check an object’s type explicitly.  
> You just use it, assuming it has the right behavior.

---

## 🤔 Why Is It Useful?

- ✅ Encourages **loose coupling**  
- ✅ Supports **polymorphism** without inheritance  
- ✅ Makes code **more flexible** and **easier to test**  
- ✅ Avoids unnecessary boilerplate like formal interfaces

---

## 🧠 Real-World Analogy

> If someone can **drive a car**, do you care what **driving school** they went to?

Probably not. You just care that they can **steer**, **accelerate**, and **brake**.

Likewise in Python, we care about **what an object can do**, not what it claims to be.

---

## 👨‍💻 Code Example: Duck Typing in Action

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(entity):
    entity.quack()  # We don’t care what class 'entity' is

make_it_quack(Duck())     # ✅ Output: Quack!
make_it_quack(Person())   # ✅ Output: I'm pretending to be a duck!
