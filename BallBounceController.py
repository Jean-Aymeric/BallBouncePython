"""
Controller : This module contains all the functions to place and move the ball

    PUBLIC
        moveBall()
        ballBounce()
"""
import BallBounceView
import BallBounceModel
import time
import math


def __moveBall():
    """ Calculates the new position (x,y), new speed (speedX, speedY) of the ball.
        Also controls its bounce.
            x(t+1) = x(t) + Vx(t) * cos(α) * Δt
            Vx(t+1) = Vx(t) with no bounce
            Vx(t+1) = Vx(t) * frictionX on a bounce
            y(t+1) = y(t) + Δt * (Vy(t) - (g * Δt))
            Vy(t+1) = Vy(t) - g * Δt with no bounce
            Vy(t+1) = (Vy(t) - g * Δt) * frictionX on a bounce
    """
    bounceX = False

    """ Calculates the new x, x(t+1)."""
    BallBounceModel.ball['x'] += BallBounceModel.ball['speedX'] \
                                 * math.cos(math.radians(BallBounceModel.ball['angle'])) \
                                 * BallBounceModel.INTERVAL

    """ Calculates the new y, y(t+1)."""
    BallBounceModel.ball['y'] += BallBounceModel.INTERVAL * \
                                 (BallBounceModel.ball['speedY'] - (BallBounceModel.GRAVITY * BallBounceModel.INTERVAL))

    """ Calculates the new speedY, Vy(t+1)."""
    BallBounceModel.ball['speedY'] += - BallBounceModel.GRAVITY * BallBounceModel.INTERVAL

    """ Checks bounce on the left."""
    if BallBounceModel.ball['x'] - BallBounceModel.ball['radius'] <= 0:
        BallBounceModel.ball['x'] = 0 + BallBounceModel.ball['radius']
        bounceX = True

    """ Checks bounce on the right."""
    if BallBounceModel.ball['x'] + BallBounceModel.ball['radius'] >= BallBounceModel.BOX_WIDTH:
        BallBounceModel.ball['x'] = BallBounceModel.BOX_WIDTH - BallBounceModel.ball['radius']
        bounceX = True

    """ Checks bounce on the ground."""
    if BallBounceModel.ball['y'] - BallBounceModel.ball['radius'] <= 0:
        BallBounceModel.ball['y'] = 0 + BallBounceModel.ball['radius']
        """ Applies friction on the new speedY."""
        BallBounceModel.ball['speedY'] = - BallBounceModel.ball['speedY'] * BallBounceModel.FRICTION_Y
        """ Applies friction on the new speedX."""
        BallBounceModel.ball['speedX'] = BallBounceModel.ball['speedX'] * BallBounceModel.FRICTION_X

    """ Calculates the new speedY, Vy(t+1)."""
    if bounceX:
        """ Change angle after a bounce."""
        BallBounceModel.ball['angle'] = (180 - BallBounceModel.ball['angle']) % 360
        """ Applies friction on the new speedX."""
        BallBounceModel.ball['speedX'] = BallBounceModel.ball['speedX'] * BallBounceModel.FRICTION_X


def __changeStartBall(x, y, speed, angle, radius):
    BallBounceModel.ball['x'] = x
    BallBounceModel.ball['y'] = y
    BallBounceModel.ball['speedX'] = speed * math.cos(math.radians(angle))
    BallBounceModel.ball['speedX'] = speed * math.sin(math.radians(angle))
    BallBounceModel.ball['angle'] = angle
    BallBounceModel.ball['radius'] = radius


def ballBounce():
    """ The 'GameLoop' function of the controller."""
    BallBounceView.initialize()
    while 1:
        """ Moves the ball in the Model."""
        __moveBall()
        """ Asks the view to update its window."""
        BallBounceView.update()
        """ Wait a little."""
        time.sleep(0.02)
