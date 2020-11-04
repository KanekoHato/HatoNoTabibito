# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ka = Character("Kaneko Hato", color="#cc33ff")
define pname = Character("[Anon]", color="#ff5050")
define na = Character("Narrator", color="#ffffff")
define age = Character("[age]", color="#ffffff")
define audio.bgmone = "audio/bgmone.ogg"
define audio.flaps = "audio/wingsflap.mp3"
define audio.zapped = "audio/zapped.mp3"
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
            pname = "Ethel Chamomile"

        age = renpy.input("Please Enter Your Age")
        age = age.strip()
        if not age:
            age = "21"

        #pnamef = renpy.input("What Is Your First Name?")
        #pnamef = pnamef.strip()
        #if not pnamef:
        #    pnamef = "Ethel"

        #pnamel = renpy.input("What Is Your Last Name?")
        #pnamel = pnamel.strip()
        #if not pnamel:
        #    pnamel = "Chamomile"


    stop music fadeout 1.0
    scene bg house
    with fade

    play music bgmone
    show hato standby at left

    ka "[pname] Welcome to my home !!! its tough to get here eh? come, come inside ...."
    pname "Oh sure sure!, Lets Go Inside !!!!"
    na "[pname] Getting excited while entering [ka] house"
    ka "Lets talk in my room"
    na "[pname] Wants to hug [ka] from behind but [pname] is a shy person so [pname] didnt do it"
    ".... Such a shame ...."
    scene bg bedroom
    show hato standby
    ka "Nice nice to meet you [pname]"
    ka "Before you know more about me how about ..."
    ka "We talk about my past for a little ?"
    show hato standby at right
    menu:

        ka "Do you want to listen to it?"

        "Yes, I Want To Know The Past":
            jump storymode

        "No, Go Straight To Introduction":
            jump skiphistory

    pname "Okay so what is your past, Kaneko?"

label storymode:
    stop music fadeout 1.0

    scene bg sky
    with fade
    play sound flaps
    play music story
    stop sound
    ka "Stupid Yagoo, always ask me for help"
    na "Suddenly A lightning strikes [ka]"
    play sound zapped
    ka "Aaaaaaaa nooo im falling !!!!!"
    scene bg magicarray
    stop sound
    ka "Wah, what is that maggic array doing over there !!!!"
    ka "Aaaaaah ~ Im getting sucked by a maggic array !!! "
    na "Magic arrray engulfed all of [ka]  body and her vision getting blurred as she passed out"
    scene bg grassland
    show hato standby at right
    "Chrip Chrip Chrip"
    ka "Uuuuh w-what had just happened Aaaah my head ........,"
    "*looks around*"
    ka "What wait  where the fark i am ?!"
    ka "Am i in the middle of a grassland that who know where the fark it is ?!!!"
    ka "Uh what is that ? is that a building ?\nbut it was impossible that the building\ncould be so high that it could reach the sky !!"
    ka "Stupid yagoo if its not because of you !!!,\nill not be zapped and transported here !!!!"
    show hato depressed at center
    ka "Crap what happen to my body !!!"
    ka "Why am i transforming into hooman?"
    ka "My wings !!! its gone !!!"
    show hato standby at right
    ka "Oh wait, i can still felt mana inside of me"
    ka "Maybe i could still fly using my magic power ?!!!"
    ka "Ah well never mind ill think about it later , now ill just explore this place"
    ka "Woah what is this thing on my clothes is this a wings ?"
    ka "Oh i can felt my wings , so this symbol now is my wings ?!! nice !!"
    stop sound
    stop music fadeout 1.0
    jump introduce



label introduce:
    scene bg bedroom
    stop music fadeout 1.0
    play music bgmone
    with fade
    show hato standby at center
    na "After A Few Moments .........."
    ka "Thats my story !!"
    ka "My past is intresting right so\nwhat do you want to know about me?"
    ka "Wait a moment , let me change my clothes"
    "......."
    ".........."
    show hato cute at left
    ka "Alright im back !!!"
    ka "Am i cute ?"

    menu:

        na "At this moment [pname] knows that [pname] must answer something to increase [ka] impression"

        "Yes, You are very cute !!":
            $cute = True

        "It looks good on you but nothing changed":
            $cute = False

    ka "Thanks!! , Ill remember that !!!"
    pname "So.....Tell me, what is your favourite food ?"
    ka "My favourite food is rendang & Pizza !!"
    ka "Its a meaty food made from beef meat or chicken ~"
    ka "You should make it by  yourself like Battle Programmer does"
    ka "Or you can just buy it from your store !!!"
    ka "Also you could mix rendang with jackfruit condement"
    ka "So the summary is rendang taste is like a beef meat mixed with"
    ka "many spices and cooked with the spices untill the spices absorbed by the meat"
    ka "also i love pizza , but not the one that has pineapple i find it didnt goes well\nwith the meat"
    pname "How could you became a VTuber?"
    ka "Oh i see okay after i came to this world i transformed into a pigeon that resemble hooman girl"
    ka "And after i learn hooman culture and learn so advance things with my magic"
    ka "I became a what that you guys called a programmer, and thats it , because i felt bored"
    ka "And i need more new friends , new connecion and i be came VTuber ! A Pigeon VTuber\nthat came from another world!!!"
    pname "Thats cool and such but what is your future goal [ka]? Became a hero ?! Demon slayer ?!"
    ka "I want my subjecs and citizen to enjoy me more and make everyone happy and befirends everyone !!!"
    pname "Woah thats a cool goal !!! what about the content?!"
    ka "For now i want to make a inspirative content , educational, gaming content because hooman likes that\nalso maybe music content in the future"
    pname "What is your name?"
    ka "Really isnt it rude in hooman culture to ask about girls age?"

    menu:
        ka "Do you still want to know about my age  ?"
        "Yes":
            $askage = True
            pname "Yes Yes Yes YES [ka] !!! I Want To Know Your Age !!!\nHATO HATO HATO HATO,\nWANGI Wangi Wangi WANGI!!HUM WANGI !!"
            jump police

        "No":
            $askage = False
            pname "No, I think im fine"
            jump safe

