from Model import BallBounceModel
import tkinter
import random
import math


def parameterForm():
    """ Creates a form to change the initial values."""
    ballWindows = tkinter.Tk()
    ballWindows.title("Ball Bounce")
    ballWindows.geometry("250x300")

    x = tkinter.DoubleVar(value=BallBounceModel.INITIAL_X)
    y = tkinter.DoubleVar(value=BallBounceModel.INITIAL_Y)
    speed = tkinter.DoubleVar(value=BallBounceModel.INITIAL_SPEED)
    angle = tkinter.DoubleVar(value=BallBounceModel.INITIAL_ANGLE)
    radius = tkinter.DoubleVar(value=BallBounceModel.INITIAL_RADIUS)
    gravity = tkinter.DoubleVar(value=BallBounceModel.gravity)
    frictionX = tkinter.DoubleVar(value=BallBounceModel.frictionX)
    frictionGround = tkinter.DoubleVar(value=BallBounceModel.frictionY)
    timeInterval = tkinter.DoubleVar(value=BallBounceModel.interval)
    showBall = tkinter.BooleanVar(value=BallBounceModel.INITIAL_SHOW_BALL)
    showVector = tkinter.BooleanVar(value=BallBounceModel.INITIAL_SHOW_VECTOR)
    traceVector = tkinter.BooleanVar(value=BallBounceModel.INITIAL_TRACE_VECTOR)

    tkinter.Label(ballWindows, text='x =').grid(row=0, column=0)
    tkinter.Entry(ballWindows, textvariable=x).grid(row=0, column=1)

    tkinter.Label(ballWindows, text='y =').grid(row=1, column=0)
    tkinter.Entry(ballWindows, textvariable=y).grid(row=1, column=1)

    tkinter.Label(ballWindows, text='speed =').grid(row=2, column=0)
    tkinter.Entry(ballWindows, textvariable=speed).grid(row=2, column=1)

    tkinter.Label(ballWindows, text='angle =').grid(row=3, column=0)
    tkinter.Entry(ballWindows, textvariable=angle).grid(row=3, column=1)

    tkinter.Label(ballWindows, text='radius =').grid(row=4, column=0)
    tkinter.Entry(ballWindows, textvariable=radius).grid(row=4, column=1)

    tkinter.Label(ballWindows, text='gravity =').grid(row=5, column=0)
    tkinter.Entry(ballWindows, textvariable=gravity).grid(row=5, column=1)

    tkinter.Label(ballWindows, text='Friction X =').grid(row=6, column=0)
    tkinter.Entry(ballWindows, textvariable=frictionX).grid(row=6, column=1)

    tkinter.Label(ballWindows, text='Friction Ground =').grid(row=7, column=0)
    tkinter.Entry(ballWindows, textvariable=frictionGround).grid(row=7, column=1)

    tkinter.Label(ballWindows, text='Time Interval =').grid(row=8, column=0)
    tkinter.Entry(ballWindows, textvariable=timeInterval).grid(row=8, column=1)

    tkinter.Label(ballWindows, text='Show ball =').grid(row=9, column=0)
    tkinter.Checkbutton(ballWindows, variable=showBall).grid(row=9, column=1)

    tkinter.Label(ballWindows, text='Show vector =').grid(row=10, column=0)
    tkinter.Checkbutton(ballWindows, variable=showVector).grid(row=10, column=1)

    tkinter.Label(ballWindows, text='Trace vector =').grid(row=11, column=0)
    tkinter.Checkbutton(ballWindows, variable=traceVector).grid(row=11, column=1)

    tkinter.Button(ballWindows,
                   text='Throw the ball',
                   command=lambda: throwBall(ballWindows,
                                             x,
                                             y,
                                             speed,
                                             angle,
                                             radius,
                                             gravity,
                                             frictionX,
                                             frictionGround,
                                             timeInterval,
                                             showBall,
                                             showVector,
                                             traceVector)
                   ).grid(row=12, column=0)

    tkinter.Button(ballWindows,
                   text='Full random',
                   command=lambda: throwBallRandom(ballWindows, showBall, showVector, traceVector)
                   ).grid(row=12, column=1)

    ballWindows.mainloop()


def throwBall(ballWindows, x, y, speed, angle, radius, gravity, frictionX, frictionGround, timeInterval, showBall,
              showVector, traceVector):
    """ Close the ball's form and initializes the values with user's entries."""

    changeInitialData(x.get(), y.get(), speed.get(), angle.get(), radius.get(), gravity.get(),
                      frictionX.get(), frictionGround.get(), timeInterval.get())
    BallBounceModel.showBall = showBall.get()
    BallBounceModel.showVector = showVector.get()
    BallBounceModel.traceVector = traceVector.get()
    ballWindows.destroy()


def throwBallRandom(ballWindows, showBall, showVector, traceVector):
    """ Close the ball's form and initializes the values with random entries."""
    changeInitialData(random.randint(0, BallBounceModel.boxWidth), random.randint(0, BallBounceModel.boxHeight),
                      random.randint(0, 200),
                      random.randint(0, 180), random.randint(1, 200),
                      random.randint(0, 2000) / 100,
                      random.randint(80, 100) / 100,
                      random.randint(80, 100) / 100,
                      random.randint(0, 10) / 10 + 0.1)
    BallBounceModel.showBall = showBall.get()
    BallBounceModel.showVector = showVector.get()
    BallBounceModel.traceVector = traceVector.get()
    ballWindows.destroy()


def changeInitialData(x, y, speed, angle, radius, gravity, frictionX, frictionGround, timeInterval):
    """ Change the initial values."""
    BallBounceModel.ball['x'] = x
    BallBounceModel.ball['y'] = y
    BallBounceModel.ball['speedX'] = speed * math.cos(math.radians(angle))
    BallBounceModel.ball['speedY'] = speed * math.sin(math.radians(angle))
    BallBounceModel.ball['angle'] = angle
    BallBounceModel.ball['radius'] = radius
    BallBounceModel.gravity = gravity
    BallBounceModel.frictionX = frictionX
    BallBounceModel.frictionGround = frictionGround
    BallBounceModel.timeInterval = timeInterval
