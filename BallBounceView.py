"""
View : This module contains all the functions to show the ball in a windows

    PUBLIC
        initialize()
        update()
    PRIVATE
        __createWindows()
        __getBallX0Transformed()
        __getBallX1Transformed()
        __getBallY0Transformed()
        __getBallY1Transformed()
        __createBall()

"""
import tkinter
import BallBounceModel
import BallBounceController
import math

__WINDOWS_ZOOM = 1.3
__WINDOWS_WIDTH = int(BallBounceModel.BOX_WIDTH * __WINDOWS_ZOOM)
__WINDOWS_HEIGHT = int(BallBounceModel.BOX_HEIGHT * __WINDOWS_ZOOM)

__windows = 0
__canvas = 0
__ballDraw = 0
__arrow = 0
__showBall = BallBounceModel.INITIAL_SHOW_BALL
__showVector = BallBounceModel.INITIAL_SHOW_VECTOR
__traceVector = BallBounceModel.INITIAL_TRACE_VECTOR


def __createWindows():
    """ Creates the windows and show it."""
    global __windows
    global __canvas

    __windows = tkinter.Tk()
    __windows.title("Ball Bounce")
    __windows.geometry(str(__WINDOWS_WIDTH) + "x" + str(__WINDOWS_HEIGHT))
    __canvas = tkinter.Canvas(__windows, bg="black")
    __canvas.pack(fill="both", expand=True)

    __windows.protocol("WM_DELETE_WINDOW", __on_closing)
    __windows.update()


def __getBallX0Transformed():
    """ Converts physical coordinate x to x0."""
    return (BallBounceModel.ball['x'] - BallBounceModel.ball['radius']) * __WINDOWS_ZOOM


def __getBallX1Transformed():
    """ Converts physical coordinate x to x1."""
    return (BallBounceModel.ball['x'] + BallBounceModel.ball['radius']) * __WINDOWS_ZOOM


def __getBallY0Transformed():
    """ Converts physical coordinate y to y0."""
    return __WINDOWS_HEIGHT - ((BallBounceModel.ball['y'] - BallBounceModel.ball['radius']) * __WINDOWS_ZOOM)


def __getBallY1Transformed():
    """ Converts physical coordinate y to y1."""
    return __WINDOWS_HEIGHT - ((BallBounceModel.ball['y'] + BallBounceModel.ball['radius']) * __WINDOWS_ZOOM)


def __getBallX0Arrow():
    """ Converts physical coordinate x to x0Arrow."""
    return BallBounceModel.ball['x'] * __WINDOWS_ZOOM


def __getBallX1Arrow():
    """ Converts physical coordinate x to x1Arrow."""
    return (BallBounceModel.ball['x'] + math.cos(math.radians(BallBounceModel.ball['angle']))
            * BallBounceModel.ball['speedX'] * 2) * __WINDOWS_ZOOM


def __getBallY0Arrow():
    """ Converts physical coordinate y to yArrow."""
    return __WINDOWS_HEIGHT - ((BallBounceModel.ball['y']) * __WINDOWS_ZOOM)


def __getBallY1Arrow():
    """ Converts physical coordinate y to yArrow."""
    return __WINDOWS_HEIGHT - ((BallBounceModel.ball['y'] + math.sin(math.radians(BallBounceModel.ball['angle']))
                                * BallBounceModel.ball['speedY'] * 2) * __WINDOWS_ZOOM)


def __on_closing():
    """ Close properly the windows."""
    BallBounceController.stop()
    __windows.destroy()


def __createBall():
    """ Creates an circle on the windows at the ball's coordinates."""
    global __canvas
    global __ballDraw

    __ballDraw = __canvas.create_oval(__getBallX0Transformed(),
                                      __getBallY0Transformed(),
                                      __getBallX1Transformed(),
                                      __getBallY1Transformed(),
                                      fill='RED',
                                      outline='RED')


def __createArrow():
    global __canvas
    global __arrow

    __arrow = __canvas.create_line(__getBallX0Arrow(),
                                   __getBallY0Arrow(),
                                   __getBallX1Arrow(),
                                   __getBallY1Arrow(),
                                   fill='white',
                                   width=1,
                                   arrow=tkinter.LAST)


def initialize():
    """ Creates an circle on the windows at the ball's coordinates."""
    __createWindows()
    if __showBall:
        __createBall()
    if __showVector:
        __createArrow()


def update():
    """ Replaces the coordinate's circle with those of the balls."""
    global __canvas
    global __windows
    global __ballDraw
    global __arrow

    if __showBall:
        __canvas.coords(__ballDraw, __getBallX0Transformed(), __getBallY0Transformed(), __getBallX1Transformed(),
                        __getBallY1Transformed())
    if __showVector:
        __canvas.coords(__arrow, __getBallX0Arrow(), __getBallY0Arrow(), __getBallX1Arrow(), __getBallY1Arrow())
    if __traceVector:
        __createArrow()
    __windows.update()


def throwBall(ballWindows, x, y, speed, angle, radius, gravity, frictionX, frictionGround, timeInterval, showBall,
              showVector, traceVector):
    """ Creates an circle on the windows at the ball's coordinates."""
    global __showBall
    global __showVector
    global __traceVector

    BallBounceController.changeInitialData(x.get(), y.get(), speed.get(), angle.get(), radius.get(), gravity.get(),
                                           frictionX.get(), frictionGround.get(), timeInterval.get())
    __showBall = showBall.get()
    __showVector = showVector.get()
    __traceVector = traceVector.get()
    ballWindows.destroy()


def ballForm():
    """ Creates a form to change the initial values."""
    ballWindows = tkinter.Tk()
    ballWindows.title("Ball Bounce")
    ballWindows.geometry("250x300")

    x = tkinter.DoubleVar()
    x.set(BallBounceModel.INITIAL_X)
    y = tkinter.DoubleVar()
    y.set(BallBounceModel.INITIAL_Y)
    speed = tkinter.DoubleVar()
    speed.set(BallBounceModel.INITIAL_SPEED)
    angle = tkinter.DoubleVar()
    angle.set(BallBounceModel.INITIAL_ANGLE)
    radius = tkinter.DoubleVar()
    radius.set(BallBounceModel.INITIAL_RADIUS)
    gravity = tkinter.DoubleVar()
    gravity.set(BallBounceModel.GRAVITY)
    frictionX = tkinter.DoubleVar()
    frictionX.set(BallBounceModel.FRICTION_X)
    frictionGround = tkinter.DoubleVar()
    frictionGround.set(BallBounceModel.FRICTION_Y)
    timeInterval = tkinter.DoubleVar()
    timeInterval.set(BallBounceModel.INTERVAL)
    showBall = tkinter.BooleanVar()
    showBall.set(BallBounceModel.INITIAL_SHOW_BALL)
    showVector = tkinter.BooleanVar()
    showVector.set(BallBounceModel.INITIAL_SHOW_VECTOR)
    traceVector = tkinter.BooleanVar()
    traceVector.set(BallBounceModel.INITIAL_TRACE_VECTOR)

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
                   ).grid(row=12, column=1)

    ballWindows.mainloop()
