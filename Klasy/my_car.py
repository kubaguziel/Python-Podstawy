from car import * #zamiast * możemy wpisać wszystkie klasy tj. Car, ElectricCar, Battery

my_new_car = Car('Audi','A4','2010')
# print(my_new_car.get_name())
# # my_new_car.odometer_reading += 20000
# my_new_car.update_odometer(500)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(300)
# my_new_car.read_odometer()

my_Tesla = ElectricCar('Tesla', 'Roadster', 2020)
print(my_Tesla.get_name())
my_Tesla.battery.describe_battery()
my_Tesla.battery.get_range()

# my_new_car.fill_gas_tank()
# my_Tesla.fill_gas_tank()