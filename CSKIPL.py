# IPL Ticket Booking System with GST, Match Dates, and Food Items 

print("Welcome to the IPL Ticket Booking System!")

# Ticket prices for each team (base price without GST)
ticket_prices = {
    "CSK": 5000,
    "DC": 4500,
    "PK": 4000,
    "HYD": 3500,
    "RR": 9000,
    "GT": 7745,
    "LUG": 7543
}

# Match dates for each team
match_dates = {
    "CSK": "2025-05-01",
    "DC": "2025-05-02",
    "PK": "2025-05-03",
    "HYD": "2025-05-04",
    "RR": "2025-05-05",
    "GT": "2025-05-06",
    "LUG": "2025-05-07"
}

# Food items and their prices (base price without GST)
food_items = {
    "Burger": 500,
    "Pizza": 840,
    "Sprite": 250,
    "Thumbs Up": 250,
    "Maza": 450,
    "Fruits": 950
}

GST_RATE = 0.12  # 12% GST

# Display available teams, ticket prices, and match dates
print("\nAvailable Teams, Ticket Prices (excluding GST), and Match Dates:")
for team, price in ticket_prices.items():
    print(f"{team}: ₹{price}, Match Date: {match_dates[team]}")

# User input for team selection
selected_team = input("\nEnter the team you want to book tickets for (e.g., CSK, DC): ").upper()

# Check if the selected team is valid
if selected_team in ticket_prices:
    try:
        # Input number of tickets
        num_tickets = int(input(f"Enter the number of tickets you want to book for {selected_team}: "))
        if num_tickets <= 0:
            print("Number of tickets must be greater than 0.")
        else:
            # Calculate ticket cost with GST
            base_cost = ticket_prices[selected_team] * num_tickets
            gst_amount = base_cost * GST_RATE
            total_ticket_cost = base_cost + gst_amount

            # Display food items
            print("\nAvailable Food Items (excluding GST):")
            for item, price in food_items.items():
                print(f"{item}: ₹{price}")

            # Input food selection
            selected_food = input("\nEnter the food item you want to purchase (e.g., Burger, Pizza): ").title()
            if selected_food in food_items:
                food_quantity = int(input(f"Enter the quantity of {selected_food}: "))
                if food_quantity > 0:
                    # Calculate food cost with GST 
                    food_base_cost = food_items[selected_food] * food_quantity
                    food_gst_amount = food_base_cost * GST_RATE
                    total_food_cost = food_base_cost + food_gst_amount
                else:
                    print("Food quantity must be greater than 0.")
                    total_food_cost = 0
            else:
                print("Invalid food item selected. No food added.")
                total_food_cost = 0

            # Final total cost
            grand_total = total_ticket_cost + total_food_cost

            # Display booking summary
            print(f"\nBooking successful! You have booked {num_tickets} tickets for {selected_team}.")
            print(f"Match Date: {match_dates[selected_team]}")
            print(f"Ticket Base Cost: ₹{base_cost}")
            print(f"Ticket GST (12%): ₹{gst_amount:.2f}")
            print(f"Total Ticket Cost (including GST): ₹{total_ticket_cost:.2f}")
            if total_food_cost > 0:
                print(f"Food Base Cost: ₹{food_base_cost}")
                print(f"Food GST (12%): ₹{food_gst_amount:.2f}")
                print(f"Total Food Cost (including GST): ₹{total_food_cost:.2f}")
            print(f"Grand Total (Tickets + Food): ₹{grand_total:.2f}")
    except ValueError:
        print("Invalid input! Please enter valid numbers for tickets or food quantity.")
else:
    print("Invalid team selected! Please choose a valid team from the list.")