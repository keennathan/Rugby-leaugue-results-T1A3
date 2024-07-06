from operations import load_games, save_games, display_games_from_round, team_with_most_points_scored, add_match, collect_match_details, list_of_stadiums, list_of_teams, display_menu
from tabulate import tabulate
from colorama import Fore, Style, init
import sys

# initilising colorama
init()


FILE_PATH = './data/SeasonData.json'

def main():
    matches = load_games(FILE_PATH)

    if not matches:
        print(Fore.RED + "No games loaded or an error has occurred." + Style.RESET_ALL)
        return
    
    while True:
        display_menu()
        choice = input(Fore.CYAN + "Make a selection: " + Style.RESET_ALL)

        if choice == '1':
            try:
                round_number = int(input(Fore.CYAN +"Enter the round number: " + Style.RESET_ALL))
                results = display_games_from_round(matches, round_number)
                if results:
                    # Prepare data for tabulate
                    headers = ["MatchNumber", "Date", "Location", "HomeTeam", "AwayTeam", "HomeTeamScore", "AwayTeamScore"]
                    table = [[result["MatchNumber"], result["Date"], result["Location"], result["HomeTeam"], result["AwayTeam"], result["HomeTeamScore"], result["AwayTeamScore"]] for result in results]
                    
                    # Print table
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else:
                    print(Fore.RED + f"No results found for round {round_number}." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid round number." + Style.RESET_ALL)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


        elif choice == "2":
            try:
                top_team, max_points = team_with_most_points_scored(matches)
                print(Fore.CYAN + f"The team who has scored the most points is {top_team} with {max_points} points."+ Style.RESET_ALL)
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

        elif choice == '4':
            list_teams = list_of_teams(matches)
            if list_teams:
                headers = ["All the different Teams"]
                table = [[location] for location in list_stadiums]
                print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="grid") + Style.RESET_ALL)
            else:
                print("No stadiums found.")


        elif choice == '5':
            teams = list_of_teams(matches)
            if teams:
                headers = ["All the different Teams"]
                table = [[team] for team in teams]
                print(Fore.CYAN + tabulate(table, headers=headers, tablefmt="grid") + Style.RESET_ALL)
            else:
                print("No teams found.")


        elif choice == '0':
            save_games(FILE_PATH, matches)
            print("Saving and exiting the program.")
            sys.exit(0)
        
        else:
            print(Fore.RED + "Invalid selection.  Enter selection between 0 - 5" + Style.RESET_ALL)


if __name__ == "__main__":
    main()