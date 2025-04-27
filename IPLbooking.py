# IPL Ticket Booking System with GST

print("Welcome to the IPL Ticket Booking System!")

# Ticket prices for each team (base price without GST)
ticket_prices = {
    "CSK": 2000,
    "DC": 1900,
    "PK": 1700,
    "HYD": 1600,
    "RR": 2000,
    "GT": 2300,
    "LUG": 1500
}

GST_RATE = 0.12  # 12% GST

# Display available teams and their ticket prices
print("\nAvailable Teams and Ticket Prices (excluding GST):")
for team, price in ticket_prices.items():
    print(f"{team}: ₹{price}")

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
            # Calculate total cost with GST
            base_cost = ticket_prices[selected_team] * num_tickets
            gst_amount = base_cost * GST_RATE
            total_cost = base_cost + gst_amount
            print(f"\nBooking successful! You have booked {num_tickets} tickets for {selected_team}.")
            print(f"Base cost: ₹{base_cost}")
            print(f"GST (12%): ₹{gst_amount:.2f}")
            print(f"Total cost (including GST): ₹{total_cost:.2f}")
    except ValueError:
        print("Invalid input! Please enter a valid number of tickets.")
else:
    print("Invalid team selected! Please choose a valid team from the list.")