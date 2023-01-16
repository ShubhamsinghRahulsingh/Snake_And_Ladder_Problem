# UC1- Single Player at Starting Position Zero
import random

def snake_ladder():
    """
        This function Checks for the player position to reach Exact winning position 100
        If reached then will print that player won the game
    :return: None
    """
    # no_play = 0
    # ladder = 1
    # snake = 2
    player_position = 0
    winning_position = 100
    print("Lets Start the Game")
    while player_position < winning_position:
        number_on_dice = roll_dice()
        player_options = random.randint(0, 2)
        match player_options:
            case 0:
                player_position += 0
            case 1:
                player_position += number_on_dice
                if player_position > winning_position:
                    player_position -= number_on_dice
            case 2:
                player_position -= number_on_dice
                if player_position < 0:
                    player_position = 0
        print("Player Position is: ", player_position)

    print("Congratulations You Won!")


def roll_dice():
    """
       This function will check the number comes on Dice after a dice-roll
    :return: Dice Number
    """
    dice = random.randint(1, 6)
    return dice


if __name__ == '__main__':
    snake_ladder()
