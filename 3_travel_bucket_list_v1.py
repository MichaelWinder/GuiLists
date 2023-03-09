import easygui

favoriteFivePlaces = easygui.enterbox("Enter the names of 5 places you would "
                                      "most like to visit\nSeparate each place"
                                      " name with a comma", "Enter favorite "
                                      "places")
favoritePlacesList = favoriteFivePlaces.split(",")
lenFavoritePlaces = len(favoritePlacesList)

while lenFavoritePlaces != 5:
    easygui.msgbox("Sorry but you can only enter the names of 5 places and "
                   f"you entered {lenFavoritePlaces} places", "Error")
    favoriteFivePlaces = easygui.enterbox("Enter the names of 5 places you "
                                          "would most like to visit\nSeparate "
                                          "each place name with a comma",
                                          "Enter favorite places")
for place in favoritePlacesList:
    output = "\n* ".join(favoritePlacesList)
easygui.msgbox(f"My bucket list:\n\n* {output}", "Travel Bucket list")
