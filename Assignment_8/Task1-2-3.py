class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moving up. Current floor: {self.current_floor}")
        else:
            print(f"Already at top floor: {self.current_floor}")
    
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moving down. Current floor: {self.current_floor}")
        else:
            print(f"Already at bottom floor: {self.current_floor}")
    
    def go_to_floor(self, destination_floor):
        if destination_floor < self.bottom_floor or destination_floor > self.top_floor:
            print(f"Invalid floor: {destination_floor}")
            return
        
        while self.current_floor != destination_floor:
            if self.current_floor < destination_floor:
                self.floor_up()
            else:
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
    
    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f"\nElevator {elevator_num} going to floor {destination_floor}:")
            self.elevators[elevator_num].go_to_floor(destination_floor)
        else:
            print(f"Invalid elevator number: {elevator_num}")
    
    def fire_alarm(self):
        print("\n*** FIRE ALARM! All elevators moving to bottom floor ***")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}:")
            elevator.go_to_floor(self.bottom_floor)


if __name__ == "__main__":
    print("=== Testing Single Elevator ===")
    elevator = Elevator(1, 10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(1)

    print("\n=== Testing Building ===")
    building = Building(1, 10, 3)
    
    building.run_elevator(0, 7)
    building.run_elevator(1, 4)
    building.run_elevator(2, 9)
    
    building.fire_alarm()