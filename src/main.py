from file_operations import load_games, save_games
from games_operation import display_games_from_round 

FILE_PATH = '../data/SeasonData.json'

def main():
    matches = load_games(FILE_PATH)

    if not matches:
        print("No games loaded or an error has occured")
        return
    
    print("\nFooty Results Tracker")
    print("1. Search for results from a round.")

    choice = input("Make a selection: ")

    if choice == '1':
        try:
            round_number = int(input("Enter the round number: "))
            results = display_games_from_round(matches, round_number)
            if results:
                for result in results:
                    print(result)
            else:
                print(f"No results found for round {round_number}.")
        except ValueError:
            print("Invalid input. Please enter a valid round number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()