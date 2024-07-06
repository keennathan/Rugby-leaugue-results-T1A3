# Rugby League Results Tracker
## Overview: 
This application was made to track rugby leaugue results.  The user will be able to look up results from a selected round, add a match, see which team has scored the most points in the season, see the list of stadiums played at, see the list of teams in the competion and save and exit the program. 

## Features: 
### Main Menu:
With this feature the user will be given a list of options choose from.  This will direct them to the different features of the application.
### The logic:
1. Loads the Matches:
    * the function starts by loading game matches from a specific path to the json file.
2. Checks if the matches are loaded:
    * If there are no matches loaded, it will print an error message and exit the function
3. Menu Loop:
    * The function enters the loop to display a menu and get the users choice:  
        * Displays a menu - Shows the user a list of options.  
        * User Input - Gets the users input.  
        * Option 1 Displays games from a round - Prompts the user for a round number and fetches and displays the specific round.  
        * Option 2 Team with the most points - Identifies the team who has scored the most points.  
        * Option 3 Add a new match - Collects details of a new match and adds it to the file.  
        * Option 4 Lists the stadiums - lists and displays the stadiums played at.  
        * Option 5 Lists the teams - Lists the teams that play in the competion.  
        * option 0 Exit - Saves and exits the program.  
        * Invalid selection - It prints an error message if the user doesn't enter a valid selection.  

### Display games from a round:
This function will let the user select a round and will print out the results of all the games in that round.
### The Logic:
1. Input Data:
    * 'matches' - A list of dictonaries where each dictonary represents a match and contains keys such as 'RoundNumber'.
    * 'round_number' - is a number that represents the round number we want to filter to.
2. List Comprehension:
    * Iterate over each dictionary('match') in the list 'matches'.
    * For each 'match', check if the value associated with the key 'RoundNumber' is equal to 'round_number'.
    * If it is True, add the 'match' dictionary to the resulting list.
    * If it is False, exclude the 'match' dictionary from the resulting list.
3. Assigning the results:
    * The resulting list, that contains only the dictionaries that meet the condition, is assigned to the variable 'results'.
4. Return Statement:
    * the 'results' list is then returned.

### Team with the most points scored:
This function will calculate which team has scored the most points across all the matches in the season.  
### The Logic:
1. Input Data:
    * 'matches' - A list of dictonaries where each dictonary represents a match and contains keys such as 'HomeTeam', 'HomeTeamScore', 'AwayTeam', and 'AwayTeamScore'.  
2. Initialize Dictionary:
    * Initialize an empty dictionary ('team_points') to store the total points scored by each team.  
3. Iterate Over Matches:
    * Loop though each 'match' in 'matches'.  
4. Update the Home Team points:
    * Extract the home team name ('home_team') and its score ('home_points').
    * If the home team is already in 'team_points', add the points to their existing total.
    * If the home team is not in 'team_points', add a new entry with their score.
5. Update the Away Team points:
    * Extract the away team name ('away_team') and its score ('away_points').
    * If the away team is already in 'team_points', add the points to their existing total.
    * If the away team is not in 'team_points', add a new entry with their score.  
6. Find team with most points:
    * Initialize 'max_points' to 0 and 'top_team' to 'None'.
    * Iterate over the 'team_points' dictionary.
    * For each team, if their points are greater than 'max_points', update 'max_points' and 'top_team'.
7. Return Statement:
    * Return the 'top_team' and 'max_points'.  



