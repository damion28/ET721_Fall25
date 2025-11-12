"""
damion ally
sep 17, 2025
lab 6: objects and classes
"""

print("\n---- Example 1: create a class ----")


class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # method
    def add_radius(self, r):
        self.radius += r
        return self.radius


class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    # method to calculate the area
    def area(self):
        return self.width * self.height

    # method to calculate the perimeter
    def perimeter(self):
        return 2 * self.width + 2 * self.height


# creating an instance of the class, which is an object
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2, 5, "magenta")
rectangle2 = Rectangle(7, 3, "blue")

# accessing information in an object
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

# updating data in an object
# change circle1 color from 'red' to 'yellow'
print(f"The color of circle2 before the update = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle2 after the update = {circle1.color}")

# accessing a method
print(f"Radius of circle2 = {circle2.radius}")
# update the radius by adding 5
circle2.add_radius(5)
print(f"Radius of circle2 after method add_raidus = {circle2.radius}")

# accessing methods in Rectangle
print(
    f"The area of the rectangle1 with width {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}"
)
print(f"The perimeter of rectangle2 = {rectangle2.perimeter()}")


print("\n---- Exercise ----")


class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 1000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New balance: {self.balance}")
        else:
            print("Insufficient funds for this withdrawl.")


useraccount = BankAccount(123456789, "Damion Ally")

useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)

print(f"Final balance {useraccount.balance}")
