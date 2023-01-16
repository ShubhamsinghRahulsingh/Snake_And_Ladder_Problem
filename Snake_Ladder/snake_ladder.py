# UC1- Single Player at Starting Position Zero
import random

def snake_ladder():
    """
        This function Checks between the two player position who reaches Exact winning position 100 first
        If reached winning position then will print which player won the game
        Also count the number of times dice rolled by that player to win game
    :return: None
    """
    # no_play = 0
    # ladder = 1
    # snake = 2
    player1_position = 0
    player2_position = 0
    winning_position = 100
    dice_count = 0
    dice_count_player1 = 0
    dice_count_player2 = 0
    player1_turn = 0
    player2_turn = 1
    print("Lets Start the Game")
    check_turn = player_turn()
    while player1_position < winning_position and player2_position < winning_position:
        dice_count += 1
        if check_turn == player1_turn:
            check_turn = player2_turn
            number_on_dice = roll_dice()
            dice_count_player1 += 1
            player_option = random.randint(0, 2)
            match player_option:
                case 0:
                    player1_position += 0
                case 1:
                    player1_position += number_on_dice
                    check_turn = player1_turn
                    if player1_position > winning_position:
                        player1_position -= number_on_dice
                case 2:
                    player1_position -= number_on_dice
                    if player1_position < 0:
                        player1_position = 0
            print("Player1 Position is: ", player1_position)
        else:
            check_turn = player1_turn
            number_on_dice = roll_dice()
            dice_count_player2 += 1
            player_option = random.randint(0, 2)
            match player_option:
                case 0:
                    player2_position += 0
                case 1:
                    player2_position += number_on_dice
                    check_turn = player2_turn
                    if player2_position > winning_position:
                        player2_position -= number_on_dice
                case 2:
                    player2_position -= number_on_dice
                    if player2_position < 0:
                        player2_position = 0
            print("Player2 Position is: ", player2_position)

    if player1_position > player2_position:
        print("\nPlayer1 Won the Game")
        print("Number Of times First Player's Dice was Rolled to win Game :", dice_count_player1)
    else:
        print("\nPlayer2 Won the Game")
        print("Number Of times Second Player's Dice was Rolled to win Game:", dice_count_player2)
    print("Total Dice Rolled:", dice_count)


def roll_dice():
    """
       This function will check the number comes on Dice after a dice-roll
    :return: Dice Number
    """
    dice = random.randint(1, 6)
    return dice

def player_turn():
    """
        this function will toss for which player to start the game
    :return: Player turn
    """
    toss = random.randint(0, 1)
    return toss


if __name__ == '__main__':
    snake_ladder()