from Model import BallBounceModel
import math


def moveBall():
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
    bounceY = False

    """ Calculates the new x, x(t+1)."""
    BallBounceModel.ball['x'] += BallBounceModel.ball['speedX'] * math.cos(
        math.radians(BallBounceModel.ball['angle'])) * BallBounceModel.interval

    """ Calculates the new y, y(t+1)."""
    BallBounceModel.ball['y'] += BallBounceModel.interval * (
            BallBounceModel.ball['speedY'] - (BallBounceModel.gravity * BallBounceModel.interval))

    """ Calculates the new speedY, Vy(t+1)."""
    BallBounceModel.ball['speedY'] += - BallBounceModel.gravity * BallBounceModel.interval

    """ Checks bounce on the left."""
    if BallBounceModel.ball['x'] - BallBounceModel.ball['radius'] <= 0:
        BallBounceModel.ball['x'] = 0 + BallBounceModel.ball['radius']
        bounceX = True

    """ Checks bounce on the right."""
    if BallBounceModel.ball['x'] + BallBounceModel.ball['radius'] >= BallBounceModel.boxWidth:
        BallBounceModel.ball['x'] = BallBounceModel.boxWidth - BallBounceModel.ball['radius']
        bounceX = True

    """ Checks bounce on the ground."""
    if BallBounceModel.ball['y'] - BallBounceModel.ball['radius'] <= 0:
        BallBounceModel.ball['y'] = 0 + BallBounceModel.ball['radius']
        bounceY = True

    """ Checks bounce on the top."""
    if BallBounceModel.ball['y'] + BallBounceModel.ball['radius'] >= BallBounceModel.boxHeight:
        BallBounceModel.ball['y'] = BallBounceModel.boxHeight - BallBounceModel.ball['radius']
        bounceY = True

    """ Calculates the new speedY, Vy(t+1)."""
    if bounceX:
        """ Change angle after a bounce."""
        BallBounceModel.ball['angle'] = (180 - BallBounceModel.ball['angle']) % 360
        """ Applies friction on the new speedX."""
        BallBounceModel.ball['speedX'] = BallBounceModel.ball['speedX'] * BallBounceModel.frictionX

    if bounceY:
        """ Applies friction on the new speedY."""
        BallBounceModel.ball['speedY'] = - BallBounceModel.ball['speedY'] * BallBounceModel.frictionGround
        """ Applies friction on the new speedX."""
        BallBounceModel.ball['speedX'] = BallBounceModel.ball['speedX'] * BallBounceModel.frictionGround
