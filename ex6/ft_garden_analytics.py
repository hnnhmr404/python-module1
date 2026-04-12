#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, {self.show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant.Stats()

    def grow(self, amount: float):
        self.height += amount
        self._stats.grow_calls += 1

    def age_one(self, days: int):
        self.age += days
        self._stats.age_calls += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self._stats.show_calls += 1

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def display_stats(self):
        self._stats.display()


# -------- FLOWER --------
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


# -------- TREE --------
class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter}cm wide."
        )
        self.shade_calls += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


# -------- SEED --------
class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


# -------- GLOBAL FUNCTION --------
def show_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()
    if isinstance(plant, Tree):
        print(f"{plant.shade_calls} shade")


# -------- MAIN --------
def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    show_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age_one(20)
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)
    print()

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    show_stats(unknown)


if __name__ == "__main__":
    main()
