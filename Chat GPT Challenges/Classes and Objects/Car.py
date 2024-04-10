class Car:

    def __init__(self, make, model, year, color, mileage, miles, gallons):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.miles = miles
        self.gallons = gallons

    def fuelEfficiency(self, miles, gallons):
        efficiency = miles / gallons
        print(f"{efficiency} miles per gallon.")

car1 = Car("Toyota", "Corolla", 2019, "silver", 43000, 300, 10)

print(f"The fuel efficiency of the {car1.year} {car1.make} {car1.model} is ", end="")
car1.fuelEfficiency(car1.miles, car1.gallons)




