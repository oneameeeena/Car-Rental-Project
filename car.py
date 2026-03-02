from datetime import datetime

# -------------------------
# 1. Car Categories
# -------------------------
car_categories = ["Mercedes", "Volkswagen", "BMW", "Renault"]

# -------------------------
# 2. Cars
# -------------------------
cars = []

# Function to add a car
def add_car(car_id, seats, price, category):
    if category not in car_categories:
        print(f"Error: Invalid category. Choose from {car_categories}")
        return
    car = {
        "id": car_id,
        "seats": seats,
        "price": price,
        "category": category
    }
    cars.append(car)
    print(f"Car ID {car_id} added successfully!")

# Function to remove a car
def remove_car(car_id):
    global cars
    cars[:] = [c for c in cars if c["id"] != car_id]
    print(f"Car ID {car_id} removed successfully!")

# Function to display a car
def show_car(car_id):
    for c in cars:
        if c["id"] == car_id:
            print(c)
            return
    print("Car not found!")

# Function to show all cars
def display_cars():
    if not cars:
        print("No cars available.")
    for c in cars:
        print(c)

# Function to search cars by price
def search_car_by_price(price):
    results = [c for c in cars if c["price"] == price]
    if not results:
        print("No cars found with that price.")
    return results

# Function to search cars by category
def search_car_by_category(category):
    results = [c for c in cars if c["category"] == category]
    if not results:
        print(f"No cars found in category '{category}'.")
    return results

# Helper to find a car by ID
def search_car_by_id(car_id):
    for c in cars:
        if c["id"] == car_id:
            return c
    return None

# -------------------------
# 3. Rentals
# -------------------------
rentals = []

# Function to rent a car for a client
def rent_car(rental_id, car_id, start_date_str, return_date_str, client_name):
    car = search_car_by_id(car_id)
    if not car:
        print("Cannot rent: Car does not exist.")
        return
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
    rental = {
        "id": rental_id,
        "car": car,
        "start_date": start_date,
        "return_date": return_date,
        "client_name": client_name
    }
    rentals.append(rental)
    print(f"Car ID {car_id} rented to {client_name} successfully!")

# Function to cancel a rental
def cancel_rental(rental_id):
    global rentals
    rentals[:] = [r for r in rentals if r["id"] != rental_id]
    print(f"Rental ID {rental_id} canceled.")

# Function to display a rental's information
def show_rental(rental_id):
    for r in rentals:
        if r["id"] == rental_id:
            print({
                "id": r["id"],
                "client_name": r["client_name"],
                "car_id": r["car"]["id"],
                "category": r["car"]["category"],
                "start_date": r["start_date"].strftime("%Y-%m-%d"),
                "return_date": r["return_date"].strftime("%Y-%m-%d"),
                "price": r["car"]["price"]
            })
            return
    print("Rental not found!")

# Function to calculate the total amount for a rental
def total_amount_rental(rental_id):
    for r in rentals:
        if r["id"] == rental_id:
            days = (r["return_date"] - r["start_date"]).days + 1
            total = r["car"]["price"] * days
            print(f"Total amount for rental ID {rental_id}: {total}")
            return total
    print("Rental not found!")
    return 0

# Function to display all rentals in progress
def display_rentals_in_progress():
    today = datetime.today()
    for r in rentals:
        if r["start_date"] <= today <= r["return_date"]:
            show_rental(r["id"])

# Function to calculate total amount of all rentals for a given month/year
def total_amount_month(month, year):
    total = 0
    for r in rentals:
        if r["start_date"].month == month and r["start_date"].year == year:
            days = (r["return_date"] - r["start_date"]).days + 1
            total += r["car"]["price"] * days
    print(f"Total amount of all rentals in {month}/{year}: {total}")
    return total

# -------------------------
# 4. Menu
# -------------------------
def menu():
    while True:
        print("\n--- Car Rental Management ---")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. Show Car")
        print("4. Display All Cars")
        print("5. Search Car by Price")
        print("6. Search Car by Category")
        print("7. Rent a Car")
        print("8. Cancel Rental")
        print("9. Show Rental")
        print("10. Total Amount for Rental")
        print("11. Display Rentals in Progress")
        print("12. Total Amount of Rentals in Month")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cid = input("Car ID: ")
            seats = int(input("Number of seats: "))
            price = float(input("Price per day: "))
            category = input(f"Category {car_categories}: ")
            add_car(cid, seats, price, category)
        elif choice == "2":
            cid = input("Car ID to remove: ")
            remove_car(cid)
        elif choice == "3":
            cid = input("Car ID to show: ")
            show_car(cid)
        elif choice == "4":
            display_cars()
        elif choice == "5":
            price = float(input("Price to search: "))
            results = search_car_by_price(price)
            for c in results:
                print(c)
        elif choice == "6":
            category = input(f"Category {car_categories}: ")
            results = search_car_by_category(category)
            for c in results:
                print(c)
        elif choice == "7":
            rid = input("Rental ID: ")
            cid = input("Car ID: ")
            start_date = input("Start Date (YYYY-MM-DD): ")
            return_date = input("Return Date (YYYY-MM-DD): ")
            client = input("Client Name: ")
            rent_car(rid, cid, start_date, return_date, client)
        elif choice == "8":
            rid = input("Rental ID to cancel: ")
            cancel_rental(rid)
        elif choice == "9":
            rid = input("Rental ID to show: ")
            show_rental(rid)
        elif choice == "10":
            rid = input("Rental ID to calculate total: ")
            total_amount_rental(rid)
        elif choice == "11":
            display_rentals_in_progress()
        elif choice == "12":
            month = int(input("Month (1-12): "))
            year = int(input("Year: "))
            total_amount_month(month, year)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
