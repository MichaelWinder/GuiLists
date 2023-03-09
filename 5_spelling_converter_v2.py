import easygui


def nzToUs():
    nzWord = easygui.enterbox("Write the sentence you would like to turn "
                              "into American spelling", "Translator 9000")
    if "our" in nzWord or "ise" in nzWord or "yse" in nzWord:
        while "our" in nzWord:
            nzWord = nzWord.replace("our", "or")
        while "ise" in nzWord:
            nzWord = nzWord.replace("ise", "ize")
        while "yse" in nzWord:
            nzWord = nzWord.replace("yse", "yze")
        easygui.msgbox(f"The NZ sentence has been translated into the US "
                       f"spelling and is:\n{nzWord}", "Translator 9000")
    else:
        easygui.msgbox("There is no change in spelling", "Translator 9000")


while True:
    yorn = easygui.ynbox("Do you want to translate a sentence?", "Translator "
                         "9000")
    if yorn:
        nzToUs()
    else:
        quit()
