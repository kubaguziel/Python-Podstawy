class Car():
    """Prosta próba zaprezentowania samochodu."""
    def __init__(self,make,model,year):
        """Inicjalizacja atrybutów"""
        self.make = make
        self.model = model 
        self.year = year 
        self.odometer_reading = 0

    def get_name(self):
        """Zwrot elegancko sformatowanego opiu samochodu"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu"""
        print(f"Przebieg wynosi: {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """Przypisanie podanej wartości licznikowi przebiegu"""
        if mileage < self.odometer_reading:
            print("Nie można cofnąć licznika!")

        else: self.odometer_reading = mileage

    def increment_odometer(self, kilometers):
        """Inkrementowanie wartości licznika"""
        self.odometer_reading += kilometers

    def fill_gas_tank(self):
        print("Samochód zatankowany!")

class Battery():
    def __init__(self,battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora"""
        print(f"\nBateria ma pojemność {self.battery_size} kWh.")

    def get_range(self):
        """Wyświetla informacje o zasięgu, na podstawie pojemności akumulatora"""
        if self.battery_size == 100:
            range = 260
        elif self.battery_size == 120:
            range = 300

        print(f"Zasięg wynosi {range} km.")
    

class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne dla samochodów elektrycznych"""
    def __init__(self, make, model, year):
        """inicjalizacja atrybutów z klasy nadrzędnej"""
        super().__init__(make, model, year)
        """Atrybuty charakterystyczne dla klasy potomnej"""
        self.battery = Battery()

    def fill_gas_tank(self):
        print("Ten samochód nie wymaga tankowania paliwa!")

