# Judul Games

print("  ____                            ")
print(" / ___| __ _ _ __ ___   ___  ___  ")
print("| |  _ / _` | '_ ` _ \ / _ \/ __| ")
print("| |_| | (_| | | | | | |  __/\__ \ ")
print(" \____|\__,_|_| |_| |_|\___||___/ ")


print(" _____ _        _____            _____ ")
print("|_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ ")
print("  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ ")
print("  | | | | (__    | | (_| | (__    | | (_) |  __/ ")
print("  |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___| ")
print("------------- WELCOME TO THIS GAME -------------")
print("------------- HAVE FUN GUYS ^_^ --------------")
print("Games by Alya Mirza")

instructions = """
This will be our tic tac toe board

  1 | 2 | 3 
----|---|---
  4 | 5 | 6  
----|---|---
  7 | 8 | 9 

*rules:
1. Insert the spot number (1-9) to put your sign
2. You must fill all 9 spots to get the result
3. player 1 will go first


"""

sign_dictionary = []
for i in range(9):
    sign_dictionary.append(' ')

def print_board():
    board = f"""
    
      {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]} 
    ----|---|---
      {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}  
    ----|---|---
      {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]} 

    """
    print(board)


index_list = []
def take_input(player_name):
    while True:
        x = int(input(f"{player_name}: "))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print("This spot is blocked.")
                continue
            index_list.append(x)
            return x
        print("Please enter number between 1-9")


def calculate_result(player_one, player_two):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X' or  sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X' :  
        print(f"Congratulations {player_one}.!!! You WON.!")
        quit("Thanks both for joining this game.")
    elif sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'O' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'O' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'O' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'O' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'O' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'O' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'O' or  sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'O' :
        print(f"Congratulations {player_two}.!!! You WON.!")
        quit("Thanks both for joining this game.")
    

def main():
    player_one = input("Enter player one name (X): ")
    player_two = input("Enter player two name (O): ")
    print(f"Thanks for joining this game {player_one} and {player_two}")

    print(instructions)
    print(f"{player_one}'s sign will be - X")
    print(f"{player_two}'s sign will be - O")
    input("Enter any key to start the game: ")


    print_board()


    for i in range(9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_dictionary[index] = 'X'
        else:
            index = take_input(player_two)
            sign_dictionary[index] = 'O'
        
        print_board()
        calculate_result(player_one, player_two)

    print("This a TIE, Nobody WON. Play Again.")

main()

