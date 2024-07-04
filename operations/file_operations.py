import json
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
            games = json.load(file)
        return games
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error has occured: {e}.")
        return []
    

def save_games(file_path, games):
    """
    saves games to a JSON file

    parameters: file_path - Path to the JSON file

    """
    try:
        with open(file_path, 'w') as file:
            json.dump(games, file, indent=4)
        print(f"The game was successfully saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denide to write.")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")




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
        date = input("Enter the date (YYYY-MM-DD): ")
        location = input("Enter the stadium: ")
        home_team = input("Enter the home team: ")
        away_team = input("Enter the away team: ")
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