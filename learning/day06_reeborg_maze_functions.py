def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while not wall_in_front():
        move()
        turn_right()
        while front_is_clear() is True:
            move()
            turn_right()


while not at_goal():
    if right_is_clear() is True:
        turn_right()
        move()
    elif front_is_clear() is True:
        move()
    else:
        turn_left()
