try:
    import pyautogui as pag
    import keyboard
    import time
    import os
except ModuleNotFoundError:
    # Open the batch that installs the missing extensions
    open('installMissingLibraries.bat')


def moveMouse():  # Opens the stickers menu
    pag.moveTo(584, 984, 0.5)
    pag.leftClick()
    pag.moveTo(481, 454, 2)
    for i in range(9):  # Click nine times since it doesn't work on the first one
        pag.leftClick()
    pag.moveTo(344, 520, 0.5)


def mouseSpam():  # Spams mouse click
    limit = int(input("Enter limit: "))
    usageInstructions = int(
        input("Would you like to recive usage instructions?\n[1] Yes \n[2] No \n? "))
    if usageInstructions != 1 and usageInstructions != 2:
        input("Invalid option, press enter to quit...")
        return
    elif usageInstructions == 1:
        print("---   Usage instructions   ---")
        input("Please, open WhatsApp and press enter...")
        input("Open the desired chat, move the window aside, and press enter...")
        moveMouse()
    else:
        input("Press enter when ready...")
        moveMouse()

    i = 0

    while i < limit:
        if keyboard.is_pressed("q"):  # When enter is pressed, end the spam
            print("We're done for today!")
            break
        pag.leftClick()
        i += 1


def keyboardSpam():
    limit = int(input("Enter limit: "))
    msg = input("Enter the message you want to spam: ")

    i = 0

    while i < limit:
        # Break from the loop if the key `enter is pressed`
        if keyboard.is_pressed("q"):
            print("We're done for today!")
            break
        time.sleep(0.3)
        pag.typewrite(msg)
        pag.press("enter")


def spamBot():
    confirm = 0
    while confirm != 1:
        print("------   Welcome to the Spamming Bot!   ------\nWhat would you like to do?")
        option = int(input("[1] Click Spamming \n[2] Message Spamming \n? "))
        confirm = int(
            input("Are you sure that's your desired option? \n[1] Yes \n[2] No \n? "))
        if confirm != 1 and confirm != 2:
            input("Invalid option, press enter to quit...")
            return

    if option == 1:
        mouseSpam()
    elif option == 2:
        keyboardSpam()


spamBot()
