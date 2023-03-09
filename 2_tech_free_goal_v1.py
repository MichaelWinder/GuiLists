import easygui
goal = 3
daysOnTech = easygui.enterbox("Please enter each of the days on which "
                              "you used technology\nSeparate each day "
                              "with a space", "Days tech was used")
daysOnTechList = daysOnTech.split(" ")
numDaysOnTech = len(daysOnTechList)
if goal <= numDaysOnTech:
    easygui.msgbox(f"Congratulations! You had {numDaysOnTech} tech-free "
                   f"days.\nThat is {numDaysOnTech - goal} more than your "
                   f"goal.", "Goal Achieved")
else:
    easygui.msgbox(f"FAIL! You had {numDaysOnTech} tech-free "
                   f"days.\nThat is {goal - numDaysOnTech} less than your "
                   f"goal.", "Goal FAILED")
