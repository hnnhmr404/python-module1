#!/usr/bin/env python3

def ft_garden_intro(name: str, height: int, age: int) -> None:
    """
    Display the plant information in garden
    """
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")


def main() -> None:
    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    ft_garden_intro(name, height, age)
    print()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
