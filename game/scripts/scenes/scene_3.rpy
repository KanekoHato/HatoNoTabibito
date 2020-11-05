label scene_3:
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
    ka "Rendang Is a meaty food made from beef meat or chicken"
    ka "You could make it by  yourself or just buy it"
    ka "Ah i also love pizza !"
    ka "Oh sorry im getting out from the topics, Tehe ~"

    pname "Oh thats okay, i dont mind it."
    pname "So how could you became a VTuber?"

    ka "Oh i see okay after i came to this world i transformed into a pigeon that resemble hooman girl"
    ka "And after i learn hooman culture and learn so advance things with my magic"
    ka "I became a what that you guys called a programmer, and thats it , because i felt bored"
    ka "And i need more new friends , new connecion and i be came VTuber ! A Pigeon VTuber\nthat came from another world!!!"

    pname "Thats cool and such but what is your future goal [ka]? Became a hero ?! Demon slayer ?!"

    ka "I want my subjecs and citizen to enjoy me more and make everyone happy and befirends everyone !!!"

    pname "Woah thats a cool goal !!! what about the content?!"

    ka "For now i want to make a inspirative content , educational, gaming content because hooman likes that\nalso maybe music content in the future"

    pname "Can you tell me how old are you now?"
    
    ka "Really isnt it rude in hooman culture to ask about girls age?"

    menu:
        ka "Do you still want to know how old i'am?"
        "Yes":
            $askage = True
            pname "Yes Yes Yes YES [ka] !!! I Want To Know Your Age !!!\nHATO HATO HATO HATO,\nWANGI Wangi Wangi WANGI!!HUM WANGI !!"
            jump scene_3_bad_end

        "No":
            $askage = False
            pname "No, I think im fine"
            jump scene_4
