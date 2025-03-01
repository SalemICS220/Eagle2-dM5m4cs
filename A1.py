from datetime import datetime
from enum import Enum


# Define an Enum for Nationality
class Nationality(Enum):
    USA = "USA"
    UAE = "UAE"
    UK = "UK"
    INDIA = "India"
    CANADA = "Canada"


# Customer Class
class Customer:
    def __init__(self, first_name, last_name, nationality, date_of_birth, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address


    def setFirstName(self, first_name):
        self.first_name = first_name


    def getFirstName(self):
        return self.first_name


    def setLastName(self, last_name):
        self.last_name = last_name


    def getLastName(self):
        return self.last_name


    def setNationality(self, nationality):
        self.nationality = nationality


    def getNationality(self):
        return self.nationality


    def setDateOfBirth(self, date_of_birth):
        self.date_of_birth = date_of_birth


    def getDateOfBirth(self):
        return self.date_of_birth


    def setEmail(self, email):
        self.email = email


    def getEmail(self):
        return self.email


    def displayCustomerInfo(self):
        """Displays customer details."""
        return f"Customer: {self.first_name} {self.last_name}, Nationality: {self.nationality.name}, DOB: {self.date_of_birth}, Email: {self.email}, Address: {self.address}"


    def customerPurchaseHistory(self):
        """Retrieves the customer's purchase history (placeholder)."""
        pass  # This function should return the purchase history


# Manager Class
class Manager:
    def __init__(self, first_name, last_name, nationality, date_of_birth, responsibility, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.responsibility = responsibility
        self.salary = salary


    def setFirstName(self, first_name):
        self.first_name = first_name


    def getFirstName(self):
        return self.first_name


    def setLastName(self, last_name):
        self.last_name = last_name


    def getLastName(self):
        return self.last_name


    def setNationality(self, nationality):
        self.nationality = nationality


    def getNationality(self):
        return self.nationality


    def setDateOfBirth(self, date_of_birth):
        self.date_of_birth = date_of_birth


    def getDateOfBirth(self):
        return self.date_of_birth


    def setResponsibility(self, responsibility):
        self.responsibility = responsibility


    def getResponsibility(self):
        return self.responsibility


    def setSalary(self, salary):
        self.salary = salary


    def getSalary(self):
        return self.salary


    def displayManagerInfo(self):
        """Displays manager details."""
        return f"Manager: {self.first_name} {self.last_name}, Nationality: {self.nationality.name}, Responsibility: {self.responsibility}, Salary: ${self.salary}"


    def managerProgress(self):
        """Tracks the manager's performance and progress (placeholder)."""
        pass  # This function should return progress details


# Delivery Staff Class
class DeliveryStaff:
    def __init__(self, first_name, last_name, nationality, date_of_birth, orders_number, shifts):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.date_of_birth = date_of_birth
        self.orders_number = orders_number
        self.shifts = shifts


    def setFirstName(self, first_name):
        self.first_name = first_name


    def getFirstName(self):
        return self.first_name


    def setLastName(self, last_name):
        self.last_name = last_name


    def getLastName(self):
        return self.last_name


    def setNationality(self, nationality):
        self.nationality = nationality


    def getNationality(self):
        return self.nationality


    def setDateOfBirth(self, date_of_birth):
        self.date_of_birth = date_of_birth


    def getDateOfBirth(self):
        return self.date_of_birth


    def setOrdersNumber(self, orders_number):
        self.orders_number = orders_number


    def getOrdersNumber(self):
        return self.orders_number


    def setShifts(self, shifts):
        self.shifts = shifts


    def getShifts(self):
        return self.shifts


    def displayDeliveryStaff(self):
        """Displays delivery staff details."""
        return f"Delivery Staff: {self.first_name} {self.last_name}, Nationality: {self.nationality.name}, Orders Handled: {self.orders_number}, Shifts: {self.shifts}"


    def deliveryProgress(self):
        """Tracks the delivery progress of the staff (placeholder)."""
        pass  # This function should return progress details


# Deliver Order Class
class DeliverOrder:
    def __init__(self, orderID, status, total_amount, delivery_time, delivery_address):
        self.orderID = orderID
        self.status = status
        self.total_amount = total_amount
        self.delivery_time = delivery_time
        self.delivery_address = delivery_address  # New attribute


    def setOrderID(self, orderID):
        self.orderID = orderID


    def getOrderID(self):
        return self.orderID


    def setStatus(self, status):
        self.status = status


    def getStatus(self):
        return self.status


    def setTotalAmount(self, total_amount):
        self.total_amount = total_amount


    def getTotalAmount(self):
        return self.total_amount


    def setDeliveryTime(self, delivery_time):
        self.delivery_time = delivery_time


    def getDeliveryTime(self):
        return self.delivery_time


    def setDeliveryAddress(self, delivery_address):
        self.delivery_address = delivery_address


    def getDeliveryAddress(self):
        return self.delivery_address


    def displayOrderInfo(self):
        """Displays order details."""
        return f"Order ID: {self.orderID}, Status: {self.status}, Total: ${self.total_amount:.2f}, Delivery Time: {self.delivery_time}, Address: {self.delivery_address}"


    def calculateTotal(self):
        """Calculates the total amount for the order (placeholder)."""
        pass  # This function should return total amount based on order details


# Creating Objects
customer1 = Customer("John", "Doe", Nationality.USA, "1990-01-01", "john.doe@example.com", "123 Elm St")
customer2 = Customer("Alice", "Smith", Nationality.UK, "1995-06-15", "alice.smith@example.com", "456 Oak St")


manager1 = Manager("Robert", "Brown", Nationality.CANADA, "1985-09-22", "Operations", 75000)
manager2 = Manager("Emma", "Johnson", Nationality.UAE, "1988-04-11", "Logistics", 68000)


staff1 = DeliveryStaff("David", "Williams", Nationality.INDIA, "1992-07-30", 120, "Night Shift")
staff2 = DeliveryStaff("Sophia", "Davis", Nationality.USA, "1994-11-12", 95, "Morning Shift")


order1 = DeliverOrder(1001, "Delivered", 49.99, datetime(2024, 3, 1, 14, 30), "123 Main St, NY")
order2 = DeliverOrder(1002, "In Transit", 29.99, datetime(2024, 3, 1, 18, 15), "456 Elm St, CA")


# Displaying Delivery Note
print("===== Delivery Note =====")
print(order1.displayOrderInfo())
print(order2.displayOrderInfo())