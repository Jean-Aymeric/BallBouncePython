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
INITIAL_X = 25
""" The initial position y(0) of the ball."""
INITIAL_Y = 25
""" The initial speed V(0) of the ball."""
INITIAL_SPEED = 140
""" The initial angle α of the ball."""
INITIAL_ANGLE = 60
""" The radius of the ball."""
INITIAL_RADIUS = 15
""" The default value to show vector on ball."""
INITIAL_SHOW_BALL = True
""" The default value to show vector on ball."""
INITIAL_SHOW_VECTOR = False
""" The default value to trace vector during the move."""
INITIAL_TRACE_VECTOR = False

""" The ball at time 0."""
ball = {'x': INITIAL_X,
        'y': INITIAL_Y,
        'speedX': INITIAL_SPEED * math.cos(math.radians(INITIAL_ANGLE)),
        'speedY': INITIAL_SPEED * math.sin(math.radians(INITIAL_ANGLE)),
        'angle': INITIAL_ANGLE,
        'radius': INITIAL_RADIUS}
