import datetime

def collect_user_preferences():
    user_prefs = {}
    user_prefs['name'] = input("Enter your name: ")
    user_prefs['destination'] = input("Preferred destination: ")
    user_prefs['start_date'] = input("Start date of the vacation (YYYY-MM-DD): ")
    user_prefs['end_date'] = input("End date of the vacation (YYYY-MM-DD): ")
    user_prefs['budget'] = float(input("What's your budget (in USD): "))
    user_prefs['payment_info'] = input("Enter payment information (dummy for now): ")
    user_prefs['calendar_access'] = input("Do you grant access to your calendar (yes/no)? ").lower() == 'yes'
    return user_prefs

def recommend_vacation_options(destination, budget):
    recommendations = {
        'flights': [
            {"airline": "AirGen", "price": 500, "duration": "10h"},
            {"airline": "SkyAI", "price": 450, "duration": "11h"}
        ],
        'hotels': [
            {"name": "Aston Hotel", "price_per_night": 120},
            {"name": "GenInn", "price_per_night": 100}
        ],
        'activities': [
            {"activity": "Discovery City Tour", "price": 50},
            {"activity": "GenAI Museum Visit", "price": 30}
        ]
    }
    
    print(f"Recommended flights to {destination}:")
    for flight in recommendations['flights']:
        print(f"Airline: {flight['airline']}, Price: {flight['price']}, Duration: {flight['duration']}")
    
    print(f"Recommended hotels in {destination}:")
    for hotel in recommendations['hotels']:
        print(f"Hotel: {hotel['name']}, Price per night: {hotel['price_per_night']}")
    
    print(f"Recommended activities in {destination}:")
    for activity in recommendations['activities']:
        print(f"Activity: {activity['activity']}, Price: {activity['price']}")

def plan_vacation(start_date, end_date, calendar_access):
    if calendar_access:
        print("Accessing calendar to check availability...")
        available = True  
        if available:
            print(f"Planning vacation from {start_date} to {end_date}.")
        else:
            print("Dates conflict with existing calendar events.")
    else:
        print("Calendar access not granted. Using provided dates.")

def book_flight(flight_option):
    print(f"Booking flight with {flight_option['airline']} for ${flight_option['price']}.")

def book_hotel(hotel_option, nights):
    total_price = hotel_option['price_per_night'] * nights
    print(f"Booking hotel {hotel_option['name']} for {nights} nights. Total cost: ${total_price}.")

def book_activity(activity_option):
    print(f"Booking activity: {activity_option['activity']} for ${activity_option['price']}.")

user_preferences = collect_user_preferences()
recommend_vacation_options(user_preferences['destination'], user_preferences['budget'])
plan_vacation(user_preferences['start_date'], user_preferences['end_date'], user_preferences['calendar_access'])

selected_flight = {"airline": "AirGen", "price": 500, "duration": "10h"}
selected_hotel = {"name": "Aston Hotel", "price_per_night": 120}
selected_activity = {"activity": "AI City Tour", "price": 50}

book_flight(selected_flight)
book_hotel(selected_hotel, nights=5)
book_activity(selected_activity)
