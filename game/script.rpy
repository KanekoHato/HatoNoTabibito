# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ka = Character("Kaneko", color="#cc33ff")
define pname = Character("[Anonymous]", color="#ff5050")
define na = Character("Narrator", color="#ffffff")
define audio.bgmone = "audio/bgmone.ogg"
define audio.flaps = "audio/wingsflap.mp3"
define audio.story = "audio/storytime.ogg"
define audio.horror = "audio/horror.ogg"
define skiphistory = "None"

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 1.0
    python:
        pname = renpy.input("What Is Your Name?")
        pname = pname.strip()

        if not pname:
            pname = "Wakashigihime"

    stop music fadeout 1.0
    scene bg bedroom
    with fade

    play music bgmone
    show hato standby at right
    ka "Nice nice to meet you [pname]"
    ka "Before you know more about me how about ..."
    ka "We talk about my past for a little ?"

    menu:

        ka "Do you want to listen to it?"

        "Yes, I Want To Know The Past":
            $skiphistory = False
            jump storymode

        "No, Go Straight To Introduction":
            $skiphistory = True
            jump skiphistory

    pname "Okay so what is your past, Kaneko?"

label storymode:
    stop music fadeout 1.0

    scene bg sky
    with fade
    play sound flaps
    play music story

    ka "Stupid Yagoo, always ask me for help"
    jump introduce



label introduce:
    scene bg bedroom
    stop music fadeout 1.0
    play music bgmone
    with fade
    show hato standby at right
    na "After A Few Moments .........."





label skiphistory:
    scene bg bedroom
    stop music fadeout 1.0
    play music horror
    with fade
    show hato standby at right
    ka "So sad..... so you didnt want to know or hear about my past? [pname]"
    ka "Its unfortunate, B But it has come to this ..."
    pname "W what ? "
    ka "EHEHEHEHEHEHEHEHEHEHEHEHEHE"
    ka "EHEHEHEHEHEHEHEHEHEHEHEHEHE\nHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEEHEHEHEHEHE"
    ka "EHEHEHEHEHEHEHEHEHEHEHE\nHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEEHEHEHEHEHEEH\nEHEHEHEHEHEHEHEHEHEHEHEHEHE\nHEHEHEHEHEHEHEHEHEHEHEHEHEHEEHEHEHEHEHE"
    na "Kaneko grabs a box from under the bed and open it, she wears the thing"
    na "it turn out it was a beak mask"
    na "Suddenly Kaneko proppel herself forwad and then stab [pname] right into the heart with her beak mask !!!"
    pname "AAAAAAAAAAAAAAAAA"
    "Congratulations Now You're Dead"
    "Game Over"












    return
