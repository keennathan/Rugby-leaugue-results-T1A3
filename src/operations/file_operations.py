import json
import datetime
from tabulate import tabulate
from colorama import Fore, Style, init

init()


def load_games(file_path):
    """
    load games from a JSON file

    parameters: file_path - Path to the JSON file
    returns: lists of games or an empty list if an error occurs

    """

    try:
        with open(file_path, 'r') as file:
            matches = json.load(file)
        return matches
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error has occured: {e}.")
        return []
    

def save_games(file_path, matches):
    """
    saves games to a JSON file

    parameters: file_path - Path to the JSON file

    """
    try:
        with open(file_path, 'w') as file:
            json.dump(matches, file, indent=4)
        print(f"Successfully saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denide to write.")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")


ALLOWED_TEAMS = [
    "Dragons", "Knights", "Sharks", "Storm", "Wests Tigers", "Cowboys", "Rabbitohs", 
    "Bulldogs", "Titans", "Broncos", "Sea Eagles", "Dolphins", "Raiders", "Warriors", 
    "Roosters", "Eels", "Panthers"
]

ALLOWED_LOCATIONS = [
    "Suncorp Stadium", "Scully Park", "McDonald Jones Stadium", "Kayo Stadium",
    "PointsBet Stadium", "Belmore Sports Ground", "AAMI Park", "BlueBet Stadium",
    "Queensland Country Bank Stadium", "Cbus Super Stadium", "Go Media Stadium",
    "Leichhardt Oval", "Allianz Stadium", "CommBank Stadium", "Netstrata Jubilee Stadium",
    "Campbelltown Sports Stadium", "Accor Stadium", "Allegiant Stadium", "Apollo Projects Stadium",
    "Industree Group Stadium", "WIN Stadium", "GIO Stadium", "Carrington Park",
    "4 Pines Park", "TIO Stadium"
]

def display_allowed_teams():
    headers = ["Teams"]
    table = [[team] for team in ALLOWED_TEAMS]
    print(Fore.YELLOW + tabulate(table, headers=headers, tablefmt="grid") + Style.RESET_ALL)

def display_allowed_locations():
    headers = ["Locations"]
    table = [[location] for location in ALLOWED_LOCATIONS]
    print(Fore.YELLOW + tabulate(table, headers=headers, tablefmt="grid") + Style.RESET_ALL)

def add_match(filepath, new_match):
    matches = load_games(filepath)
    if matches is None:
        print("Error loading matches. Cannot add new match")
        return
    
    matches.append(new_match)
    save_games(filepath, matches)
    print("Match added successfully.")

def get_next_match_number(matches):
    if not matches:
        return 1
    return max(match["MatchNumber"] for match in matches) + 1    

def collect_match_details(filepath):
    matches = load_games(filepath)
    if matches is None:
        print("Error loading matches.  Cannot collect the match details.")
        return None
    
    next_match_number = get_next_match_number(matches)

    try:
        round_number = int(input("Enter the round number: "))
        while True:    
            date = input("Enter the date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print(Fore.RED + "Invalid date format. Please enter the date in YYYY-MM-DD format." + Style.RESET_ALL) 

        #Display allowed locations
        display_allowed_locations()
        location = input(Fore.CYAN + "Enter the location: " + Style.RESET_ALL)
        while location not in ALLOWED_LOCATIONS:
            print(Fore.RED + "Invalid location. Please select a valid location from the list." + Style.RESET_ALL)
            location = input(Fore.CYAN + "Enter the location: " + Style.RESET_ALL)

        # Display allowed teams
        display_allowed_teams()
        home_team = input(Fore.CYAN + "Enter the home team: " + Style.RESET_ALL)
        while home_team not in ALLOWED_TEAMS:
            print(Fore.RED + "Invalid team. Please select a valid team from the list." + Style.RESET_ALL)
            display_allowed_teams()
            home_team = input(Fore.CYAN + "Enter the home team: " + Style.RESET_ALL)

        away_team = input(Fore.CYAN + "Enter the away team: " + Style.RESET_ALL)
        while away_team not in ALLOWED_TEAMS:
            print(Fore.RED + "Invalid team. Please select a valid team from the list." + Style.RESET_ALL)
            display_allowed_teams()
            away_team = input(Fore.CYAN + "Enter the away team: " + Style.RESET_ALL)

        home_team_score = int(input("Enter the home team score: "))
        away_team_score = int(input("Enter the away team score: "))

        new_match = {
            "MatchNumber": next_match_number,
            "RoundNumber": round_number,
            "Date": date,
            "Location": location,
            "HomeTeam": home_team,
            "AwayTeam": away_team,
            "HomeTeamScore": home_team_score,
            "AwayTeamScore": away_team_score
        }
        return new_match
    except ValueError:
        print("Invalid input. Please enter valid data.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None