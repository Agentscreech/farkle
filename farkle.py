#!python3
import random
from collections import Counter

#scoring functions
def check_set_of_six(dice: list) -> int:
    dice_count = Counter(dice)
    for i in range(1, 7):
        if dice_count[i] == 6:
            return 3000
    return 0


def check_set_of_five(dice: list) -> int:
    dice_count = Counter(dice)
    for i in range(1, 7):
        if dice_count[i] == 5:
            return 2000
    return 0


def check_set_of_four(dice: list) -> int:
    dice_count = Counter(dice)
    for i in range(1, 7):
        if dice_count[i] == 4:
            return 1000
    return 0


def check_four_two(dice: list) -> int:
    dice_count = Counter(dice)
    four = False
    two = False
    for i in range(1, 7):
        if dice_count[i] == 4:
            four = True
            continue
        if dice_count[i] == 2:
            two = True
            continue
    if four == True and two == True:
        return 1500
    return 0

def check_three_pair(dice: list) -> int:
    dice_count = Counter(dice)
    one = False
    two = False
    three = False
    for i in range(1, 7):
        if dice_count[i] == 2 and one == False:
            one = True
            continue
        if dice_count[i] == 2 and two == False:
            two = True
            continue
        if dice_count[i] == 2 and three == False:
            three = True
            continue
    if one != False and two != False and three != False:
        return 1500
    return 0

def check_three_triplets(dice: list) -> int:
    dice_count = Counter(dice)
    one = False
    two = False
    for i in range(1, 7):
        if dice_count[i] == 3 and one == False:
            one = True
            continue
        if dice_count[i] == 3 and two == False:
            two = True
            continue
    if one != False and two != False:
        return 2500
    return 0

def check_straight(dice: list) -> int:
    dice.sort() 
    if dice == [1,2,3,4,5,6]:
        return 1500
    return 0

def check_triple(dice: list) -> int:
    dice_count = Counter(dice)
    for i in range(1, 7):
        if dice_count[i] == 3:
            return i*100
    return 0

def check_ones(dice: list) -> int:
    dice_count = Counter(dice)
    return dice_count[1]*100

def check_fives(dice: list) -> int:
    dice_count = Counter(dice)
    return dice_count[5]*50


def score_dice(dice: list) -> int:
    temp_score = 0
    ones_qty = Counter(dice)[1]
    fives_qty = Counter(dice)[5]
    if check_straight(dice) > temp_score:
        temp_score = check_straight(dice)

    if check_set_of_six(dice) > temp_score:
        temp_score = check_set_of_six(dice)

    if check_set_of_five(dice) > 0:
        if ones_qty == 5:
            if check_set_of_five(dice) + check_fives(dice) > temp_score:
                temp_score = check_set_of_five(dice) + check_fives(dice)
        elif fives_qty == 5:
            if check_set_of_five(dice) + check_ones(dice) > temp_score:
                temp_score = check_set_of_five(dice) + check_ones(dice)
        else:
            if check_set_of_five(dice) + check_fives(dice) + check_ones(dice) > temp_score:
                temp_score = check_set_of_five(dice) + check_fives(dice) + check_ones(dice)

    if check_set_of_four(dice) > 0:
        if ones_qty == 4:
            if check_set_of_four(dice) + check_fives(dice) > temp_score:
                temp_score = check_set_of_four(dice) + check_fives(dice)
        elif fives_qty == 4:
            if check_set_of_four(dice) + check_ones(dice) > temp_score:
                temp_score = check_set_of_four(dice) + check_ones(dice)
        else:
            if check_set_of_four(dice) + check_fives(dice) + check_ones(dice) > temp_score:
                temp_score = check_set_of_four(dice) + check_fives(dice) + check_ones(dice)

    if check_four_two(dice) > temp_score:
        temp_score = check_four_two(dice)
    if check_three_pair(dice) > temp_score:
        temp_score = check_three_pair(dice)
    if check_three_triplets(dice) > temp_score:
        temp_score = check_three_triplets(dice)

    if check_triple(dice) > 0:
        if ones_qty == 3:
            if check_triple(dice) + check_fives(dice) > temp_score:
                temp_score = check_triple(dice) + check_fives(dice)
        elif fives_qty == 3:
            if check_triple(dice) + check_ones(dice) > temp_score:
                temp_score = check_triple(dice) + check_ones(dice)
        else:
            if check_triple(dice) + check_fives(dice) + check_ones(dice) > temp_score:
                temp_score = check_triple(dice) + check_fives(dice) + check_ones(dice)
    
    if check_ones(dice) + check_fives(dice) > temp_score:
        temp_score = check_ones(dice) + check_fives(dice)
    if check_ones(dice) > temp_score:
        temp_score = check_ones(dice)
    if check_fives(dice) > temp_score:
        temp_score = check_fives(dice)

    return temp_score

#a class that is used to keep track of the player's score
class Player:
    def __init__(self):
        self.score = 0
        self.dice = []
        self.held_dice = []
        self.held_score = 0
        self.name = input("Name of the player: ")

    def initial_roll(self) -> list:
        self.dice = [self.roll(), self.roll(), self.roll(), self.roll(), self.roll(), self.roll()]
    def roll(self) -> int:
        return random.randint(1, 6)
    def reroll(self) -> list:
        for i in range(len(self.dice)):
            self.dice[i] = self.roll()



def turn_flow(player: Player) -> None:
    player.initial_roll()
    print(f"Here are {player.name}'s dice after initial roll")
    farkled = False
    while not farkled:
        print(player.dice)
        temp_score = score_dice(player.dice)
        if temp_score == 0:
            print("Player Farkled!")
            farkled = True
            player.held_score = 0
            player.held_dice = []
            return
        else:
            if player.held_score != 0:
                print(f"{player.name} has {player.held_score} in held dice")
        print(f"This roll is currently worth {temp_score} points")
        reroll = input("Type 'done' to keep dice with this score or 'reroll' to reroll dice: ")
        reroll = reroll.lower()
        while reroll != "done" and reroll != "reroll":
            reroll = input("Type 'done' to keep dice with this score or 'reroll' to reroll dice: ")
        if reroll == "done":
            player.score += temp_score + player.held_score
            print(f"{player.name}'s score is now {player.score}")
            player.held_score = 0
            player.held_dice = []
            break
        elif reroll == "reroll":
            finished = False
            while not finished:
                print(player.dice)
                choice = input("Which dice would you like to keep? Input the index of the dice (zero indexed) Type 'Done' to finish: ")
                if choice.lower() == "done":
                    finished = True
                    continue
                else:
                    player.held_dice.append(player.dice[int(choice)])
                    player.dice.remove(player.dice[int(choice)])
            player.held_score = score_dice(player.held_dice)
            player.reroll()




def __main__():
    player1 = Player()
    player2 = Player()
    
    while player1.score < 10000 and player2.score < 10000:
        turn_flow(player1)
        if player1.score >= 10000:
            print(f"{player1.name} wins!")
            break
        turn_flow(player2)
        if player2.score >= 10000:
            print(f"{player2.name} wins!")
            break

if  __name__ == "__main__":
    __main__()
