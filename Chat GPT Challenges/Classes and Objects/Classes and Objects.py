# 12
# Classes and Objects Challenge:
# Extend the car class to include a method that calculates the fuel efficiency of the car.
from Car import Car

# Initialize the car object
car1 = Car("Toyota", "Corolla", 2019, "silver", 43000, 300, 10)

car2 = Car("Honda", "Civic", 2018, "black", 35000, 250, 10)

# Call the fuelEfficiency method
car1.fuelEfficiency(car1.miles, car1.gallons)
car2.fuelEfficiency(car2.miles, car2.gallons)
