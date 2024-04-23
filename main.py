# Define 2d array to store the table in
table = [["-" for _ in range(3)] for _ in range(3)]



# Function that checks if there is a winner
def check_for_winner(t):
    # Checks for win by checking for matching row
    for i in t:
        if i[0] == i[1] == i[2] != "-":
            return i[0]

    # Checks for win by checking for matching column
    for j in range(2):
        if t[j][0] == t[j][1] == t[j][2] != "-":
            return t[j][0]
    # Checks for win via diagonal
    for i in range(2):
        if t[0][2-(i * 2)] == t[1][1] == t[2][2 * i] != "-":
            return t[1][1]

    # Returns dash if no current winner
    return "-"




# Function allows user to place on the board
def place_on_board(type, x, y):
    # If x and y are between 0 and 2 and are ints then desired placement does exist. If not then return error.
    if 0 <= x < 3 and 0 <= y < 3 and isinstance(x, int) and isinstance(y, int):
        # If desired place is empty, then place and return. If not then return error.
        if table[x][y] == "-":
            table[x][y] = type
            return 0
        else:
            print("Space is already occupied.")
            return 1
    else:
        print("Space selected is invalid.")
        return 1



# Function to print the table
def print_table(t):
    for i in range(3):
        print(f"{t[0][i]} | {t[1][i]} | {t[2][i]}")

# While true for the program
while True:

    # Asks user if they want to start game
    start_game = input("Would you like to start a new game? Type 'yes' if so.")

    # Starts new game if user typed 'yes'
    if start_game.lower() == "yes":
        # While game is active
        while True:
            # While player 1 hasnt made an acceptable placement
            while True:
                player1_move = input("Player 1, please choose the x and y coordinates for your move. "
                                     "Your input should be in the style 'x y'")
                player1_move_xy = player1_move.split()
                if place_on_board("X", int(player1_move_xy[0]), int(player1_move_xy[1])) == 0:
                    break
                else:
                    print("Input was not valid. Try again.")

            # Print table after player 1 has placed and check for winner
            print_table(table)
            outcome = check_for_winner(table)
            if outcome == "X":
                print("Player 1 has won!")
                break

            elif outcome == "O":
                print("Player 2 has won!")
                break

            # While player 1 hasnt made an acceptable placement
            while True:
                player2_move = input("Player 2, please choose the x and y coordinates for your move. "
                                     "Your input should be in the style 'x y'")
                player2_move_xy = player2_move.split()
                if place_on_board("O", int(player2_move_xy[0]), int(player2_move_xy[1])) == 0:
                    break
                else:
                    print("Input was not valid. Try again.")

            # Print table after player 2 has placed and check for winner
            print_table(table)
            outcome = check_for_winner(table)
            if outcome == "X":
                print("Player 1 has won!")
                break

            elif outcome == "O":
                print("Player 2 has won!")
                break
