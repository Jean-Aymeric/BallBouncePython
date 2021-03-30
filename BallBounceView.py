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

__WINDOWS_ZOOM = 1.3
__WINDOWS_WIDTH = int(BallBounceModel.BOX_WIDTH * __WINDOWS_ZOOM)
__WINDOWS_HEIGHT = int(BallBounceModel.BOX_HEIGHT * __WINDOWS_ZOOM)

__windows = 0
__canvas = 0
__ballDraw = 0


def __createWindows():
    """ Creates the windows and show it."""
    global __windows
    global __canvas

    __windows = tkinter.Tk()
    __windows.title("Ball Bounce")
    __windows.geometry(str(__WINDOWS_WIDTH) + "x" + str(__WINDOWS_HEIGHT))
    __canvas = tkinter.Canvas(__windows, bg="black")
    __canvas.pack(fill="both", expand=True)
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


def __on_closing():
    """ Close properly the windows."""
    BallBounceController.stop()
    __windows.destroy()


def __createBall():
    """ Creates an circle on the windows at the ball's coordinates."""
    global __canvas
    global __windows
    global __ballDraw

    __ballDraw = __canvas.create_oval(__getBallX0Transformed(),
                                      __getBallY0Transformed(),
                                      __getBallX1Transformed(),
                                      __getBallY1Transformed(),
                                      fill='RED',
                                      outline='RED')

    __windows.protocol("WM_DELETE_WINDOW", __on_closing)
    __windows.update()


def initialize():
    """ Creates an circle on the windows at the ball's coordinates."""
    __createWindows()
    __createBall()


def update():
    """ Replaces the coordinate's circle with those of the balls."""
    global __canvas
    global __windows
    global __ballDraw

    __canvas.coords(__ballDraw,
                    __getBallX0Transformed(),
                    __getBallY0Transformed(),
                    __getBallX1Transformed(),
                    __getBallY1Transformed())
    __windows.update()


def throwBall(ballWindows, x, y, speed, angle, radius):
    """ Creates an circle on the windows at the ball's coordinates."""
    BallBounceController.changeStartBall(x.get(), y.get(), speed.get(), angle.get(), radius.get())
    ballWindows.destroy()


def ballForm():
    """ Creates a form to change the initial values."""
    ballWindows = tkinter.Tk()
    ballWindows.title("Ball Bounce")
    ballWindows.geometry("250x140")

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

    tkinter.Button(ballWindows,
                   text='Throw the ball',
                   command=lambda: throwBall(ballWindows, x, y, speed, angle, radius)).grid(row=5, column=1)

    ballWindows.mainloop()
