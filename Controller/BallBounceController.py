"""
Controller : This module contains all the functions to place and move the ball

    PUBLIC
        changeInitialData()
        stop()
        ballBounce()
"""
from View import BallBounceView
from Controller import BallManagement
import time

__run = True


def stop():
    """ Stops the gameloop."""
    global __run
    __run = False


def ballBounce():
    """ The 'GameLoop' function of the controller."""

    """ Change the initial values."""
    BallBounceView.parameterForm()
    BallBounceView.ballBounceForm()
    while __run:
        """ Moves the ball in the Model."""
        BallManagement.moveBall()
        """ Asks the view to update its window."""
        BallBounceView.update()
        """ Wait a little."""
        time.sleep(0.02)
