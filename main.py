from operations import load_games, save_games, display_games_from_round, team_with_most_points_scored
from tabulate import tabulate
from colorama import Fore, Style, init
init()


FILE_PATH = './data/SeasonData.json'

def main():
    matches = load_games(FILE_PATH)

    if not matches:
        print("No games loaded or an error has occured")
        return
    
    print(Fore.RED + "\nFooty Results Tracker" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1." + Style.RESET_ALL, "Search for results from a round.")
    print("2. Display the team who has scored the most points.")
    print("3. Add a match.")
    print("0. Save and exit.")

    choice = input("Make a selection: ")
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
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()