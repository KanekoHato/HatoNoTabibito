label scene_1:
    scene bg house
    with fade

    play music bgmone
    show hato standby at left

    ka "[pname]! Welcome to my home! It's a bit tough to get here, right?"
    ka "Come, follow me inside!"

    pname "Oh! Sure, sure."

    show hato walkbehind at right
    "*Trot Trot*"

    ka "So, How was your day?"

    pname "It was pretty tiring. Anyways, thanks for inviting me here!"

    ka "Yeah, no problem! Right now I'm also free anyway."

    scene bg livingroom
    play sound doors
    "*Doors Open*"
    "..."

    show hato handsear at center
    ka "So, welcome to my house, [pname]."
    ka "I hope you enjoy your stay!"

    pname "Yeah, thanks."

    show hato standby at center
    ka "Also..."
    extend "Talking here might be a bit boring, so ..."
    extend "Let's go upstairs and talk in my room!"

    pname "O-Oh, really? Sure! Let's go then!"

    scene bg stairs
    show hato walkbehind at left
    "*Trot Trot*"

    ka "Dont worry! There's no one here right now."
    ka "So we could talk about aaaanything you want~"

    scene bg roomexterior
    show hato handsear at right
    ka "Okay! We have arrived on the 2nd floor, let's go to my room!"

    play sound doors
    "*Doors Open*"
    "..."

    scene bg bedroom
    show hato standby at center
    ka "Here we are [pname]! Ah..."
    ka "I'm sorry for the mess."
    ka "Anyway, you can sit anywhere you like!"

    pname "It's not messy at all, its pretty tidy."

    ka "Thank you very much!"
    ka "Before we talk about me, would you like to hear a story about my past?"

    pname "Haha, what is this? [ka]s origin story?"

    ka "Yea, pretty much that."

    show hato standby at right
    menu:

        ka "So do you want to hear about my past?"

        "Yes, I want to know more about you.":
            jump scene_2

        "No, skip the past. Who cares anyway.":
            jump scene_1_bad_end
