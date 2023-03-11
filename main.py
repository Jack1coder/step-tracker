def on_gesture_shake():
    global steps
    steps += 1
    led.stop_animation()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
set_steps = 0

def on_forever():
    steps_1000 = 0
    basic.show_number(steps)
    if steps_1000:
        pass
    elif False:
        pass
basic.forever(on_forever)
