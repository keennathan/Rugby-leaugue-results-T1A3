

def display_games_from_round(matches, round_number):
    """
    Searches for match results from a specific round.
    
    Parameters:
    matches (list): A list of dictionaries, where each dictionary represents a match and contains the following keys:
        - 'MatchNumber' (int): The match number.
        - 'RoundNumber' (int): The round number.
        - 'Date' (str): The date of the match.
        - 'Location' (str): The location of the match.
        - 'HomeTeam' (str): The name of the home team.
        - 'AwayTeam' (str): The name of the away team.
        - 'HomeTeamScore' (int): The score of the home team.
        - 'AwayTeamScore' (int): The score of the away team.
    round_number (int): The round number to search for.
    
    Returns:
    list: A list of dictionaries containing the match results for the specified round. Returns an empty list if no matches are found.
    """
    try:
        results = [match for match in matches if match['RoundNumber'] == round_number]
        return results
    except KeyError as e:
        print(f"Key error: {e} - One of the matches is missing expected keys.")
    except TypeError as e:
        print(f"Type error: {e} - Input data is not in the expected format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

# add_game


# def most_points_scored():