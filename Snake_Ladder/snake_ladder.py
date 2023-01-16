# UC1- Single Player at Starting Position Zero
import random

def snake_ladder():
    """
        This function checks the options for snake,ladder or no play and updates the player
        position accordingly
    :return: None
    """
    player_position = 0
    print("Lets Start the Game")
    print("Player is at Start Position ", player_position)
    print("Lets Roll the Dice")
    number_on_dice = roll_dice()
    print("The Number on Dice is:", number_on_dice)
    player_options = random.randint(0, 2)
    # no_play = 0
    # ladder = 1
    # snake = 2
    match player_options:
        case 0:
            player_position = 0
        case 1:
            player_position += number_on_dice
        case 2:
            player_position -= number_on_dice
            if player_position < 0:
                player_position = 0

    print("Player Position is:", player_position)


def roll_dice():
    """
       This function will check the number comes on Dice after a dice-roll
    :return: Dice Number
    """
    dice = random.randint(1, 6)
    return dice


if __name__ == '__main__':
    snake_ladder()
