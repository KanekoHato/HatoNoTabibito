label splashscreen:
    stop music fadeout 1.0
    stop sound
    scene black
    with Pause(1)

    play sound bell

    show splash with dissolve
    with Pause(2)

    scene black
    with Pause(2)

    show text "Squabber Gaming Presents..." with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)
    stop sound

    return
