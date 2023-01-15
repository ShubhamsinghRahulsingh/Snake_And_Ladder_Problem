# UC1- Single Player at Starting Position Zero
import random

def snake_ladder():
    """
        This function checks for the starting Position of Single player and Roll a Dice to
        get number 
    :return: None
    """
    player_position = 0
    print("Lets Start the Game")
    print("Player is at Start Position ", player_position)
    print("Lets Roll the Dice")
    number_on_dice = roll_dice()
    print("The Number on Dice is:", number_on_dice)


def roll_dice():
    """
       This function will check the number comes on Dice after a dice-roll
    :return: Dice Number
    """
    dice = random.randint(1, 6)
    return dice


if __name__ == '__main__':
    snake_ladder()
