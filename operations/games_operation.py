

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



def team_with_most_points_scored(matches):
    """
    Searches for the team that has scored the most points in the season.

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

    returns:
    A string with the team and the total points 

    """

    # A dictionary to store total points for each team
    team_points = {}

    for match in matches:
        # Add the points for the home team
        home_team = match["HomeTeam"]
        home_points = match["HomeTeamScore"]
        if home_team in team_points:
            team_points[home_team] += home_points
        else:
            team_points[home_team] = home_points

        # Add the points for the away team
        away_team = match["AwayTeam"]
        away_points = match["AwayTeamScore"]
        if away_team in team_points:
            team_points[away_team] += away_points
        else:
            team_points[away_team] = away_points

        # To find th team with the most points
    max_points = 0 
    top_team = None
    for team, points in team_points.items():
        if points > max_points:
            max_points = points
            top_team = team
    return top_team, max_points



# add_game