#Movie Recommendation Agent

import random
from datetime import datetime

print("Welcome to MovieMate \n")

# Step 1: Ask user's name
name = input("Enter your name: ")

# Step 2: Ask favorite genre
print("\nChoose Genre:")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Romance")

choice = int(input("\nEnter your choice (1-4): "))

# Step 3: Display available movies
movies = {
    1: ["Leo", "Vikram", "Dc"],
    2: ["Jathi Ratnalu", "F2", "DJ Tillu"],
    3: ["The Conjuring", "Masooda", "Smile"],
    4: ["Sita Ramam", "arjunreddy", "Love Story"]
}

genre_names = {
    1: "Action",
    2: "Comedy",
    3: "Horror",
    4: "Romance"
}

if choice in movies:
    print(f"\nAvailable {genre_names[choice]} Movies:")
    for movie in movies[choice]:
        print("-", movie)

    # Step 4: Ask which movie they want
    selected_movie = input("\nEnter movie: ")

    # Step 5: Show booking timings and details
    show_times = [
        "10:00 AM",
        "1:30 PM",
        "4:00 PM",
        "7:30 PM",
        "10:00 PM"
    ]

    show_time = random.choice(show_times)
    booking_date = datetime.now().strftime("%d-%b-%Y")

    print("\nBooking Confirmed!\n")
    print("Customer    :", name)
    print("Movie       :", selected_movie)
    print("Show Time   :", show_time)
    print("Booking Date:", booking_date)
    print("\nEnjoy your movie! ")

else:
    print("\nInvalid genre selection.")
