from operations import load_games, save_games, display_games_from_round, team_with_most_points_scored, add_match, collect_match_details, list_of_stadiums, list_of_teams
from tabulate import tabulate
from colorama import Fore, Style, init
import sys

# initilising colorama
init()


FILE_PATH = './data/SeasonData.json'

def main():
    matches = load_games(FILE_PATH)

    if not matches:
        print("No games loaded or an error has occured")
        return
    
    while True:
        print(Fore.RED + "\nFooty Results Tracker" + Style.RESET_ALL)
        print(Fore.MAGENTA + "1." + Style.RESET_ALL, "Search for results from a round.")
        print("2. Display the team who has scored the most points.")
        print("3. Add a match.")
        print(Fore.MAGENTA + "4." + Style.RESET_ALL, "Display the different stadiums.")
        print("5. List of all teams.")
        print("0. Save and exit.")

        choice = input("\nMake a selection: ")
        if choice == '1':
            try:
                round_number = int(input("Enter the round number: "))
                results = display_games_from_round(matches, round_number)
                if results:
                    # Prepare data for tabulate
                    headers = ["MatchNumber", "Date", "Location", "HomeTeam", "AwayTeam", "HomeTeamScore", "AwayTeamScore"]
                    table = [[result["MatchNumber"], result["Date"], result["Location"], result["HomeTeam"], result["AwayTeam"], result["HomeTeamScore"], result["AwayTeamScore"]] for result in results]
                    
                    # Print table
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else:
                    print(f"No results found for round {round_number}.")
            except ValueError:
                print("Invalid input. Please enter a valid round number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


        elif choice == "2":
            try:
                top_team, max_points = team_with_most_points_scored(matches)
                print(f"The team who has scored the most points is {top_team} with {max_points} points.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


        elif choice == '3':
            new_match = collect_match_details(FILE_PATH)
            if new_match:
                add_match(FILE_PATH, new_match)
                

        elif choice == '4':
            list_stadiums = list_of_stadiums(matches)
            if list_stadiums:
                headers = ["All the different Stadiums"]
                table = [[location] for location in list_stadiums]
                print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="grid") + Style.RESET_ALL)
            else:
                print("No stadiums found.")


        elif choice == '5':
            teams = list_of_teams(matches)
            if teams:
                headers = ["All the different Teams"]
                table = [[location] for location in teams]
                print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="grid") + Style.RESET_ALL)
            else:
                print("No teams found.")


        elif choice == '0':
            save_games(FILE_PATH, matches)
            print("Saving and exiting the program.")
            sys.exit(0)
        
        else:
            print("Invalid selection.  Enter selection between 0 - 5")


if __name__ == "__main__":
    main()