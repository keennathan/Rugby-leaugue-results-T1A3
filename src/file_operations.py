import json


def load_games(file_path):
    # """
    # load games from a JSON file

    # parameters: file_path - Path to the JSON file
    # returns: lists of games or an empty list if an error occurs

    # """

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
    # """
    # saves games to a JSON file

    # parameters: file_path - Path to the JSON file

    # """
    try:
        with open(file_path, 'w') as file:
            json.dump(games, file, indent=4)
        print(f"The game was successfully saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denide to write.")
    except Exception as e:
        print(f"An unexpected error has occured: {e}")