#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height_cm: float = 0, age_days: int = 0):
        self.name = name
        self._height_cm = 0
        self._age_days = 0

        if height_cm >= 0:
            self._height_cm = height_cm
        else:
            print(f"{self.name}: Error, height can't be negative")

        if age_days >= 0:
            self._age_days = age_days
        else:
            print(f"{self.name}: Error, age can't be negative")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height_cm = height
            print(f"Height updated: {round(self._height_cm, 1)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = age
            print(f"Age updated: {self._age_days} days")

    def get_height(self) -> float:
        return self._height_cm

    def get_age(self) -> int:
        return self._age_days

    def show(self) -> None:
        print(f"{self.name}: {round(self._height_cm, 1)}cm, {self._age_days} days old")


def main() -> None:
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    print()

    rose.set_height(25)
    rose.set_age(30)

    print()

    rose.set_height(-5)
    rose.set_age(-10)
    
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
