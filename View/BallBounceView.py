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
from View import ParameterForm
from View import BallBounceForm


def parameterForm():
    ParameterForm.parameterForm()


def ballBounceForm():
    BallBounceForm.ballBounceForm()


def update():
    BallBounceForm.update()