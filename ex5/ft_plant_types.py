#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: float):
        self.height += amount

    def age_one(self, days: int):
        self.age += days

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float):
        super().grow(amount)

    def age_one(self, days: int):
        super().age_one(days)
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")

    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    veg = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Flower")
    flower.show()

    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree.show()

    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    veg.show()

    print("[make tomato grow and age for 20 days]")
    veg.grow(42.0)
    veg.age_one(20)
    veg.show()


if __name__ == "__main__":
    main()
