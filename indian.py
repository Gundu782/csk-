def welcome():
    print("\n_________________\n")
    print("    WELCOME TO IPL EVENT\n")
    print("_________________\n")
    def show_matches():
        print("1. Match 1: Team A vs Team B")
        print("2. Match 2: Team C vs Team D")
        print("3. Match 3: Team E vs Team F")
        print("4. Match 4: Team G vs Team H")
        print("5. Match 5: Team I vs Team J")
        print("6. Match 6: Team K vs Team L")
        for i, match in enumerate(show_matches, start=1):
            print(f"{i}. {match['team1']} vs {match['team2']}")
            def book_ticket():
                print("Booking ticket...")
                name = input("Enter your name: ")
                match=input("Enter match number: ")
                tickets=int(input("Enter number of tickets: "))
                print(f"Booking confirmed for {name} for match {match} with {tickets} tickets.")
                def food_order():
                    print("\n Food Menu")
                    menu={1:"Pizza",2:"Burger",3:"Pasta",4:"Sandwich",5:"Soda"}
                    prices={1:200,2:150,3:250,4:100,5:50}
                    choice=int(input("Enter food choice: "))
                    qty=int(input("Enter quantity: "))
                    if choice in menu:
                        food=menu[choice]
                        price=prices[choice]
                        total_price=price*qty
                        gst=total_price+total_price*0.18
                        print(f"Food ordered: {food}, Quantity: {qty}, Total Price: {total_price}, GST: {gst}")
                        print("Food ordered successfully!")
                        print(f"Food ordered: {food}, Quantity: {qty}, Total Price: {total_price}")
                    else:
                        print("Invalid choice")
                        def toss_prediction():
                            print("Toss prediction...")
                            toss = input("Enter toss prediction (Team A or Team B): ")
                            if toss in ["Team A", "Team B"]:
                                print(f"Toss prediction for {toss} is successful!")
                            else:
                                print("Invalid toss prediction")
                                def dot_ball_prediction():
                                    print("Dot ball prediction...")
                                    dot_ball = input("Enter dot ball prediction (Yes or No): ")
                                    if dot_ball in ["Yes", "No"]:
                                        print(f"Dot ball prediction for {dot_ball} is successful!")
                                    else:
                                        print("Invalid dot ball prediction")
                                        def player_of_the_match_prediction():
                                            print("Player of the match prediction...")
                                            player = input("Enter player of the match prediction: ")
                                            print(f"Player of the match prediction for {player} is successful!")
                                            def player_of_the_match_prediction():
                                                player = input("Enter player of the match prediction: ")
                                                if player in ["Player A", "Player B", "Player C"]:
                                                    print(f"Player of the match prediction for {player} is successful!")
                                                    def player_of_the_series_prediction():
                                                        player = input("Enter player of the series prediction: ")
                                                        if player in ["Player A", "Player B", "Player C"]:
                                                            print(f"Player of the series prediction for {player} is successful!")
                                                        else:
                                                            print("Invalid player of the series prediction")
                                                            def fair_play_prediction():
                                                                player = input("Enter fair play prediction: ")
                                                                if player in ["Player A", "Player B", "Player C"]:
                                                                    print(f"Fair play prediction for {player} is successful!")
                                                                else:
                                                                    print("Invalid fair play prediction")   
                                                                    def orange_cap_prediction():
                                                                        player = input("Enter orange cap prediction: ")
                                                                        if player in ["Player A", "Player B", "Player C"]:
                                                                            print(f"Orange cap prediction for {player} is successful!")
                                                                        else:
                                                                            print("Invalid orange cap prediction")
                                                                            def purple_cap_prediction():
                                                                                player = input("Enter purple cap prediction: ")
                                                                                if player in ["Player A", "Player B", "Player C"]:
                                                                                    print(f"Purple cap prediction for {player} is successful!")
                                                                                else:
                                                                                    print("Invalid purple cap prediction")
                                                                                    def purple_cap_prediction():
                                                                                        player = input("Enter purple cap prediction: ")
                                                                                        if player in ["Player A", "Player B", "Player C"]:
                                                                                            print(f"Purple cap prediction for {player} is successful!")
                                                                                        else:
                                                                                            print("Invalid purple cap prediction")
                                                                                            def player_of_the_match_prediction():
                                                                                                player = input("Enter player of the match prediction: ")
                                                                                                if player in ["Player A", "Player B", "Player C"]:
                                                                                                    print(f"Player of the match prediction for {player} is successful!")
                                                                                                    def main():
                                                                                                        print("Welcome to IPL Event")
                                                                                                        print("1. Match 1: Team A vs Team B")
                                                                                                        print("2. Match 2: Team C vs Team D")
                                                                                                        print("3. Match 3: Team E vs Team F")
                                                                                                        print("4. Match 4: Team G vs Team H")
                                                                                                        print("5. Match 5: Team I vs Team J")
                                                                                                        print("6. Match 6: Team K vs Team L")
                                                                                                        def menu():
                                                                                                            print("\nMenu:")
                                                                                                    print("1>book match ticket")
                                                                                                    print("2>food order")
                                                                                                    print("3>toss prediction")
                                                                                                    print("4>dot ball prediction")
                                                                                                    print("5>player of the match prediction")
                                                                                                    print("6>player of the series prediction")
                                                                                                    print("7>fair play prediction")
                                                                                                    print("8>orange cap prediction")
                                                                                                    print("9>purple cap prediction")
                                                                                                    print("10>player of the match prediction")
                                                                                                    print("11>exit")
                                                                                                    def main():
                                                                                                        welcome()
                                                                                                        show_matches()
                                                                                                        while True:
                                                                                                            print("\nMenu:")
                                                                                                            print("1. Book Ticket")
                                                                                                            print("2. Food Order")
                                                                                                            print("3. Toss Prediction")
                                                                                                            print("4. Dot Ball Prediction")
                                                                                                            print("5. Player of the Match Prediction")
                                                                                                            print("6. Player of the Series Prediction")
                                                                                                            print("7. Fair Play Prediction")
                                                                                                            print("8. Orange Cap Prediction")
                                                                                                            print("9. Purple Cap Prediction")
                                                                                                            print("10. Player of the Match Prediction")
                                                                                                            print("11. Exit")
                                                                                                        choice=int(input("Enter your choice: "))
                                                                                                        if choice==1:
                                                                                                            book_ticket()
                                                                                                        elif choice==2:
                                                                                                            food_order()
                                                                                                        elif choice==3:
                                                                                                            toss_prediction()
                                                                                                        elif choice==4:
                                                                                                            dot_ball_prediction()
                                                                                                        elif choice==5:
                                                                                                            player_of_the_match_prediction()
                                                                                                        elif choice==6:
                                                                                                            player_of_the_series_prediction()
                                                                                                        elif choice==7:
                                                                                                            fair_play_prediction()
                                                                                                        elif choice==8:
                                                                                                            orange_cap_prediction()
                                                                                                        elif choice==9:
                                                                                                            purple_cap_prediction()
                                                                                                        elif choice==10:
                                                                                                            player_of_the_match_prediction()
                                                                                                        elif choice==11:
                                                                                                            print("Exiting...")
                                                                                                    
                                                                                                 
                                             
                                                                                                else:
                                                                                                        print("Invalid choice! Please try again.")


                                                                                                    
                                                                                                        
                                                                                                    
                                                                                                    

                                                                                            
            

                