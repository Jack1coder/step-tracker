input.onGesture(Gesture.Shake, function () {
    steps += 1
    led.stopAnimation()
})
let steps = 0
let set_steps = 0
basic.forever(function () {
    let steps_1000 = 0
    basic.showNumber(steps)
    if (steps_1000) {
        basic.showString("\"well done nearly there\"")
    }
})
