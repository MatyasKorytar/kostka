def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    if True:
        for index in range(randint(1, 6)):
            led.plot(randint(0, 4), randint(0, 4))
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
    else:
        for index2 in range(randint(1, 10)):
            led.plot(randint(0, 4), randint(0, 4))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
