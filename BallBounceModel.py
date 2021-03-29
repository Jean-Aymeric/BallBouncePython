"""
Model : This module contains all the constants and the ball
"""
import math

""" The gravity, g."""
GRAVITY = 9.80665
""" The time interval, Δt."""
INTERVAL = 0.4
""" The friction on left an right, frictionX."""
FRICTION_X = 0.95
""" The friction on ground, frictionY."""
FRICTION_Y = 0.85
""" The box width in which the ball bounces."""
BOX_WIDTH = 800
""" The box height in which the ball bounces."""
BOX_HEIGHT = 600

""" The initial position x(0) of the ball."""
__INITIAL_X = 25
""" The initial position y(0) of the ball."""
__INITIAL_Y = 25
""" The initial speed V(0) of the ball."""
__INITIAL_SPEED = 140
""" The initial angle α of the ball."""
__INITIAL_ANGLE = 60
""" The radius of the ball."""
__INITIAL_RADIUS = 15

""" The ball at time 0."""
ball = {'x': __INITIAL_X,
        'y': __INITIAL_Y,
        'speedX': __INITIAL_SPEED * math.cos(math.radians(__INITIAL_ANGLE)),
        'speedY': __INITIAL_SPEED * math.sin(math.radians(__INITIAL_ANGLE)),
        'angle': __INITIAL_ANGLE,
        'radius': __INITIAL_RADIUS}
