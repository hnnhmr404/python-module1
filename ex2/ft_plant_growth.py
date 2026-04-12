#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, cm: float) -> None:
        self.height_cm += cm

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def get_info(self) -> str:
        return f"{self.name}: {round(self.height_cm, 1)}cm, {self.age_days} days old"


def simulate_week(plant: Plant, daily_growth: float) -> None:
    print("=== Garden Plant Growth ===")
    print(plant.get_info())

    for day in range(1, 8):
        plant.grow(daily_growth)
        plant.age(1)
        print(f"=== Day {day} ===")
        print(plant.get_info())

    total_growth = plant.height_cm - (plant.height_cm - daily_growth * 7)
    print(f"Growth this week: {round(total_growth, 1)}cm")


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    simulate_week(rose, 0.8)


if __name__ == "__main__":
    main()
