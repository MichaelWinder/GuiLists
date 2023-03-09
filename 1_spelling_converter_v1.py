import easygui
while True:
    nzWord = list(easygui.enterbox("Enter the NZ word you would like to "
                                   "translate: "))
    nzWord.remove("u")
    easygui.msgbox("".join(nzWord))
