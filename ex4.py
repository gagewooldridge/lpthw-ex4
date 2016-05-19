# This program will tahe the calculations for a carpooling
# Company and output the daily requirements

# Total cars availible
cars = 100

# How many seats each car has
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# How many more cars than drivers
cars_not_driven = cars - drivers

# Number of cars driven is equal to the number of drivers
cars_driven = drivers

# Total number of potential passengers
carpool_capacity = cars_driven * space_in_a_car

# Average number of people that will need to be in each car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars availible.")
print ("There are only", drivers, "drivers availible.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
