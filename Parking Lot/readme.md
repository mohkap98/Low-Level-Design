# 🅿️ Parking Lot System – Low-Level Design (LLD)

This project is a clean and extensible **Low-Level Design (LLD)** of a multi-floor parking lot system, built in Python using core OOP principles and key software design patterns.

---
## ✅ Requirements

The system supports:

- Multiple **types of parking slots** (Car, Bike, Truck)
- Multiple **floors**, each having their own set of slots
- **Dynamic allocation** of slots based on vehicle type
- **Payment processing** via multiple methods (UPI, Credit Card, Bank)
- **Fare strategy** based on vehicle type and time parked
- Ticketless flow with clear entry and exit behavior

---

## 🏗️ System Structure

### 🚙 Vehicle Management
- Supports `Car`, `Bike`, `Truck`
- Created via a **Factory Pattern**
- Fare calculated using **Strategy Pattern**

### 🅿️ Parking Structure
- `ParkingLot`: Manages multiple floors
- `ParkingFloor`: Manages multiple slots
- `ParkingSlot`: Holds vehicle + availability info

### 💳 Payment System
- `PaymentStrategy`: Abstract strategy interface
- Concrete strategies: `UPI`, `CreditCard`, `BankACC`

### 💰 Fare Calculation
- `FareStrategy`: Abstract strategy interface
- `BasicFare` (for Car/Bike)
- `PremiumFare` (for Truck)

---

## 📦 Class Design

### 1. `Vehicle` (Abstract Base Class)
- Subclasses: `Car`, `Bike`, `Truck`
- Contains license plate and fare strategy

### 2. `VehicleFactory`
- Creates appropriate vehicle instances using a map

### 3. `ParkingSlot`
- Holds one vehicle at a time
- Knows if it's available or occupied

### 4. `ParkingFloor`
- Contains multiple slots of different types
- Can add slots and find available ones

### 5. `ParkingLot`
- Manages multiple floors
- Coordinates slot assignment and exit payment

### 6. `FareStrategy` Interface
- `BasicFare`: For Car and Bike (1, 6, 12 hour brackets)
- `PremiumFare`: For Truck (1, 6, 12 hour brackets)

### 7. `PaymentStrategy` Interface
- `UPI`, `CreditCard`, `BankACC`

---

## 🔁 Design Patterns Used

| Pattern            | Purpose                                                       |
|--------------------|---------------------------------------------------------------|
| Factory Pattern     | To create `Vehicle` instances based on type                  |
| Strategy Pattern    | To handle both fare and payment method logic dynamically     |
| Composition         | `ParkingLot` → `ParkingFloor` → `ParkingSlot`                |
| Single Responsibility | Each class has one clear, maintainable job                 |

---

## 📦 Core Functional Flows

### 1️⃣ Vehicle Entry Flow

**Objective:** Allocate an available parking slot to a vehicle and issue a ticket.

**Steps:**
1. Vehicle object is created (`Car`, `Bike`, etc.)
2. `ParkingLot.assign_spot(vehicle)` is called.
3. System checks each floor and slot:
   - Finds the first available slot matching vehicle type.
4. Allocates the spot and generates a `Ticket`.
5. Returns ticket to user.

---

### 2️⃣ Vehicle Exit Flow

**Objective:** Free the slot and calculate fee based on parked time.

**Steps:**
1. User provides the `Ticket` at exit.
2. `ParkingLot.release_spot(ticketId)` is triggered.
3. System:
   - Retrieves the ticket
   - Calculates duration using `FeeStrategy`
   - Frees the slot
   - Processes payment using `PaymentStrategy`
   - Returns receipt to user

---

### 3️⃣ Find Available Slot Flow

**Objective:** Return available slots by vehicle type.

**Steps:**
1. User queries: `ParkingLot.get_available_slots(vehicle_type)`
2. System loops through all floors and slots.
3. Filters available slots matching the type.
4. Returns list of available `ParkingSpot`s


## 🗂️ UML Class Diagram

```mermaid
classDiagram
  class Vehicle {
    - vehicleType: str
    - licensePlate: str
    - fare_strategy: FareStrategy
    + getVehicleType()
    + getLicensePlate()
    + calculate_price(hours)
  }

  class FareStrategy {
    <<interface>>
    + calculateFare(hours, vehicle_type)
  }

  class PaymentStrategy {
    <<interface>>
    + pay(amount)
  }

  class ParkingSlot {
    - slot_id: int
    - slot_type: str
    - is_avail: bool
    - vehicle: Vehicle
    + park_vehicle(vehicle)
    + unpark_vehicle()
    + check_avail()
  }

  class ParkingFloor {
    - floor_num: int
    - parking_slots: dict
    + add_slot(slot_id, type)
    + find_avail_slot(vehicle_type)
  }

  class ParkingLot {
    - floors: dict
    + add_floor(floor_num)
    + add_slot_to_floor(floor, slot_id, type)
    + assign_slot(vehicle_type, license)
    + exit_parking(vehicle, slot, hours, payment_method)
  }

  class Car
  class Bike
  class Truck

  class BasicFare
  class PremiumFare

  class UPI
  class BankACC
  class CreditCard

  class VehicleFactory {
    + createVehicle(vehicle_type, license_plate)
  }

  Vehicle <|-- Car
  Vehicle <|-- Bike
  Vehicle <|-- Truck

  FareStrategy <|.. BasicFare
  FareStrategy <|.. PremiumFare

  PaymentStrategy <|.. UPI
  PaymentStrategy <|.. BankACC
  PaymentStrategy <|.. CreditCard

  ParkingLot "1" o-- "many" ParkingFloor
  ParkingFloor "1" o-- "many" ParkingSlot
  ParkingSlot "1" o-- "0..1" Vehicle

  VehicleFactory --> Vehicle
  Vehicle --> FareStrategy
  ParkingLot --> VehicleFactory
  ParkingLot --> PaymentStrategy
