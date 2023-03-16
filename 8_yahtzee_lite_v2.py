import easygui
import random


def roll():
    return random.randint(1, 6)


def finalScore(pnum, proll):
    for i in range(6):
        occurrences = proll.count(i)
        if occurrences > 2:
            num = i
            break
    if occurrences < 3:
        easygui.msgbox(f"{proll}\n\nNothing!\nScore: 0", f"Player {pnum}")
        return 0
    else:
        if occurrences == 3:
            easygui.msgbox(f"{proll}\n\nThree of a kind!\nScore: 10",
                           f"Player {pnum}")
            return 10
        if occurrences == 4:
            easygui.msgbox(f"{proll}\n\nFour of a kind!\nScore: 30",
                           f"Player {pnum}")
            return 30
        if occurrences == 5:
            easygui.msgbox(f"{proll}\n\nFive of a kind!\nScore: 50",
                           f"Player {pnum}")
            return 50


def rerollDice(pnum, proll):
    rollAgain = easygui.ynbox(f"Player {pnum} rolled"
                              f" {proll}\n\nChoose:", f"Player {pnum}",
                              choices=("Roll again", "Stick"))
    if rollAgain:
        rollDice = easygui.multchoicebox(f"What dices do you want to "
                                         f"reroll\n{proll}",
                                         f"Reroll Dices", choices=("Dice 1",
                                                                   "Dice 2",
                                                                   "Dice 3",
                                                                   "Dice 4",
                                                                   "Dice 5",))
        if "Dice 1" in rollDice:
            proll.pop(0)
            proll.insert(0, roll())
        if "Dice 2" in rollDice:
            proll.pop(1)
            proll.insert(1, roll())
        if "Dice 3" in rollDice:
            proll.pop(2)
            proll.insert(2, roll())
        if "Dice 4" in rollDice:
            proll.pop(3)
            proll.insert(3, roll())
        if "Dice 5" in rollDice:
            proll.pop(4)
            proll.insert(4, roll())
        if "Dice 6" in rollDice:
            proll.pop(5)
            proll.insert(5, roll())
        easygui.msgbox(f"Your current dice rolls are\n{proll}", "Player "
                                                                f"{pnum}")
        return proll
    else:
        return proll


def yahtzee():
    player_1_Dice = []
    player_2_Dice = []
    p1score = 0
    p2score = 0
    p1name = easygui.enterbox("Enter the name of player 1:", "Player 1")
    p2name = easygui.enterbox("Enter the name of player 2:", "Player 2")

    for i in range(5):
        player_1_Dice.append(roll())
        player_2_Dice.append(roll())
    player_1_Dice = rerollDice("1", player_1_Dice)
    player_1_Dice = rerollDice("1", player_1_Dice)
    player_2_Dice = rerollDice("2", player_2_Dice)
    player_2_Dice = rerollDice("2", player_2_Dice)
    p1score += finalScore("1", player_1_Dice)
    p2score += finalScore("2", player_2_Dice)
    if p1score > p2score:
        easygui.ynbox(f"The winner is Player 1: {p1name} with a score of"
                      f" {p1score}\n\nPlayer 2: {p2name} scored {p2score}\n\n"
                      f"Do you want to play another round?", "Result")
    elif p2score > p1score:
        easygui.ynbox(f"The winner is Player 2: {p2name} with a score of"
                      f" {p2score}\n\nPlayer 1: {p1name} scored {p1score}\n\n"
                      f"Do you want to play another round?", "Result")
    else:
        ans = easygui.ynbox(f"You had a draw\n\nThe Score was: {p1score}\n\nDo"
                            f" you want to play another round?", "Result")
        if ans:
            yahtzee()
        else:
            quit()


yahtzee()
