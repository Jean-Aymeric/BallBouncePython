from Model import BallBounceModel
from Controller import BallBounceController
import math
import tkinter


__WINDOWS_ZOOM = 1.3
__WINDOWS_WIDTH = int(BallBounceModel.boxWidth * __WINDOWS_ZOOM)
__WINDOWS_HEIGHT = int(BallBounceModel.boxHeight * __WINDOWS_ZOOM)

__root: tkinter.Tk
__canvas = tkinter.Canvas
__ballDraw: tkinter.Canvas
__arrow: tkinter.Canvas
__showBall = BallBounceModel.INITIAL_SHOW_BALL
__showVector = BallBounceModel.INITIAL_SHOW_VECTOR
__traceVector = BallBounceModel.INITIAL_TRACE_VECTOR


def __createWindows():
    """ Creates the windows and show it."""
    global __canvas
    global __root

    __root = tkinter.Tk()
    __canvas = tkinter.Canvas(__root)
    __root.title("Ball Bounce")
    __root.geometry(str(__WINDOWS_WIDTH) + "x" + str(__WINDOWS_HEIGHT))
    __canvas.configure(bg="black")
    __canvas.pack(fill="both", expand=True)

    __root.protocol("WM_DELETE_WINDOW", __on_closing)
    __root.deiconify()
    __root.update()


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
    __root.destroy()


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


def ballBounceForm():
    """ Creates an circle on the windows at the ball's coordinates."""
    __createWindows()
    if __showBall:
        __createBall()
    if __showVector:
        __createArrow()


def update():
    """ Replaces the coordinate's circle with those of the balls."""
    global __canvas
    global __root
    global __ballDraw
    global __arrow

    if __showBall:
        __canvas.coords(__ballDraw, __getBallX0Transformed(), __getBallY0Transformed(), __getBallX1Transformed(),
                        __getBallY1Transformed())
    if __showVector:
        __canvas.coords(__arrow, __getBallX0Arrow(), __getBallY0Arrow(), __getBallX1Arrow(), __getBallY1Arrow())
    if __traceVector:
        __createArrow()
    __root.update()

