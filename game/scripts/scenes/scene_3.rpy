label scene_3:
    scene bg bedroom
    stop music fadeout 1.0
    play music bgmone
    with fade
    show hato standby at center

    na "After a few moments..."

    ka "And that's my story!"
    ka "My past is interesting, right? So..."
    ka "What else do you want to know about me?"
    ka "Wait a moment, let me change my clothes."

    "..."

    show hato cute at left
    ka "Alright! I'm back!"
    ka "Well?"
    ka "Is my outfit cute?"

    menu:
        na "At this moment [pname] knows that [pname] absolutely has to answer."

        "Yes, You are very cute!":
            $cute = True

        "It looks good on you, but nothing really changed":
            $cute = False

    ka "Thanks! I'll remember this!"

    pname "So..."
    pname "Tell me, what is your favourite food?"

    ka "My favourite foods are rendang and pizza!"
    ka "Rendang is a meaty food made from beef or chicken, you know."
    ka "You could make it at home or just buy it."
    ka "Ah! I also love pizza!"
    ka "Oh sorry! I'm getting ahead of myself, tehe ~"

    pname "Thats okay, I dont mind at all."
    pname "So... how could you became a VTuber?"

    ka "Oh! I see!"
    ka "After I came to this world I was transformed into a pigeon that resembles a human girl."
    ka "And after I learned so much about human culture with the help of my magic..."
    ka "I became what you guys would call a programmer. Pretty much just because I was bored."
    ka "And well, I met more new friends, made new connections and then I became a VTuber!"
    ka "A Pigeon VTuber that came from another world!"

    pname "Thats cool and such, but..."
    pname "What is your future goal, [ka]? Become a hero?! Maybe a demon slayer?!"

    ka "I want my subjects and citizens to enjoy me more!"
    ka "And also make everyone happy!"
    ka "Oh! And be friends with everyone!"

    pname "Woah! That are some cool goals! What about your content?"

    ka "For now I want to make inspirational content, maybe some educational stuff..."
    ka "And gaming for sure! Humans like that..."
    ka "Also... maybe music content in the future? That'd be cool!"

    pname "Can you tell me how old you are?"

    ka "Really!"
    ka "Isn't it super rude in human culture to ask about a girls age?"

    menu:
        ka "Do you really want to know how old I am?"
        "Yes":
            $askage = True
            pname "Yes Yes Yes YES [ka]! I Want To Know Your Age!\nHATO HATO HATO HATO,\nWANGI Wangi Wangi WANGI! HUM WANGI!"
            jump scene_3_bad_end

        "No":
            $askage = False
            pname "No, I think I'm fine."
            jump scene_4
