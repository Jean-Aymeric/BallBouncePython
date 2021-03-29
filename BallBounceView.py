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