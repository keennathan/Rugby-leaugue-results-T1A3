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
This feature will let the user select a round and will print out the results of all the games in that round.
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


