label scene_1:
    scene bg house
    with fade

    play music bgmone
    show hato standby at left

    ka "[pname] Welcome to my home !!! its tough to get here eh?"
    ka "Come, follow me inside..."

    pname "Oh sure sure!"

    show hato walkbehind at right
    "*Trot Trot*"

    ka "So how's your day ?"

    pname "Its pretty tiring, anyway thanks for inviting me here"

    ka "Yeah no problem, right now i'm also free anyway"

    scene bg livingroom
    play sound doors
    "*Doors Open*"
    "...."
    "....."

    show hato handsear at center
    ka "So welcome to my house [pname]"
    ka "I hope you enjoy your stay"

    pname "Yeah, thanks"

    show hato standby at center
    ka "Also talking here might be boring so ..."
    ka "Lets go upstairs and talk in my room"

    pname "O Ooh, Really? Sure lets go then"

    scene bg stairs
    show hato walkbehind at left
    "*Trot Trot*"

    ka "Dont worry theres noone here right now anyway"
    ka "So we could talk about anything intresting !"

    scene bg roomexterior
    show hato handsear at right
    ka "So we have arrived at 2nd floor, lets go inside"

    play sound doors
    "*Doors Open*"
    "...."
    "....."

    scene bg bedroom
    show hato standby at center
    ka "Here we are [pname], its pretty messy right?"
    ka "You could sit anywhere you like !"

    pname "No, its not messy at all , its pretty tidy"

    ka "Thank you very much!"
    ka "Before we talk about me how about you listen to my past story?"

    pname "So now [ka] gonna told a story about your past ?"

    ka "Yea, pretty much like that"
    
    show hato standby at right
    menu:

        ka "So do you want to hear my past story?"

        "Yes, I Want To Know The Past":
            jump scene_2

        "No, Go Straight To Introduction":
            jump scene_1_bad_end
