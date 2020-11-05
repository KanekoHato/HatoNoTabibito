
label start:
    stop music fadeout 1.0
    python:
        pname = renpy.input("What Is Your Name?")
        pname = pname.strip()

        if not pname:
            pname = "Ethel Chamomile"

        age = renpy.input("Please enter Your Age")
        age = age.strip()
        if not age:
            age = "21"

    stop music fadeout 1.0

    jump scene_1
