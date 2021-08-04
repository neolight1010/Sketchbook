# Butterfly
# by NeoLight
# Function found in: https://www.originlab.com/www/products/GraphGallery.aspx?GID=354

from __future__ import division
import math

t = 0
t_precision = .05

s = 100 # Scale factor
r = 7 # Circle radius

MAX_POINTS = 150 # Maximum number of points to be drawn

b_start_color = color(0) # Starting color of background gradient
b_end_color = color(74, 21, 12) # Starting color of background gradient
G_PRECISION = 50 # Number of rectangles used to perform background gradient

DECIMAL_PRECISION = 100

points = []


class Point():
    def __init__(self, coords, color_obj):
        self.coords = coords
        self.color_obj = color_obj
        
        self.x = self.coords[0]
        self.y = self.coords[1]


def setup():
    size(1336, 768)
    
    # background(background_color)
    stroke(0, 0, 0, 0)
    
def draw():
    global t, b_start_color
    gradient(b_start_color, b_end_color, G_PRECISION)
    
    # Get random point colors
    random_color_r = random(255)
    random_color_g = random(255)
    random_color_b = random(255)
    
    random_color = color(random_color_r, random_color_g, random_color_b)
    
    # Get x and y points
    x = butterfly_x(t, DECIMAL_PRECISION)
    y = butterfly_y(t, DECIMAL_PRECISION)
    
    # Scale
    x = x * s
    y = y * s
    
    # Transpose
    x = x + width / 2
    y = y + (height / 5) * 3
    
    # Delete overflow points
    if len(points) == MAX_POINTS:
        points.pop(0)
    
    # Add new point to array
    print(x, y)
    new_point = Point([x, y], random_color)
    points.append(new_point)
    
    # Draw
    
    for point_obj in points:        
        fill(point_obj.color_obj)
        stroke(0, 0, 0, 0)
        circle(point_obj.x, point_obj.y, r)
    
    if len(points) > 1:
        # Draw line between to last points
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
            middle_color = lerpColor(current_point.color_obj,
                                     next_point.color_obj,
                                     0.5)
            
            stroke(middle_color)
            line(current_point.x, current_point.y,
                 next_point.x, next_point.y)
    
    # Increase t
    t = t + t_precision
    b_start_color = lerpColor(b_start_color, color(255), 0.005)
    
def gradient(start_color, end_color, g_precision):
    width_fraction = width / g_precision
    lerp_fraction = 1 / (g_precision - 1) # -1 allows the last rectangle to be the same as the end color
    
    for i in range(g_precision):
        current_x = width_fraction * i
        current_lerp = lerp_fraction * i
        current_color = lerpColor(start_color, end_color, current_lerp)
        
        noStroke()
        fill(current_color)
        rect(current_x, 0, width_fraction, height)
    
def butterfly_x(t, dec_precision=3):
    x = sin(t) * (exp(cos(t)) - 2 * cos(4*t)-(sin(t/12))**5)
    return round(x, dec_precision)

def butterfly_y(t, dec_precision=3):
    # y axis is inverted to fix different coordinate systems
    y = -(cos(t) * (exp(cos(t)) - 2 * cos(4*t)-(sin(t/12))**5))
    return round(y, dec_precision)
