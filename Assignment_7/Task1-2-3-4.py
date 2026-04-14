import random

#define class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max = max_speed
        self.speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f"Registration:\n{self.registration_number},\nMax Speed: {self.max} km/h,\nCurrent Speed: {self.speed} km/h,\nTravelled Distance: {self.travelled_distance} km"
    
    def accel(self, speed_change):
        self.speed += speed_change
        if self.speed > self.max:
            self.speed = self.max
        elif self.speed < 0:
            self.speed = 0
    def drive(self, hour):
        self.travelled_distance += self.speed * hour
    


#small progam
car = Car("ABC-123", 142)
print(car)

car.accel(30)
car.accel(70)
car.accel(50)
print(f"Current Speed: {car.speed} km/h")
car.accel(-200)
print(f"Final Speed: {car.speed} km/h")

#race

#car list
cars=list()
for i in range(1, 11):
    reg = f'ABC-{i}'
    max = random.randint(150, 200)
    cars.append(Car(reg, max))

#simulate
race_hour = 0
while True:
    race_hour += 1
    
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accel(speed_change)
        car.drive(1)
    
    if any(car.travelled_distance >= 10000 for car in cars):
        break

print(f"\nRace finished after {race_hour} hours!\n")
print(f"{'Registration':<12} | {'Max Speed':<10} | {'Current Speed':<14} | {'Distance':<12}")
print("-" * 60)
for car in cars:
    print(f"{car.registration_number:<12} | {car.max:<10} km/h | {car.speed:<14} km/h | {car.travelled_distance:<12.1f} km")