#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def walk():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and wall_in_front():
        turn_left()
    elif wall_on_right() != True and is_facing_north():
        turn_right()
        move()
        turn_right()
    elif wall_on_right() != True and front_is_clear():
        move()

while at_goal() != True:
    walk()