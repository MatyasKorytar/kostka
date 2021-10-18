input.onButtonPressed(Button.A, function () {
	
})
input.onGesture(Gesture.Shake, function () {
    if (true) {
        for (let index = 0; index < randint(1, 6); index++) {
            led.plot(randint(0, 4), randint(0, 4))
            music.playTone(262, music.beat(BeatFraction.Whole))
        }
    } else {
        for (let index = 0; index < randint(1, 10); index++) {
            led.plot(randint(0, 4), randint(0, 4))
        }
    }
})
