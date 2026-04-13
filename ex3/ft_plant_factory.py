#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height_cm: float, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def show(self) -> None:
        print(
                f"{self.name}: {self.height_cm:.1f}cm, "
                f"{self.age_days} days old"
            )


def main() -> None:
    plant_data = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120)
    ]

    plants = [Plant(name, height, age) for name, height, age in plant_data]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
