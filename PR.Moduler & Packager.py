import datetime
import math
import os
import random
import time
import uuid


def main_menu():
    while True:
        print("\n=================================")
        print("Welcome to Multi-Utility Toolkit")
        print("=================================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("=================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_ops_menu()
        elif choice == "6":
            explore_dir_menu()
        elif choice == "7":
            print("Exiting Multi-Utility Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            now = datetime.datetime.now()
            print(f"\nCurrent Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

        elif choice == "2":
            try:
                date1_str = input(
                    "Enter the first date (YYYY-MM-DD): "
                ).strip()
                date2_str = input(
                    "Enter the second date (YYYY-MM-DD): "
                ).strip()
                d1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
                diff = abs((d2 - d1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")

        elif choice == "3":
            try:
                date_str = input("Enter date (YYYY-MM-DD): ").strip()
                fmt = input(
                    "Enter format (e.g. %d/%m/%Y or %B %d, %Y): "
                ).strip()
                d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                print(f"Formatted Date: {d.strftime(fmt)}")
            except ValueError:
                print("Invalid date or format string!")

        elif choice == "4":
            input("Press Enter to START the stopwatch...")
            start_time = time.time()
            input("Press Enter to STOP the stopwatch...")
            elapsed = time.time() - start_time
            print(f"Elapsed Time: {elapsed:.2f} seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                for i in range(seconds, 0, -1):
                    print(f"Time remaining: {i}s", end="\r")
                    time.sleep(1)
                print("\nTime's up!")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "6":
            break
        else:
            print("Invalid choice!")


def math_menu():
    print("\n--- Mathematical Operations ---")
    print("1. Factorial")
    print("2. Square Root")
    print("3. Power")
    print("4. Trigonometric Functions (sin, cos, tan)")
    choice = input("Enter option: ").strip()

    if choice == "1":
        n = int(input("Enter number: "))
        print(f"Factorial of {n}: {math.factorial(n)}")
    elif choice == "2":
        n = float(input("Enter number: "))
        print(f"Square root: {math.sqrt(n)}")
    elif choice == "3":
        b = float(input("Enter base: "))
        p = float(input("Enter exponent: "))
        print(f"Result: {math.pow(b, p)}")
    elif choice == "4":
        deg = float(input("Enter angle in degrees: "))
        rad = math.radians(deg)
        print(
            f"sin: {math.sin(rad):.4f}, cos: {math.cos(rad):.4f}, tan: {math.tan(rad):.4f}"
        )


def random_menu():
    print("\n--- Random Data Generation ---")
    print("1. Random Integer")
    print("2. Random Float (0 to 1)")
    print("3. Random Choice from List")
    choice = input("Enter option: ").strip()

    if choice == "1":
        a = int(input("Min value: "))
        b = int(input("Max value: "))
        print(f"Random int: {random.randint(a, b)}")
    elif choice == "2":
        print(f"Random float: {random.random()}")
    elif choice == "3":
        items = input("Enter items separated by comma: ").split(",")
        print(f"Random selection: {random.choice(items).strip()}")


def uuid_menu():
    print("\n--- Generate Unique Identifiers (UUID) ---")
    print(f"Generated UUID v4: {uuid.uuid4()}")


def file_ops_menu():
    print("\n--- File Operations ---")
    filename = input("Enter filename to read/write: ").strip()
    action = input("Type 'r' to read or 'w' to write: ").strip().lower()

    if action == "w":
        content = input("Enter text to write: ")
        with open(filename, "w") as f:
            f.write(content)
        print("File written successfully!")
    elif action == "r":
        if os.path.exists(filename):
            with open(filename, "r") as f:
                print("\n--- File Content ---")
                print(f.read())
        else:
            print("File does not exist.")


def explore_dir_menu():
    print("\n--- Explore Module Attributes (dir()) ---")
    mod_name = (
        input("Enter built-in module name (e.g. math, os, sys, datetime): ")
        .strip()
        .lower()
    )
    modules = {
        "math": math,
        "os": os,
        "datetime": datetime,
        "random": random,
        "uuid": uuid,
    }

    if mod_name in modules:
        print(f"\nAttributes of '{mod_name}':")
        print(dir(modules[mod_name]))
    else:
        print("Module not in demo list or invalid.")


if __name__ == "__main__":
    main_menu()