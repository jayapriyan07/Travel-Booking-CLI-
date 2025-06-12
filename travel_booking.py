import datetime

def save_booking(name, destination, date, passengers):
    with open("bookings.txt", "a") as file:
        file.write(f"{name},{destination},{date},{passengers}\n")

def main():
    print("✈️ Welcome to CLI Travel Booking System")
    name = input("Enter your name: ")
    destination = input("Enter destination: ")
    
    date = input("Enter travel date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return

    passengers = input("Enter number of passengers: ")
    if not passengers.isdigit() or int(passengers) <= 0:
        print("❌ Invalid passenger count.")
        return

    save_booking(name, destination, date, passengers)

    print("\n✅ Booking Confirmed!")
    print(f"👤 Name         : {name}")
    print(f"🌍 Destination  : {destination}")
    print(f"📅 Date         : {date}")
    print(f"👥 Passengers   : {passengers}")
    print("\n📁 Booking saved to bookings.txt")

if __name__ == "__main__":
    main()
