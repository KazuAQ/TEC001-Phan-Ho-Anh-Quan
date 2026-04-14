import random
from tabulate import tabulate

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.distance = 0
        self.speed = 0
    
    def drive(self, hours=1):
        self.distance += self.speed * hours
    
    def random_speed_change(self):
        self.speed = random.uniform(0, self.max_speed)


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hours = 0
    
    def hour_passes(self):
        for car in self.cars:
            car.random_speed_change()
            car.drive()
        self.hours += 1
    
    def print_status(self):
        print(f"\n{self.name} - After {self.hours} hours:")
        table_data = []
        for car in self.cars:
            table_data.append([car.name, f"{car.speed:.2f} km/h", f"{car.distance:.2f} km"])
        print(tabulate(table_data, headers=["Car", "Speed", "Distance"], tablefmt="grid"))
    
    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)


def main():
    car_names = ["Thunder", "Blaze", "Storm", "Phoenix", "Viper", "Falcon", "Dragon", "Inferno", "Cipher", "Phantom"]
    cars = [Car(name, max_speed=180) for name in car_names]
    
    race = Race("Grand Demolition Derby", 8000, cars)
    
    while not race.race_finished():
        race.hour_passes()
        if race.hours % 10 == 0:
            race.print_status()
    
    race.print_status()
    winner = max(race.cars, key=lambda car: car.distance)
    print(f"\n Race finished! Winner: {winner.name} with {winner.distance:.2f} km")

if __name__ == "__main__":
    main()