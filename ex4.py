#declare cars as an integer equal to 100
cars = 100
#declare sapce_in_a_car as a floating point number equal to 4.0
space_in_a_car = 4.0
#declare drivers as an integer equal to 30
drivers = 30
#declare passengers as an integer equal to 90
passengers = 90
#declare cars_not_driven as the difference of cars minus drivers
cars_not_driven = cars - drivers
#declare cars_driven as the value of drivers
cars_driven = drivers
#declare carpool_capasity as the product of cars_driven multipled by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#declare average_passengers_per_car as the dividend of passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
