label splashscreen:
    stop music fadeout 1.0
    stop sound
    scene black
    with Pause(1)

    play sound bell

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(2)

    show text "Squabber Gaming Presents..." with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    scene menu_animation_help at half_size with dissolve
    stop sound


    return