label safe:
    ka "Well it doesnt matter anyway im already 20 on hooman age, but when in pigeon age im still 16"
    pname "Oh thats intresting"
    ka "I think i will also make some movie time together with my viewers !"
    pname "And so what is your hobby?"
    ka "My hobby? Of Course i like eating , gaming , reading book, travelling around the world and many other things !!"
    "*Clock is showing 21:00 PM*"
    ka "Wow i cant believe time is passing so fast!"
    pname "Ah i think its time for me to go home"
    ka "Yeah i agree , take care, before that"
    ka "Please took this emblem as my gratitude for visiting me here"
    pname "Thakyou so much [ka]"
    ka "A ?!!! Waah You're welcome, you can visit me again anytime!! just tell me beforehand"
    pname "Okay thanks for everything [ka]"
    na "*[ka] escort [pname] outside her house & close the doors*"
    "*Peek Peek*"
    ka "Ah finally the hooman is gone, now i can continue with my plan"
    ka "HeHeHeHeHe"
    jump end



label police:
    scene bg police
    stop music fadeout 1.0
    play music combat
    ka "Aaaaaaah, W What are you crazy !!!!"
    na "[ka] Pressing a buglary alarm button under her bed"
    "*Police Siren Sound*"
    play sound siren
    "MEGAPHONE : This is a police, We already got you surrounded!!!"
    "MEGAPHONE : [pname] We got you surrounded"
    pname "No No Please [ka]  Chan, Tell Me Your Age !, Please !"
    ka "Kyaaaaa ~ Mission Success, Take THE SHOT I Repeat THE SHOT !!!"
    na "Suddenly Theres a laser in [pname]  forehead"
    "*Thump **** Splat Splat ****"
    "*Thud*"
    na "Then a few seconds later [pname]  were cease to exist"
    "*RADIO : Are You okay Agent [ka]!!"
    ka "RADIO : Im Okay Director, Please Prepare The Exfil"
    "*RADIO : 10-4 Out , ETA 2 Minutes"
    "Congratulations Now You're Dead"
    "Game Over"
    stop music fadeout 1.0
    stop sound
    return


label skiphistory:
    scene bg bedroom
    stop sound
    stop music fadeout 1.0
    play music horror
    with fade
    show hato standby at right
    ka "So sad..... so you didnt want to know or hear about my past? [pname]"
    ka "First thing first let me hear about you first okay?"
    pname "What do you want to know?"
    ka "Tell me what is your age?"
    pname "My age is [age] now, i felt old already."
    ka "Ah intresting so you already lived for [age] years?"
    ka "Its unfortunate, B But it has come to this ..."
    pname "W what ? "
    ka "Such a pity, a young hooman like you that just lived for [age] years"
    ka "Need to be erased from the face of the earth ......"
    ka "EHEHEHEHEHEHEHEHEHEHEHEHEHE"
    ka "EHEHEHEHEHEHEHEHEHEHEHEHEHE\nHEHEHEHEHE"
    ka "EHEHEHEHEHEHEHEHEHEHEHE\nHEHEHEHEHEEHEHEHEHEH"
    na "Kaneko grabs a box from under the bed and open it, she wears the thing"
    na "it turn out it was a beak mask"
    na "Suddenly Kaneko proppel herself forwad and then stab [pname] right into the heart with her beak mask !!!"
    "*Schlp Crot*"
    pname "AAAAAAAAAAAAAAAAA"
    "*Thud*"
    "Congratulations Now You're Dead"
    "Game Over"
    stop sound
    stop music fadeout 1.0
    return

label end:
    scene bg bedroom
    play music maintheme
    na "Finally after they know each other [pname] go back to its own house"
    "Meanwhile"
    ka "Kukukukuku Finally i got a new subject!"
    ka "A new slave !! a new citizen my kingdom the Pigeoniest Kingdom !!!!"
    "Congratulation You, Finished The Game"
    "Thankyou For Playing"
    stop sound
    stop music fadeout 1.0
    return



    return
