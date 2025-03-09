# Designing a Parking Lot System

## Requirements
1. The parking lot should have multiple levels, each level with a certain number of parking spots.
2. The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
3. The system should handle multiple entry and exit points and support concurrent access.
4. The customer must be able to rerseve a free parking spot and cancel its reservation.
5. Customers can pay via both cash and credit cards.
6. The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.
7. The system should support a per-hour parking fee model. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.


## Classes, Interfaces or EndPoints

1. The **ParkingLot** class follows the Singleton pattern to ensure only one instance of the parking lot exists. It maintains a list of levels and provides methods to park and unpark vehicles.
2. The **Level** class represents a level in the parking lot and contains a list of parking spots. It handles parking and unparking of vehicles within the level.
3. The **ParkingSpot** abstract class represents an individual parking spot. **cars**, **motorcycle** and **trucks** implement this class.
4. The **Entry** and **Exit** Terminals. **Exit** Panel will process payment.
5. The **Ticket** will encapsulate a parking ticket. Customers will take a ticket when they enter the parking lot.
6. The **ParkingRate** class will keep track of the hourly parking rates. It will specify a dollar amount for each hour. For example, for a two hour parking ticket, this class will define the cost for the first and the second hour.
7. The **Payment** class will be responsible for making payments. The system will support credit card and cash transactions. 
