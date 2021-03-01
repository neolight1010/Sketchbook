# Butterfly
# https://www.originlab.com/www/products/GraphGallery.aspx?GID=354

t = 0
s = 100
r = 7
t_precision = 0.05
MAX_POINTS = 125 # Maximum number of points to be drawn
# background_color = color(0, 0, 0)

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
    global t
    custom_background()
    
    # Get random point colors
    random_color_r = random(255)
    random_color_g = random(255)
    random_color_b = random(255)
    
    random_color = color(random_color_r, random_color_g, random_color_b)
    
    # Get x and y points
    x = butterfly_x(t)
    y = butterfly_y(t)
    
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
    new_point = Point([x, y], random_color)
    points.append(new_point)
    
    # Draw
    print(x, y)
    
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
    
def custom_background():
    for x in range(width):
        # stroke(12, 156, 200)
        stroke(0)
        line(x, 0, x, height)
    
def butterfly_x(t):
    return sin(t) * (exp(cos(t)) - 2 * cos(4*t)-(sin(t/12))**5)

def butterfly_y(t):
    # y axis is inverted to fix different coordinate systems
    return -(cos(t) * (exp(cos(t)) - 2 * cos(4*t)-(sin(t/12))**5))
